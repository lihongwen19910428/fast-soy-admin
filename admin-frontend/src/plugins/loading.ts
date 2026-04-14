// @unocss-include
import { getColorPalette, getRgb } from '@sa/color';
import { DARK_CLASS } from '@/constants/app';
import { localStg } from '@/utils/storage';
import { toggleHtmlClass } from '@/utils/common';
import { $t } from '@/locales';

export function setupLoading() {
  const themeColor = localStg.get('themeColor') || '#646cff';
  const darkMode = localStg.get('darkMode') || false;
  const palette = getColorPalette(themeColor);

  const { r, g, b } = getRgb(themeColor);

  const primaryColor = `--primary-color: ${r} ${g} ${b}`;

  const svgCssVars = Array.from(palette.entries())
    .map(([key, value]) => `--logo-color-${key}: ${value}`)
    .join(';');

  const cssVars = `${primaryColor}; ${svgCssVars}`;

  if (darkMode) {
    toggleHtmlClass(DARK_CLASS).add();
  }

  const loadingClasses = [
    'left-0 top-0',
    'left-0 bottom-0 animate-delay-500',
    'right-0 top-0 animate-delay-1000',
    'right-0 bottom-0 animate-delay-1500'
  ];

  const dot = loadingClasses
    .map(item => {
      return `<div class="absolute w-16px h-16px bg-primary rounded-8px animate-pulse ${item}"></div>`;
    })
    .join('\n');

  const loading = `
<div class="fixed-center flex-col bg-layout" style="${cssVars}">
  <div class="w-128px h-128px">
    ${getLogoSvg()}
  </div>
  <div class="w-56px h-56px my-36px">
    <div class="relative h-full animate-spin">
      ${dot}
    </div>
  </div>
  <h2 class="text-28px font-500 text-primary">${$t('system.title')}</h2>
</div>`;

  const app = document.getElementById('app');

  if (app) {
    app.innerHTML = loading;
  }
}

function getLogoSvg() {
  const logoSvg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 85" fill="none" width="100%" height="100%">
    <path d="M20,40 Q50,-5 80,40" stroke="url(#sun-gradient)" stroke-width="8" stroke-linecap="round" fill="none" />
    <path d="M30,40 Q50,10 70,40" stroke="url(#sun-gradient)" stroke-width="6" stroke-linecap="round" fill="none" />
    <path d="M40,40 Q50,22 60,40" stroke="url(#sun-gradient)" stroke-width="4" stroke-linecap="round" fill="none" />
    
    <text x="50" y="76" font-family="Arial, sans-serif" font-size="34" font-weight="900" fill="url(#sun-gradient)" text-anchor="middle" letter-spacing="4">SUN</text>
    
    <defs>
      <linearGradient id="sun-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#FF8C00" />
        <stop offset="100%" style="stop-color:#FFD700" />
      </linearGradient>
    </defs>
  </svg>`;

  return logoSvg;
}
