<script setup>
import { Cpu, Scissors, SprayCan, Hand, ShieldCheck, Recycle, BadgeCheck } from '@lucide/vue'

import modelingOfficeImage from '../assets/images/jianmo-office.jpg'
import modelOfficeImage from '../assets/images/moxing-office.jpg'
</script>

<template>
  <main>
    <section class="page-hero page-hero--short">
      <div class="container">
        <p class="section-kicker">工厂与工艺</p>
        <h1>一间完整的微缩模型工坊</h1>
        <p>从木作车间到涂装工位，全部工序在自有厂房内完成，确保品质、进度与交付可控。</p>
      </div>
    </section>

    <section class="band band--plain factory-overview-band">
      <div class="container factory-overview">
        <div class="factory-overview__image">
          <figure>
            <img :src="modelingOfficeImage" alt="建模办公室" />
            <figcaption>建模办公室</figcaption>
          </figure>
          <figure>
            <img :src="modelOfficeImage" alt="模型办公室" />
            <figcaption>模型办公室</figcaption>
          </figure>
        </div>
        <div class="factory-overview__body">
          <p class="section-kicker">工厂概览</p>
          <h2>传统手艺与精密设备并行</h2>
          <p>
            工坊拥有完整木作、金工、涂装与装配车间。匠人负责雕刻、做旧与装配，数控设备完成板材切割与结构打样，二者配合保证复杂作品的稳定交付。
          </p>
          <dl class="factory-stats">
            <div>
              <dt>800㎡</dt>
              <dd>自有车间面积</dd>
            </div>
            <div>
              <dt>26人</dt>
              <dd>工艺与制作团队</dd>
            </div>
            <div>
              <dt>8道</dt>
              <dd>标准质检工序</dd>
            </div>
          </dl>
        </div>
      </div>
    </section>

    <section class="band band--light">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">车间分区</p>
          <h2>四个专业车间协同制作</h2>
        </div>
        <div class="zone-grid">
          <article>
            <span class="zone-grid__num">01</span>
            <h3>木作车间</h3>
            <p>板材切割、铣形、雕刻与木构组装，完成主体结构。</p>
          </article>
          <article>
            <span class="zone-grid__num">02</span>
            <h3>金工车间</h3>
            <p>金属蚀刻、折弯、焊接与传动机构制作。</p>
          </article>
          <article>
            <span class="zone-grid__num">03</span>
            <h3>涂装车间</h3>
            <p>底漆、面漆、旧化与色板管理，保证色彩统一。</p>
          </article>
          <article>
            <span class="zone-grid__num">04</span>
            <h3>装配车间</h3>
            <p>场景布置、灯光安装与成品总装，完成最终质检。</p>
          </article>
        </div>
      </div>
    </section>

    <section class="band band--plain">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">设备能力</p>
          <h2>支撑精度的核心设备</h2>
        </div>
        <table class="param-table">
          <thead>
            <tr>
              <th>设备</th>
              <th>用途</th>
              <th>能力说明</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>数控精雕机</td>
              <td>板材切割与铣形</td>
              <td>保证构件尺寸统一，适配批量部件</td>
            </tr>
            <tr>
              <td>激光切割机</td>
              <td>复杂轮廓与蚀刻</td>
              <td>细密装饰构件与金属蚀刻片制作</td>
            </tr>
            <tr>
              <td>精密喷笔系统</td>
              <td>多层涂装与旧化</td>
              <td>渐变、做旧与材质纹理表现</td>
            </tr>
            <tr>
              <td>微型机床</td>
              <td>金属与木质车削</td>
              <td>传动轴、法兰、管件等圆形构件</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <section class="band band--light">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">制作流程</p>
          <h2>八道工序，逐项确认</h2>
        </div>
        <ol class="process-list">
          <li>
            <span class="process-list__num">01</span>
            <div>
              <h3>需求评估</h3>
              <p>确认用途、尺寸、比例与预算范围。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">02</span>
            <div>
              <h3>图纸深化</h3>
              <p>整理建筑或机械图纸，拆分结构与部件。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">03</span>
            <div>
              <h3>结构打样</h3>
              <p>完成主体骨架与关键部件的小样验证。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">04</span>
            <div>
              <h3>精细雕刻</h3>
              <p>手工完成立面、构件与细节雕刻。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">05</span>
            <div>
              <h3>涂装做旧</h3>
              <p>分层喷涂、旧化与色彩校准。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">06</span>
            <div>
              <h3>场景组装</h3>
              <p>布置地面、植被、灯光与环境元素。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">07</span>
            <div>
              <h3>质检校对</h3>
              <p>对照图纸逐项检查比例、细节与牢固度。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">08</span>
            <div>
              <h3>定制包装</h3>
              <p>防震包装与安装说明随作品一同交付。</p>
            </div>
          </li>
        </ol>
      </div>
    </section>

    <section class="band band--plain">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">质量与责任</p>
          <h2>交付之外，还有长期支持</h2>
        </div>
        <div class="feature-grid">
          <article class="feature-item">
            <ShieldCheck :size="26" :stroke-width="1.5" />
            <h3>三重复检</h3>
            <p>部件、成品与包装三个阶段分别质检。</p>
          </article>
          <article class="feature-item">
            <BadgeCheck :size="26" :stroke-width="1.5" />
            <h3>工艺档案</h3>
            <p>重要项目留存图纸、色板与制作记录。</p>
          </article>
          <article class="feature-item">
            <Recycle :size="26" :stroke-width="1.5" />
            <h3>环保工艺</h3>
            <p>使用低气味涂料，废料分类回收处理。</p>
          </article>
          <article class="feature-item">
            <Hand :size="26" :stroke-width="1.5" />
            <h3>售后维护</h3>
            <p>提供运输加固、现场安装与返修支持。</p>
          </article>
        </div>
      </div>
    </section>

    <section class="band band--light">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">车间安全</p>
          <h2>规范生产，安全第一</h2>
        </div>
        <div class="notice-list">
          <p>粉尘与废气处理系统覆盖木作与涂装车间，作业区域定期检测。</p>
          <p>设备操作执行岗位培训与每日点检，工具与化学品分区管理。</p>
          <p>车间实行 6S 现场管理，物料、半成品与成品流转路径清晰。</p>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container cta-band__inner">
        <div>
          <p class="section-kicker section-kicker--gold">品质承诺</p>
          <h2>作品交付前，至少经过三重复检</h2>
        </div>
        <RouterLink to="/contact" class="btn btn--solid">联系工厂</RouterLink>
      </div>
    </section>
  </main>
</template>
