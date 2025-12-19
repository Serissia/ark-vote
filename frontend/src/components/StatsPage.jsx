import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Spin, Empty } from 'antd';
import './StatsPage.css';

const StatsPage = () => {
  const [statsData, setStatsData] = useState(null);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);

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

  if (loading) return <div style={{ textAlign: 'center', marginTop: 100 }}><Spin size="large" /></div>;
  if (!statsData) return <Empty description="暂无投票数据" />;

  return (
    <div className="stats-container">
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
    </div>
  );
};

export default StatsPage;