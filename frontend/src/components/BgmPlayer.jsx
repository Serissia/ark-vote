import React, { useState, useRef, useEffect } from 'react';
import { Button, Tooltip, message } from 'antd';
import { SoundOutlined, MutedOutlined, LoadingOutlined } from '@ant-design/icons';
import './BgmPlayer.css';

const BgmPlayer = ({ audioUrl, label }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const audioRef = useRef(null);

  useEffect(() => {
    return () => {
      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current.src = "";
        audioRef.current = null;
      }
    };
  }, []);

  const handleTogglePlay = async () => {
    if (!audioRef.current) {
      setIsLoading(true);
      try {
        const audio = new Audio(audioUrl);
        audio.loop = true;
        await new Promise((resolve, reject) => {
          audio.oncanplaythrough = resolve;
          audio.onerror = reject;
          audio.load();
        });
        audioRef.current = audio;
      } catch (error) {
        message.error("无法同步神经链接");
        setIsLoading(false);
        return;
      }
      setIsLoading(false);
    }

    const audio = audioRef.current;
    if (isPlaying) {
      audio.pause();
    } else {
      audio.play().catch(() => message.warning("需要手动唤醒音频流"));
    }
    setIsPlaying(!isPlaying);
  };

  return (
    <div className={`bgm-fixed-anchor ${isPlaying ? 'is-active' : ''}`}>
      {isPlaying && <div className="bgm-pulse-ring"></div>}
      
      <Tooltip title={isPlaying ? "静默" : `唤醒记忆：${label}`} placement="left">
        <Button 
          type="text"
          className={`bgm-ark-btn ${isPlaying ? 'playing' : ''}`}
          icon={isLoading ? <LoadingOutlined /> : (isPlaying ? <SoundOutlined /> : <MutedOutlined />)} 
          onClick={handleTogglePlay}
        />
      </Tooltip>
      
      {/* 侧边小装饰条 */}
      <div className="bgm-deco-line"></div>
    </div>
  );
};

export default BgmPlayer;