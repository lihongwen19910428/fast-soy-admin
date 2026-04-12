<template>
  <div class="absolute left-0 top-0 w-full h-full overflow-hidden bg-[#0a0a0a]">
    <img 
      :src="bgImage" 
      class="absolute left-0 top-0 w-full h-full object-cover z-0"
      alt="SUN Design Background"
    />
    
    <div class="absolute inset-0 z-1 theme-overlay"></div>
    
    <div class="particles z-2">
      <div v-for="i in 25" :key="i" class="particle" :style="getParticleStyle()"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
// ✅ 关键修改 1：使用 ESM 方式导入本地图片
import bgImage from '@/assets/imgs/sun-bg.jpg';

interface Props {
  themeColor?: string;
}

const props = withDefaults(defineProps<Props>(), {
  themeColor: '#f59e0b'
});

const hexToRgb = (hex?: string) => {
  // ✅ 关键修改 2：增加强容错，防止因空值导致 replace 报错，引发组件渲染崩溃
  if (!hex || typeof hex !== 'string') return '245, 158, 11';
  try {
    const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    const fullHex = hex.replace(shorthandRegex, (_m, r, g, b) => r + r + g + g + b + b);
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(fullHex);
    return result
      ? `${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)}`
      : '245, 158, 11';
  } catch (error) {
    return '245, 158, 11'; // 转换失败时安全回退
  }
};

const themeRgb = computed(() => hexToRgb(props.themeColor));
const themeRgbaOverlay = computed(() => `rgba(${themeRgb.value}, 0.85)`);
const themeRgbaParticle = computed(() => `rgba(${themeRgb.value}, 0.7)`);
const themeRgbaShadow = computed(() => `rgba(${themeRgb.value}, 0.5)`);

const getParticleStyle = () => {
  const size = Math.random() * 3 + 2 + 'px';
  const left = Math.random() * 100 + '%';
  const top = Math.random() * 100 + '%';
  const duration = Math.random() * 12 + 8 + 's';
  const delay = Math.random() * -20 + 's'; 
  return { width: size, height: size, left, top, animationDuration: duration, animationDelay: delay };
};
</script>

<style scoped>
.theme-overlay {
  background-color: v-bind(themeRgbaOverlay);
  mix-blend-mode: color;
  pointer-events: none;
}

.particles {
  position: absolute;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.particle {
  position: absolute;
  background: v-bind(themeRgbaParticle);
  border-radius: 50%;
  box-shadow: 0 0 8px v-bind(themeRgbaShadow);
  animation: float-up linear infinite;
}

@keyframes float-up {
  0% { transform: translateY(0) scale(1); opacity: 0; }
  20% { opacity: 0.8; }
  80% { opacity: 0.8; }
  100% { transform: translateY(-70vh) scale(0.4); opacity: 0; }
}
</style>