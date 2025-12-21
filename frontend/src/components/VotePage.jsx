import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { message } from 'antd';
import VoteCategory from '../components/VoteCategory';
import SPVotePage from '../components/SPVotePage';
import './VotePage.css';
import BgmPlayer from '../components/BgmPlayer';

const VotePage = () => {
  const [categories, setCategories] = useState([]);
  
  // 从本地读取数据
  const [votes, setVotes] = useState(() => {
    const saved = localStorage.getItem('ark_votes');
    return saved ? JSON.parse(saved) : {};
  }); // { catId: [id1, id2] }
  const [submittedStatus, setSubmittedStatus] = useState(() => {
    const saved = localStorage.getItem('ark_submitted_status');
    return saved ? JSON.parse(saved) : {};
  }); // { catId: true/false }

  const [showDLC, setShowDLC] = useState(false);

  useEffect(() => {
    // 切换页面时，立刻回到顶部
    window.scrollTo(0, 0);
  }, []);

  useEffect(() => {
    // 从后端 API 获取配置
    axios.get('/api/config')
      .then(res => setCategories(res.data.categories))
      .catch(err => message.error("无法加载配置数据"));
  }, []);

  useEffect(() => {
    localStorage.setItem('ark_votes', JSON.stringify(votes));
  }, [votes]);

  useEffect(() => {
    localStorage.setItem('ark_submitted_status', JSON.stringify(submittedStatus));
  }, [submittedStatus]);

  const handleSelect = (catId, candId) => {
    if (submittedStatus[catId]) return; // 如果该奖项已提交，禁止操作

    // 找到该奖项的最大选择数限制
    const catConfig = categories.find(c => c.id === catId);
    const maxChoices = catConfig.max_choices;

    const currentSelected = votes[catId] || [];

    if (currentSelected.includes(candId)) {
      // 取消选中
      setVotes({ ...votes, [catId]: currentSelected.filter(id => id !== candId) });
    } else if (currentSelected.length < maxChoices) {
      // 检查是否达到上限
      setVotes({ ...votes, [catId]: [...currentSelected, candId] });
    } else {
      message.warning(`该奖项最多只能选择 ${maxChoices} 位干员`);
    }
  };

  // 针对单个奖项的清空
  const handleClear = (catId) => {
    const newVotes = { ...votes };
    delete newVotes[catId];
    setVotes(newVotes);

    const newStatus = { ...submittedStatus };
    delete newStatus[catId];
    setSubmittedStatus(newStatus);
  };

  // 针对单个奖项的提交
  const handleSubmit = (catId) => {
    const selected = votes[catId] || [];
    if (selected.length === 0) return;

    // 发送数据到后端 API
    axios.post('/api/vote', {
      category_id: catId,
      choices: selected
    }).then(res => {
      if (res.data.status === 'success') {
        setSubmittedStatus({ ...submittedStatus, [catId]: true });
        message.success(`投票成功！`);
      }
    }).catch(err => message.error("提交失败，请稍后重试"));
  };

  const isVotingEnded = () => {
    const deadline = new Date('2026-01-01T00:00:00');
    return new Date() >= deadline;
  };

  const ended = isVotingEnded();

  return (
    <div className="vote-page-container">
      {ended && (
        <div className="vote-ended-banner">
          ⚠️ 2025 年度投票已圆满结束，当前仅供浏览。请前往“总数据”查看最终统计。
        </div>
      )}

      {!showDLC ? (
        <><BgmPlayer audioUrl="/audio/已至.mp3" label="...已至" />
          {categories.map(cat => (
            <VoteCategory
            key={cat.id}
            category={cat}
            selectedIds={votes[cat.id] || []}
            isSubmitted={submittedStatus[cat.id] || ended} // 独立的提交状态
            onSelect={(candId) => handleSelect(cat.id, candId)}
            onClear={() => handleClear(cat.id)}
            onSubmit={() => handleSubmit(cat.id)}
            />
          ))}
          
          {/* 隐秘入口 */}
          <div className="dlc-entrance-container" style={{ textAlign: 'center', marginTop: '100px' }}>
            <button className="ghost-dlc-btn" onClick={() => setShowDLC(true)}>
              回忆往昔...
            </button>
          </div>
        </>
      ) : (
        /* 进入 DLC 页面 */
        <SPVotePage onClose={() => setShowDLC(false)} />
      )}
    </div>
  );
};

export default VotePage;