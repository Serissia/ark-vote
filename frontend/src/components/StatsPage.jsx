import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Spin, Empty, Card, Divider } from 'antd';
import './StatsPage.css';

const StatsPage = () => {
  const [statsData, setStatsData] = useState(null);
  const [categories, setCategories] = useState([]);
  const [spStats, setSpStats] = useState([]);
  const [loading, setLoading] = useState(true);

  const isDLCUnlocked = localStorage.getItem('sp_voted_box_ids') !== null;

  useEffect(() => {
    const fetchData = async () => {
      try {
        Promise.all([
          axios.get('/api/config'),
          axios.get('/api/stats')
        ]).then(([configRes, statsRes]) => {
          setCategories(configRes.data.categories);
          setStatsData(statsRes.data.stats);
        });

        if (isDLCUnlocked) {
          Promise.all([
            axios.get('/api/sp/stats')
          ]).then(([spStatsRes]) => {
            setSpStats(spStatsRes.data.stats);
          });
        }
      } catch (err) {
        console.error("加载统计失败", err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [isDLCUnlocked]);

  useEffect(() => {
    // 同时获取配置和统计分数
    Promise.all([
      axios.get('/api/config'),
      axios.get('/api/stats')
    ]).then(([configRes, statsRes]) => {
      setCategories(configRes.data.categories);
      setStatsData(statsRes.data.stats);
      setLoading(false);
    });
  }, []);

  if (loading) return <div className="stats-loading"><Spin size="large" tip="正在翻阅档案..." /></div>;
  if (!statsData) return <Empty description="暂无数据" />;

  return (
    <div className="stats-container">
      <header className="stats-tower-header">
        <h1>年度投票统计中心</h1>
      </header>

      {categories.map(cat => {
        const catStats = statsData[cat.id] || [];
        // 获取最高分，用于计算条形图比例
        const maxScore = catStats.length > 0 ? catStats[0][1] : 1;

        return (
          <div key={cat.id} className="stats-section">
            <h2 className="stats-title">{cat.title}</h2>
            
            <div className="stats-list">
              {catStats.map(([candId, score], index) => {
                // 根据 ID 找到对应的干员详细信息
                const info = cat.candidates.find(c => c.id === candId);
                const percentage = (score / maxScore) * 100;
                const isTopOne = index === 0 && score > 0;

                return (
                  <div key={candId} className={`stats-row ${isTopOne ? 'top-one-row' : ''}`}>
                    {/* 排名 */}
                    <div className="rank-num">
                      {isTopOne ? <span className="crown-icon">👑</span> : index + 1}
                    </div>
                    
                    {/* 头像 */}
                    <div className="avatar-box">
                      <img src={info?.img_avatar} alt={info?.name} className="stat-avatar" />
                    </div>

                    {/* 名字与条形图 */}
                    <div className="bar-area">
                      <div className="name-score">
                        <span className={isTopOne ? 'top-one-name' : ''}>
                        {info?.name} {isTopOne && <small>(冠军)</small>}
                        </span>
                        <span className="score-val">{score} 分</span>
                      </div>
                      <div className="bar-bg">
                        <div 
                          className={`bar-fill ${isTopOne ? 'top-one-fill' : ''}`} 
                          style={{ width: `${percentage}%`, transitionDelay: `${index * 0.1}s` }}
                        ></div>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        );
      })}

      {isDLCUnlocked && spStats.length > 0 && (
        <div className="stats-floor-item sp-unlocked-floor">
          <Divider className="sp-divider">记忆回响</Divider>
          <div className="sp-stats-grid">
            {spStats.map((item, index) => (
              <div key={item.id} className={`sp-stat-card rank-${index + 1}`}>
                <div className="sp-rank-crown">{index + 1}</div>
                <div className="sp-boss-avatars">
                  {item.bosses.map(b => (
                    <img key={b.id} src={b.img_avatar} alt={b.name} className="sp-mini-avatar" />
                  ))}
                </div>
                <div className="sp-stat-info">
                  <div className="sp-stat-names">
                    {item.bosses.map(b => b.name).join(' & ')}
                  </div>
                  <div className="sp-stat-theme">{item.theme_title}</div>
                  <div className="sp-stat-score">分数：{item.score}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {!isDLCUnlocked && (
        <div className="sp-locked-hint">
          <p>有些记忆，似乎被埋藏在了更深处...</p>
        </div>
      )}
    </div>
  );
};

export default StatsPage;