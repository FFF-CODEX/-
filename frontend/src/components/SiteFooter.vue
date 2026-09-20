<script setup>
import logoUrl from '../assets/brand/logo.svg'
</script>

<template>
  <footer class="site-footer">
    <div class="site-footer__inner">
      <div class="site-footer__brand">
        <img class="site-footer__logo" :src="logoUrl" alt="微筑工坊" />
        <span class="site-footer__slogan">手工微缩模型定制工厂</span>
      </div>
      <nav class="site-footer__nav">
        <RouterLink to="/">首页</RouterLink>
        <RouterLink to="/products">产品</RouterLink>
        <RouterLink to="/factory">工厂</RouterLink>
        <RouterLink to="/contact">联系</RouterLink>
      </nav>
      <div class="site-footer__meta">
        <p>© 2026 微筑工坊 · 保留所有权利</p>
        <p>页面图片素材遵循开放许可，来源：Wikimedia Commons、Flickr / Openverse</p>
      </div>
    </div>
  </footer>
</template>
