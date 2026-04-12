<template>
  <div class="absolute left-0 top-0 w-full h-full overflow-hidden bg-gradient">
    <div class="sun-glow"></div>

    <svg class="absolute inset-0 w-full h-full" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="sun-arc-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="rgba(245, 158, 11, 0.5)" />
          <stop offset="100%" stop-color="rgba(245, 158, 11, 0)" />
        </linearGradient>
      </defs>

      <circle cx="25%" cy="75%" r="35%" fill="none" stroke="url(#sun-arc-grad)" stroke-width="2" class="arc arc-1" />
      <circle cx="25%" cy="75%" r="55%" fill="none" stroke="url(#sun-arc-grad)" stroke-width="1.5" class="arc arc-2" />
      <circle cx="25%" cy="75%" r="80%" fill="none" stroke="url(#sun-arc-grad)" stroke-width="0.5" class="arc arc-3" />
    </svg>

    <div class="particles">
      <div v-for="i in 30" :key="i" class="particle" :style="getParticleStyle()"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
/**
 * 随机生成粒子的初始位置、大小和动画时长
 */
const getParticleStyle = () => {
  const size = Math.random() * 4 + 2 + 'px';
  const left = Math.random() * 100 + '%';
  const top = Math.random() * 100 + '%';
  const duration = Math.random() * 15 + 10 + 's'; // 10s - 25s
  const delay = Math.random() * -20 + 's'; // 负延迟让粒子一开始就散布满屏幕

  return {
    width: size,
    height: size,
    left,
    top,
    animationDuration: duration,
    animationDelay: delay
  };
};
</script>

<style scoped>
/* 深邃底色，衬托金橙色发光 */
.bg-gradient {
  background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #451a03 100%);
}

/* 左下角的太阳核心光晕 */
.sun-glow {
  position: absolute;
  left: 10%;
  bottom: -15%;
  width: 60vw;
  height: 60vw;
  background: radial-gradient(circle, rgba(245, 158, 11, 0.3) 0%, rgba(245, 158, 11, 0.1) 40%, transparent 70%);
  border-radius: 50%;
  filter: blur(60px);
  animation: pulse 6s ease-in-out infinite alternate;
}

/* 弧线的变形与旋转动画 */
.arc {
  transform-origin: 25% 75%;
}
.arc-1 { animation: spin 45s linear infinite; }
.arc-2 { animation: spin 70s linear infinite reverse; }
.arc-3 { animation: spin 100s linear infinite; }

/* 粒子基础样式与上升漂浮动画 */
.particles {
  position: absolute;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
.particle {
  position: absolute;
  background: rgba(255, 215, 0, 0.6);
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(255, 215, 0, 0.4);
  animation: float linear infinite;
}

/* 动画定义 */
@keyframes pulse {
  0% { transform: scale(0.85); opacity: 0.7; }
  100% { transform: scale(1.15); opacity: 1; }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes float {
  0% { transform: translateY(0) scale(1); opacity: 0; }
  20% { opacity: 1; }
  80% { opacity: 1; }
  100% { transform: translateY(-80vh) scale(0.5); opacity: 0; }
}
</style>