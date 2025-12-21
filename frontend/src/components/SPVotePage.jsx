import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { message, Button, Spin, Result, Space, Popconfirm } from 'antd';
import BossCard from '../components/BossCard';
import './SPVotePage.css';
import BgmPlayer from '../components/BgmPlayer';

const SPVotePage = ({ onClose }) => {
  const [config, setConfig] = useState(null);
  const [isSubmitted, setIsSubmitted] = useState(() => {
    const saved = localStorage.getItem('sp_is_submitted');
    return saved ? JSON.parse(saved) : false;
  });
  const [loading, setLoading] = useState(true);

  const [selectedBoxIds, setSelectedBoxIds] = useState(() => {
    const saved = localStorage.getItem('sp_voted_box_ids');
    return saved ? JSON.parse(saved) : [];
  });

  useEffect(() => {
    // 切换页面时，立刻回到顶部
    window.scrollTo(0, 0);
  }, []);

  useEffect(() => {
    // 请求专属的 SP 接口
    axios.get('/api/sp/config').then(res => {
      setConfig(res.data);
      setLoading(false);
    }).catch(() => {
      message.error("DLC 记忆提取失败");
      setLoading(false);
    });
  }, []);

  useEffect(() => {
    localStorage.setItem('sp_voted_box_ids', JSON.stringify(selectedBoxIds));
  }, [selectedBoxIds]);

  useEffect(() => {
    localStorage.setItem('sp_is_submitted', JSON.stringify(isSubmitted));
  }, [isSubmitted]);

  const handleSelect = (id) => {
    if (isSubmitted) return;
    if (selectedBoxIds.includes(id)) {
      setSelectedBoxIds(selectedBoxIds.filter(i => i !== id));
    } else if (selectedBoxIds.length < (config?.max_choices || 4)) {
      setSelectedBoxIds([...selectedBoxIds, id]);
    } else {
      message.warning(`理智不足，最多只能标记 ${config.max_choices} 个 Boss 组`);
    }
  };

  const handleClear = () => {
    setSelectedBoxIds([]);
    localStorage.removeItem('sp_voted_box_ids');
    message.info("记忆已重置。");
  };

  const handleSubmit = () => {
    axios.post('/api/sp/submit', { box_ids: selectedBoxIds }).then(() => {
      setIsSubmitted(true);
      message.success("记忆已成功封存。");
    });
  };

  const isVotingEnded = () => {
    const deadline = new Date('2026-01-01T00:00:00');
    return new Date() >= deadline;
  };

  const ended = isVotingEnded();

  if (loading) return <div className="sp-loading-container"><Spin size="large" /></div>;
  if (!config) return <Result status="404" title="记忆缺失" />;

  return (
    <div className="sp-page-overlay">
      <BgmPlayer audioUrl="/audio/碧瞳中.mp3" label="in your blue eyes" />
      <div className="sp-page-container">
        <header className="sp-header">
          <h1>{config.title}</h1>
          <p className="sp-subtitle">{config.subtitle}</p>
        </header>

        <main className="sp-main-content">
          {config.themes.map((theme, tIdx) => (
            <section key={tIdx} className="theme-group">
              <div className="theme-title-container">
                <span className="theme-title-line"></span>
                <h2 className="theme-title-text">{theme.title}</h2>
                <span className="theme-title-line"></span>
              </div>
              
              <div className="theme-boxes-grid">
                {theme.boxes.map(box => {
                  const rankIdx = selectedBoxIds.indexOf(box.id);
                  const isSelected = rankIdx !== -1;
                  return (
                    <div 
                      key={box.id} 
                      className={`cand-box-item ${isSelected ? 'active' : ''}`}
                      onClick={() => handleSelect(box.id)}
                    >
                      {isSelected && <div className="sp-rank-num">{rankIdx + 1}</div>}
                      {/* 修复 img 属性传参：将后端 img_avatar 映射给 BossCard 的 img */}
                      {box.boss_details.map(boss => (
                        <BossCard 
                          key={boss.id} 
                          name={boss.name} 
                          img={boss.img_avatar} 
                          desc={boss.desc} 
                        />
                      ))}
                    </div>
                  );
                })}
              </div>
            </section>
          ))}
        </main>

        <footer className="sp-footer">
          <Space size="large">
            <Button onClick={onClose} size="large">返回主页</Button>
            
            <Popconfirm 
              title="确定要清除所有已选的 Boss 吗？" 
              onConfirm={handleClear} 
              okText="确定" 
              cancelText="取消"
            >
              <Button size="large" disabled = {isSubmitted || ended}>清除选项</Button>
            </Popconfirm>

            <Button 
              type="primary" 
              danger 
              size="large" 
              disabled={selectedBoxIds.length === 0 || isSubmitted || ended}
              onClick={handleSubmit}
            >
              {isSubmitted ? "记忆已封存" : "提交记忆"}
            </Button>
          </Space>
        </footer>
      </div>
    </div>
  );
};

export default SPVotePage;