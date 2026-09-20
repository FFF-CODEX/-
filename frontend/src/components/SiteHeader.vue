<script setup>
import logoBadgeUrl from '../assets/brand/logo-badge.svg'
</script>

<template>
  <header class="site-header">
    <div class="site-header__inner">
      <RouterLink to="/" class="site-header__brand">
        <img class="site-header__logo" :src="logoBadgeUrl" alt="微筑工坊标识" />
        <span class="site-header__name">微筑工坊</span>
      </RouterLink>
      <nav class="site-nav">
        <RouterLink to="/" class="site-nav__link">首页</RouterLink>
        <RouterLink to="/products" class="site-nav__link">产品</RouterLink>
        <RouterLink to="/factory" class="site-nav__link">工厂</RouterLink>
        <RouterLink to="/contact" class="site-nav__link">联系</RouterLink>
      </nav>
    </div>
  </header>
</template>
