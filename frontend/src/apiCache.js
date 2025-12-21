// src/apiCache.js

export let configCache = null;
export let statsCache = null;
export let spStatsCache = null;

export const setConfigCache = (data) => { configCache = data; };
export const setStatsCache = (data) => { statsCache = data; };
export const setSpStatsCache = (data) => { spStatsCache = data; };

export const invalidateStatsCache = () => {
  statsCache = null;
  spStatsCache = null;
  console.log("检测到投票行为，统计缓存已失效，下次进入将重新请求。");
};