import React, { useState, useRef, useEffect } from 'react';
import { Button, Tooltip } from 'antd';
import { SoundOutlined, MutedOutlined } from '@ant-design/icons';
import './BgmPlayer.css';

const BgmPlayer = ({ audioUrl, label }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef(new Audio(audioUrl));

  useEffect(() => {
    const audio = audioRef.current;
    audio.loop = True; // 循环播放
    
    // 强制设置初始状态
    audio.pause(); 

    // 组件卸载时停止音乐
    return () => {
      audio.pause();
      audio.currentTime = 0;
    };
  }, []);

  const togglePlay = () => {
    if (isPlaying) {
      audioRef.current.pause();
    } else {
      audioRef.current.play().catch(err => {
        console.error("播放失败:", err);
      });
    }
    setIsPlaying(!isPlaying);
  };

  return (
    <div className="bgm-player-widget">
      <Tooltip title={isPlaying ? "关闭音乐" : `播放 BGM: ${label}`}>
        <Button 
          shape="circle" 
          icon={isPlaying ? <SoundOutlined spin /> : <MutedOutlined />} 
          onClick={togglePlay}
          danger={isPlaying}
          className="bgm-btn"
        />
      </Tooltip>
    </div>
  );
};

export default BgmPlayer;