<script setup>
import overviewImage from '../assets/images/shapan-model.jpg'
import structureImage from '../assets/images/tielu-qiaodun.jpg'
import valueImage from '../assets/images/bim-jianmo.jpg'
</script>

<template>
  <main>
    <section class="page-hero page-hero--short">
      <div class="container">
        <p class="section-kicker">产品中心</p>
        <h1>高铁缩微沙盘模型</h1>
        <p>以环形双线高架高速铁路场景为核心，完整呈现桥梁结构、轨道系统、接触网与动车组模型。</p>
      </div>
    </section>

    <nav class="category-nav">
      <div class="container category-nav__inner">
        <a href="#overview">沙盘概况</a>
        <a href="#structure">核心结构</a>
        <a href="#value">社团价值</a>
      </div>
    </nav>

    <section id="overview" class="band band--plain product-section">
      <div class="container product-row">
        <img :src="overviewImage" alt="沙盘整体概况" />
        <div class="product-row__body">
          <p class="section-kicker">01 / 沙盘整体概况</p>
          <h2>环形双线高架高速铁路场景</h2>
          <p>
            沙盘为环形双线高架高速铁路场景，按比例缩微复刻真实高铁线路工程，包含完整轨道系统、两种特色桥梁、CR400BF 复兴号动车组模型、接触网、路基绿化、配套场站，还原现代化高铁线路全貌。前期先用 BIM 软件完成三维建模，确定桥墩、梁体、线路曲线布局，再下料手工拼装、打磨上色，实现从图纸到实体模型的完整落地。
          </p>
          <ul class="spec-list">
            <li>场景：环形双线高架高速铁路</li>
            <li>桥型：三跨连续梁 + 三跨斜拉桥</li>
            <li>车辆：CR400BF 复兴号动车组</li>
            <li>制作：BIM 三维建模 + 手工拼装打磨上色</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="structure" class="band band--light product-section">
      <div class="container product-row product-row--reverse">
        <img :src="structureImage" alt="核心工程结构" />
        <div class="product-row__body">
          <p class="section-kicker">02 / 核心工程结构</p>
          <h2>连续梁、斜拉桥与电气化轨道</h2>
          <ul class="spec-list">
            <li>三跨连续梁：连续梁是高铁常用桥梁形式，多跨梁体连成整体，刚度大、沉降变形小，列车高速通过时平顺性好，适合无砟轨道高铁线路。模型里连续梁段搭配圆形实体桥墩，还原高架高铁大量采用的简支、连续梁高架结构。</li>
            <li>三跨斜拉桥：沙盘内设一座小型三跨斜拉桥，属于大跨度桥型。依靠桥塔、斜拉索拉住主梁，跨越能力强，展示高速铁路特殊大跨桥梁方案，和连续梁形成两种桥型对比，直观体现不同桥梁结构适用场景。</li>
            <li>轨道与接触网系统：铺设双线轨道，搭配仿真接触网（受电弓配套），配套 CR400BF 复兴号高铁模型，模拟动车组取电、在线路上运行的真实工况。</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="value" class="band band--plain product-section">
      <div class="container product-row">
        <img :src="valueImage" alt="模型制作与社团价值" />
        <div class="product-row__body">
          <p class="section-kicker">03 / 模型制作与社团价值</p>
          <h2>从课堂知识到社团成果</h2>
          <p>
            整个项目由社团成员分工完成：BIM 图纸设计、构件切割打磨、桥梁拼装、景观绿化、细节装饰。
          </p>
          <ul class="spec-list">
            <li>专业层面：把高铁施工、桥梁工程、线路勘测课堂知识落地，直观理解桥梁结构、高架线路、电气化铁路构造。</li>
            <li>社团实践：属于模型制作、手工实操、作品研讨、成果展览的核心项目，可用于校内成果展、学科竞赛、新生科普宣讲。</li>
            <li>延伸作品：社团同时制作校园建筑沙盘，除铁道工程类模型外，也开展建筑类缩微模型创作，拓展模型制作能力。</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container cta-band__inner">
        <div>
          <p class="section-kicker section-kicker--gold">定制咨询</p>
          <h2>把高铁工程做成可展示的模型</h2>
        </div>
        <RouterLink to="/contact" class="btn btn--solid">联系定制</RouterLink>
      </div>
    </section>
  </main>
</template>
