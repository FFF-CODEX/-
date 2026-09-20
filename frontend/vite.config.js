import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  // 构建产物由 Django 托管，静态资源统一走 /static/
  base: '/static/',
  plugins: [vue()],
  server: {
    host: '127.0.0.1',
    port: 5173,
    // 开发环境下将 /api 请求代理到 Django 后端
    proxy: {
      '/api': 'http://127.0.0.1:8000',
    },
  },
})
