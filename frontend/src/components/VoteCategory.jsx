import React from 'react';
import './VoteCategory.css';

const VoteCategory = ({ category, selectedIds, onSelect, isSubmitted }) => {
  return (
    <div className={`category-block ${isSubmitted ? 'submitted' : ''}`}>
      <div className="category-header">
        <h2 className="category-title">{category.title}</h2>
        <p className="category-subtitle">{category.subtitle}</p>
      </div>

      <div className="candidates-grid">
        {category.candidates.map((candidate) => {
          // 获取当前干员在选中列表中的次序
          const orderIndex = selectedIds.indexOf(candidate.id);
          const isSelected = orderIndex !== -1;

          return (
            <div
              key={candidate.id}
              className={`role-card ${isSelected ? 'selected' : ''}`}
              onClick={() => onSelect(candidate.id)}
            >
              <img src={candidate.img_half} alt={candidate.name} className="role-image" />
              
              {/* 动态显示选中的次序 (1, 2, 3...) */}
              {isSelected && <div className="order-badge">{orderIndex + 1}</div>}

              <div className="role-info">
                <div className="role-name">{candidate.name}</div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default VoteCategory;