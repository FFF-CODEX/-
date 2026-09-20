<script setup>
import { ref } from 'vue'
import { MapPin, Phone, Mail, Clock, CalendarCheck } from '@lucide/vue'

import contactImage from '../assets/images/workshop-cc0.jpg'

const submitted = ref('')

async function handleSubmit(event) {
  event.preventDefault()
  const form = event.target
  const formData = new FormData(form)
  const payload = {
    contact_name: formData.get('contactName'),
    contact_phone: formData.get('phone'),
    company: formData.get('company') || '',
    project_type: formData.get('projectType'),
    quantity: formData.get('quantity'),
    delivery_city: formData.get('city'),
    budget: formData.get('budget'),
    requirement: formData.get('message'),
  }

  try {
    const response = await fetch('/api/contract/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
    if (response.ok) {
      submitted.value = '咨询已提交，我们将在 1 个工作日内与您联系。'
      form.reset()
    } else {
      submitted.value = '提交失败，请检查必填信息后重试。'
    }
  } catch (error) {
    submitted.value = '网络异常，提交失败，请稍后再试。'
  }
}
</script>

<template>
  <main>
    <section class="page-hero page-hero--short">
      <div class="container">
        <p class="section-kicker">联系我们</p>
        <h1>与微筑工坊建立联系</h1>
        <p>定制咨询、商务合作或到访参观，欢迎通过以下方式与我们沟通。</p>
      </div>
    </section>

    <section class="band band--plain">
      <div class="container contact-layout">
        <div class="contact-info">
          <p class="section-kicker">联系方式</p>
          <h2>欢迎预约沟通</h2>
          <dl>
            <div>
              <MapPin :size="22" :stroke-width="1.5" />
              <dt>工坊地址</dt>
              <dd>上海市 · 闵行区 · 微筑路 88 号（示例地址）</dd>
            </div>
            <div>
              <Phone :size="22" :stroke-width="1.5" />
              <dt>联系电话</dt>
              <dd>021-0000-0000（示例号码）</dd>
            </div>
            <div>
              <Mail :size="22" :stroke-width="1.5" />
              <dt>电子邮箱</dt>
              <dd>service@weizhu-models.example</dd>
            </div>
            <div>
              <Clock :size="22" :stroke-width="1.5" />
              <dt>工作时间</dt>
              <dd>周一至周六 09:00 - 18:00</dd>
            </div>
            <div>
              <CalendarCheck :size="22" :stroke-width="1.5" />
              <dt>到访预约</dt>
              <dd>建议提前两个工作日预约，可安排车间参观</dd>
            </div>
          </dl>
        </div>

        <form class="contact-form contact-form--wide" @submit="handleSubmit">
          <h3>项目咨询表单</h3>
          <p class="contact-form__hint">请完整填写以下信息，方便我们准确评估方案与报价。</p>
          <div class="contact-form__grid">
            <label>
              <span>联系人</span>
              <input type="text" name="contactName" placeholder="您的姓名" required />
            </label>
            <label>
              <span>联系电话</span>
              <input type="tel" name="phone" placeholder="手机或座机" required />
            </label>
            <label>
              <span>公司 / 品牌</span>
              <input type="text" name="company" placeholder="公司或品牌名称" />
            </label>
            <label>
              <span>项目类型</span>
              <select name="projectType" required>
                <option value="">请选择</option>
                <option>建筑模型</option>
                <option>机械模型</option>
                <option>场景模型</option>
                <option>比例原型</option>
                <option>其他</option>
              </select>
            </label>
            <label>
              <span>预计数量</span>
              <input type="text" name="quantity" placeholder="例如：1 件 / 3 件" required />
            </label>
            <label>
              <span>交付城市</span>
              <input type="text" name="city" placeholder="例如：上海" required />
            </label>
            <label>
              <span>预算区间</span>
              <select name="budget" required>
                <option value="">请选择</option>
                <option>5 万元以下</option>
                <option>5 - 10 万元</option>
                <option>10 - 30 万元</option>
                <option>30 万元以上</option>
              </select>
            </label>
            <label>
              <span>需求说明</span>
              <textarea name="message" rows="5" placeholder="用途、尺寸、比例、参考资料、期望周期等" required></textarea>
            </label>
          </div>
          <button type="submit" class="btn btn--solid btn--block">提交咨询</button>
          <p v-if="submitted" class="contact-form__notice">{{ submitted }}</p>
        </form>
      </div>
    </section>

    <section class="band band--light">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">常见问题</p>
          <h2>联系前可以先了解</h2>
        </div>
        <div class="qa-list">
          <article>
            <h3>咨询后多久会收到回复？</h3>
            <p>工作日提交的咨询一般在 24 小时内回复，复杂项目会先电话沟通。</p>
          </article>
          <article>
            <h3>外地项目如何合作？</h3>
            <p>方案沟通、进度确认与验收均可线上完成，成品通过定制包装与物流交付。</p>
          </article>
          <article>
            <h3>可以提供保密协议吗？</h3>
            <p>可以，涉及知识产权或未公开方案的项目可签署保密协议。</p>
          </article>
        </div>
      </div>
    </section>

    <section class="contact-visit">
      <img :src="contactImage" alt="微缩模型工坊车间" />
      <div class="contact-visit__overlay">
        <div class="container">
          <p class="section-kicker section-kicker--gold">到访参观</p>
          <h2>预约后可参观车间与作品陈列</h2>
          <p>参观名额有限，建议提前两个工作日预约。到访可携带图纸或参考图片，现场沟通更高效。</p>
        </div>
      </div>
    </section>
  </main>
</template>
