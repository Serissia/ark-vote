import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Space, message, Divider } from 'antd';
import VoteCategory from '../components/VoteCategory';

const VotePage = () => {
  const [categories, setCategories] = useState([]);
  const [votes, setVotes] = useState({}); // 格式: { categoryId: [id1, id2] }
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    // 从后端 API 获取配置
    axios.get('/api/config')
      .then(res => setCategories(res.data.categories))
      .catch(err => message.error("无法加载配置数据"));
  }, []);

  const handleSelect = (catId, candId) => {
    if (isSubmitted) return;

    // 找到该奖项的最大选择数限制
    const catConfig = categories.find(c => c.id === catId);
    const maxChoices = catConfig.max_choices;

    const currentSelected = votes[catId] || [];

    if (currentSelected.includes(candId)) {
      // 取消选中
      setVotes({ ...votes, [catId]: currentSelected.filter(id => id !== candId) });
    } else {
      // 检查是否达到上限
      if (currentSelected.length < maxChoices) {
        setVotes({ ...votes, [catId]: [...currentSelected, candId] });
      } else {
        message.warning(`该奖项最多只能选择 ${maxChoices} 位干员`);
      }
    }
  };

  const handleSubmit = () => {
    if (Object.keys(votes).length === 0) {
      return message.warning("请至少投出一票再提交");
    }
    // 模拟提交成功
    setIsSubmitted(true);
    message.success("投票成功！");
    console.log("最终投票结果：", votes);
  };

  const handleClear = () => {
    setVotes({});
    setIsSubmitted(false);
  };

  return (
    <div style={{ paddingBottom: '100px' }}>
      {categories.map(cat => (
        <VoteCategory
          key={cat.id}
          category={cat}
          selectedIds={votes[cat.id] || []}
          onSelect={(candId) => handleSelect(cat.id, candId)}
          isSubmitted={isSubmitted}
        />
      ))}

      {/* 底部交互按钮 */}
      <Divider style={{ borderColor: 'rgba(255,255,255,0.1)' }} />
      <div style={{ textAlign: 'center', marginTop: '40px' }}>
        <Space size="large">
          <Button
            ghost size="large"
            onClick={handleClear}
            disabled={isSubmitted}
          >
            清空所有选择
          </Button>
          <Button 
            type="primary" 
            size="large" 
            onClick={handleSubmit} 
            disabled={isSubmitted}
            style={{ backgroundColor: '#a4d007', borderColor: '#a4d007', color: '#000', fontWeight: 'bold' }}
          >
            确认提交投票
          </Button>
        </Space>
      </div>
    </div>
  );
};

export default VotePage;