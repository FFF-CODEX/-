<script setup>
import { Hammer, Paintbrush, Trees, Cog, Building2, MapPin, FileText, PackageCheck } from '@lucide/vue'

import heroImage from '../assets/images/gaotie-model.jpg'
import storyImage from '../assets/images/tuantizhao.jpg'
import coreOne from '../assets/images/shapan-model.jpg'
import coreTwo from '../assets/images/tielu-qiaodun.jpg'
import coreThree from '../assets/images/bim-jianmo.jpg'
</script>

<template>
  <main>
    <section class="hero">
      <img class="hero__image" :src="heroImage" alt="微缩模型工坊工作台" />
      <div class="hero__content">
        <p class="hero__eyebrow">手工微缩模型定制工厂</p>
        <h1>微筑工坊</h1>
        <p class="hero__lead">
          以匠人之手，还原建筑、机械与时代的真实肌理。每一件模型都从图纸开始，经由雕刻、涂装与组装，成为可收藏的微缩世界。
        </p>
        <div class="hero__actions">
          <RouterLink to="/contact" class="btn btn--solid">定制咨询</RouterLink>
          <RouterLink to="/products" class="btn btn--ghost">浏览作品</RouterLink>
        </div>
      </div>
    </section>

    <section class="band band--light">
      <div class="container">
        <dl class="stats stats--wide">
          <div class="stats__item">
            <dt>20+</dt>
            <dd>年工艺沉淀</dd>
          </div>
          <div class="stats__item">
            <dt>1200+</dt>
            <dd>件定制交付</dd>
          </div>
          <div class="stats__item">
            <dt>800㎡</dt>
            <dd>自有车间面积</dd>
          </div>
          <div class="stats__item">
            <dt>26人</dt>
            <dd>工艺与制作团队</dd>
          </div>
        </dl>
      </div>
    </section>

    <section class="band band--plain">
      <div class="container">
        <div class="split-row">
          <div class="split-row__image">
            <img :src="storyImage" alt="团队合照" />
          </div>
          <div class="split-row__body">
            <p class="section-kicker">关于微筑</p>
            <h2>团队介绍</h2>
            <p>
              本项目团队由院校领导、专业教师与学生骨干共同组成，分工明确、协同推进，保障沙盘模型项目有序落地实施。
            </p>
            <p>
              项目领导小组由胡海东院长、章韵主任、杨志鹏辅导员组成，统筹项目整体规划，引领团队开展项目实施，协调各项资源，把控项目整体方向。
            </p>
            <p>
              专业教学组由李骏、杨凯、程光威、何勇老师构成，负责模型相关专业理论与制作知识授课指导；杨福瑞老师承担 BIM 三维建模技术教学工作，完成前期数字化方案设计指导；刘占新老师负责项目全过程的安全管理与安全教育，规范现场操作，防范制作风险。
            </p>
            <p>
              技术实操组中，张亚、田正华、刘海湾负责模型的测量、放线与定位工作，保障模型构件尺寸精度；学生核心制作团队由李明松、邰昌力、曾博以及梦想家全体学生组成，承担模型构件加工、拼装、景观布设等实体搭建任务，落实模型制作各项实操工作。
            </p>
            <p>
              全体成员各司其职、紧密配合，依托专业理论与实操实践，完成高速铁路沙盘等系列缩微模型的设计与制作。
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="band band--light">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">服务领域</p>
          <h2>服务多元场景的模型定制</h2>
        </div>
        <div class="service-grid">
          <article>
            <Building2 :size="26" :stroke-width="1.5" />
            <h3>城市展陈</h3>
            <p>规划馆、产业馆与城市更新项目的建筑与规划模型。</p>
          </article>
          <article>
            <MapPin :size="26" :stroke-width="1.5" />
            <h3>文化场馆</h3>
            <p>博物馆、历史遗址与教育空间的教学与展陈模型。</p>
          </article>
          <article>
            <Cog :size="26" :stroke-width="1.5" />
            <h3>工业演示</h3>
            <p>设备结构、工艺流程与产品打样的演示原型。</p>
          </article>
          <article>
            <FileText :size="26" :stroke-width="1.5" />
            <h3>品牌商业</h3>
            <p>品牌活动、商业空间与地产项目的主题场景模型。</p>
          </article>
        </div>
      </div>
    </section>

    <section class="band band--plain">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">产品方向</p>
          <h2>三类核心产品</h2>
        </div>
        <div class="work-grid">
          <article class="work-card">
            <img :src="coreOne" alt="沙盘整体概况" />
            <div class="work-card__body">
              <h3>沙盘整体概况</h3>
              <p>沙盘为环形双线高架高速铁路场景，按比例缩微复刻真实高铁线路工程，包含完整轨道系统、两种特色桥梁、CR400BF 复兴号动车组模型、接触网、路基绿化与配套场站。前期先用 BIM 软件完成三维建模，再下料手工拼装、打磨上色，实现从图纸到实体模型的完整落地。</p>
              <RouterLink to="/products" class="text-link">查看详情</RouterLink>
            </div>
          </article>
          <article class="work-card">
            <img :src="coreTwo" alt="核心工程结构" />
            <div class="work-card__body">
              <h3>核心工程结构</h3>
              <ul class="work-card__list">
                <li>三跨连续梁：多跨梁体连成整体，刚度大、沉降变形小，列车高速通过平顺，适合无砟轨道高架线路。</li>
                <li>三跨斜拉桥：依靠桥塔、斜拉索拉住主梁，跨越能力强，与连续梁形成两种桥型对比。</li>
                <li>轨道与接触网：铺设双线轨道与仿真接触网，配套 CR400BF 复兴号模型，模拟取电与运行工况。</li>
              </ul>
              <RouterLink to="/products" class="text-link">查看详情</RouterLink>
            </div>
          </article>
          <article class="work-card">
            <img :src="coreThree" alt="模型制作与社团价值" />
            <div class="work-card__body">
              <h3>模型制作与社团价值</h3>
              <ul class="work-card__list">
                <li>专业层面：把高铁施工、桥梁工程、线路勘测等课堂知识落地，直观理解桥梁与电气化铁路构造。</li>
                <li>社团实践：作为模型制作、手工实操、作品研讨与成果展览的核心项目，用于成果展、竞赛与科普宣讲。</li>
                <li>延伸作品：同步制作校园建筑沙盘，拓展建筑类缩微模型创作能力。</li>
              </ul>
              <RouterLink to="/products" class="text-link">查看详情</RouterLink>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="band band--light">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">工艺特色</p>
          <h2>四道核心工序，支撑每一件作品</h2>
        </div>
        <div class="feature-grid">
          <article class="feature-item">
            <Hammer :size="26" :stroke-width="1.5" />
            <h3>手工雕刻</h3>
            <p>从板材到构件，以刻刀与微型工具完成精细加工。</p>
          </article>
          <article class="feature-item">
            <Paintbrush :size="26" :stroke-width="1.5" />
            <h3>微缩涂装</h3>
            <p>多层喷涂与旧化处理，还原真实材质与使用痕迹。</p>
          </article>
          <article class="feature-item">
            <Trees :size="26" :stroke-width="1.5" />
            <h3>场景营造</h3>
            <p>植被、地面与光影布置，让模型拥有完整的环境叙事。</p>
          </article>
          <article class="feature-item">
            <PackageCheck :size="26" :stroke-width="1.5" />
            <h3>精密装配</h3>
            <p>模块化结构设计，保证运输安全与长期陈列稳定。</p>
          </article>
        </div>
      </div>
    </section>

    <section class="band band--plain">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">制作流程</p>
          <h2>从需求沟通到交付维护</h2>
        </div>
        <ol class="process-list process-list--compact">
          <li>
            <span class="process-list__num">01</span>
            <div>
              <h3>需求沟通</h3>
              <p>确认用途、尺寸、比例与预算范围。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">02</span>
            <div>
              <h3>方案确认</h3>
              <p>完成图纸深化与结构拆分，确认制作方案。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">03</span>
            <div>
              <h3>打样制作</h3>
              <p>完成关键部件打样，验证工艺与细节标准。</p>
            </div>
          </li>
          <li>
            <span class="process-list__num">04</span>
            <div>
              <h3>质检交付</h3>
              <p>逐项质检、包装交付，并提供安装维护支持。</p>
            </div>
          </li>
        </ol>
      </div>
    </section>

    <section class="band band--plain">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">常见问题</p>
          <h2>定制前需要了解什么</h2>
        </div>
        <div class="qa-list">
          <article>
            <h3>定制需要提供哪些资料？</h3>
            <p>图纸、照片、尺寸或参考案例均可。资料越完整，报价与周期越准确。</p>
          </article>
          <article>
            <h3>最小起订量与周期是多少？</h3>
            <p>单件起订，常规周期为 10 至 70 个工作日，复杂项目可在方案阶段确认排期。</p>
          </article>
          <article>
            <h3>作品如何运输与安装？</h3>
            <p>按项目定制防震包装，必要时提供现场安装与长期维护支持。</p>
          </article>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container cta-band__inner">
        <div>
          <p class="section-kicker section-kicker--gold">开始定制</p>
          <h2>从一张图纸，到一座微缩世界</h2>
        </div>
        <RouterLink to="/contact" class="btn btn--solid">预约沟通</RouterLink>
      </div>
    </section>
  </main>
</template>
