import React, { useState } from 'react';
import Navbar from './components/Navbar';
import VotePage from './components/VotePage';
import StatsPage from './components/StatsPage';

function App() {
  // 定义一个状态，记录当前是在 "vote" 页面还是 "stats" 页面
  const [activeTab, setActiveTab] = useState('vote');

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#0a0a0a' }}>
      {/* 1. 放置导航栏 */}
      <Navbar activeTab={activeTab} onTabChange={setActiveTab} />

      {/* 2. 主内容区域 */}
      <main style={{ paddingTop: '100px', maxWidth: '1400px', margin: '0 auto' }}>
        {activeTab === 'vote' && (
          <VotePage />
        )}
        {activeTab === 'stats' && (
          <StatsPage />
        )}
      </main>
    </div>
  );
}

export default App;