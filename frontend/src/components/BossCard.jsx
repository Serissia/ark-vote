import React from 'react';
import './BossCard.css';

const BossCard = ({ name, img, desc }) => {
  return (
    <div className="boss-card-unit">
      <div className="boss-header-bar">{name}</div>
      <div className="boss-body">
        <div className="boss-img-container">
          <img src={img} alt={name} className="boss-img-fixed" />
        </div>
        <div className="boss-desc-area">
          <p>{desc}</p>
        </div>
      </div>
    </div>
  );
};

export default BossCard;