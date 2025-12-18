import { useState } from 'react';
import Navbar from './components/Navbar';
import { Layout } from 'antd'; // 使用 AntD 的布局容器

const { Content } = Layout;

function App() {
  // 定义一个状态，记录当前是在 "vote" 页面还是 "stats" 页面
  const [currentTab, setCurrentTab] = useState('vote');

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#0a0a0a' }}>
      {/* 1. 放置导航栏 */}
      <Navbar 
        activeTab={currentTab} 
        onTabChange={(tab) => setCurrentTab(tab)} 
      />

      {/* 2. 主内容区域 */}
      <div style={{ paddingTop: '80px', color: 'white', textAlign: 'center' }}>
        
        {currentTab === 'vote' && (
          <div>
            <h1>🗳️ 投票区域</h1>
            <p>这里将显示干员列表...</p>
          </div>
        )}

        {currentTab === 'stats' && (
          <div>
            <h1>📊 数据统计区域</h1>
            <p>这里将显示条形图...</p>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;