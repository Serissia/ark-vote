// src/components/Navbar.jsx
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faVoteYea, faChartBar, faCube } from '@fortawesome/free-solid-svg-icons';
import { GithubOutlined } from '@ant-design/icons';
import { Tooltip, Modal } from 'antd';
import './Navbar.css';

const Navbar = ({ activeTab, onTabChange }) => {
    const isVotingEnded = () => {
        const deadline = new Date('2026-01-01T00:00:00');
        return new Date() >= deadline;
    };

    const ended = isVotingEnded();
    const isDLCUnlocked = ended || localStorage.getItem('sp_is_submitted') !== null;

    const handleStatsClick = () => {
        if (!isDLCUnlocked && activeTab !== 'stats') {
            Modal.confirm({
                title: '提示',
                content: '你尚未进入隐藏页面并进行投票，现在就前往总数据页面吗？',
                okText: '确认',
                cancelText: '取消',
                onOk: () => onTabChange('stats')
            });
        } else {
            onTabChange('stats');
        }
    };

    return (
        <nav className="glass-nav">
            {/* 标题部分 */}
            <div className="nav-title">
                <FontAwesomeIcon icon={faCube} style={{ color: '#66c0f4'}} />
                <span>2025年度明日方舟干员投票</span>
            </div>

            {/* 导航链接部分 */}
            <div className="nav-menu">
                <div
                    className={`nav-item ${activeTab === 'vote' ? 'active' : ''}`}
                    onClick={() => onTabChange('vote')}
                >
                    <FontAwesomeIcon icon={faVoteYea} />
                    <span>去投票</span>
                </div>

                <div 
                    className={`nav-item ${activeTab === 'stats' ? 'active' : ''}`}
                    onClick={handleStatsClick}
                >
                    <FontAwesomeIcon icon={faChartBar} />
                    <span>总数据</span>
                </div>

                <div
                    className="nav-item"
                >
                    <Tooltip title="前往 GitHub 仓库">
                        <a 
                            href="https://github.com/Serissia/ark-vote"
                            target="_blank"
                            rel="noopener noreferrer"
                            className="github-link"
                        >
                            <GithubOutlined style={{ fontSize: '22px' }} />
                        </a>
                    </Tooltip>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;