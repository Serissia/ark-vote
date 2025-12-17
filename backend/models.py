# backend/models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class VoteRecord(db.Model):
    """
    投票记录表
    记录谁(IP/User)、在什么时候、投给了哪个奖项、选了哪些人
    """
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), nullable=False) # 简易身份标识
    category_id = db.Column(db.String(50), nullable=False) # 对应 config 中的 id
    
    # 存储选中的干员ID，用逗号分隔的字符串存储 (例如: "kaltsit,reed_alt")
    choices = db.Column(db.String(500), nullable=False) 
    
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Vote {self.ip_address} -> {self.category_id}: {self.choices}>"