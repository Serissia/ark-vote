import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { message } from 'antd';
import VoteCategory from '../components/VoteCategory';

const VotePage = () => {
  const [categories, setCategories] = useState([]);
  const [votes, setVotes] = useState({}); // { catId: [id1, id2] }
  const [submittedStatus, setSubmittedStatus] = useState({}); // { catId: true/false }

  useEffect(() => {
    // 从后端 API 获取配置
    axios.get('/api/config')
      .then(res => setCategories(res.data.categories))
      .catch(err => message.error("无法加载配置数据"));
  }, []);

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
    setVotes({ ...votes, [catId]: [] });
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
        message.success(`${catId} 投票成功！`);
      }
    }).catch(err => message.error("提交失败，请稍后重试"));
  };

  return (
    <div className="vote-page-container">
      {categories.map(cat => (
        <VoteCategory
          key={cat.id}
          category={cat}
          selectedIds={votes[cat.id] || []}
          isSubmitted={submittedStatus[cat.id]} // 独立的提交状态
          onSelect={(candId) => handleSelect(cat.id, candId)}
          onClear={() => handleClear(cat.id)}
          onSubmit={() => handleSubmit(cat.id)}
        />
      ))}
    </div>
  );
};

export default VotePage;