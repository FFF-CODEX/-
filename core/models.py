from django.db import models


# 联系表单数据表
class Contract(models.Model):
    contact_name = models.CharField('联系人', max_length=100)
    contact_phone = models.CharField('联系人电话', max_length=30)
    company = models.CharField('公司/品牌', max_length=200, blank=True, default='')
    project_type = models.CharField('项目类型', max_length=50)
    quantity = models.CharField('预计数量', max_length=50)
    delivery_city = models.CharField('交付城市', max_length=100)
    budget = models.CharField('预算区间', max_length=50)
    requirement = models.TextField('需求说明')
    created_at = models.DateTimeField('提交时间', auto_now_add=True)

    class Meta:
        db_table = 'contract'
        verbose_name = '联络表单'
        verbose_name_plural = '联络表单'

    def __str__(self):
        return f'{self.contact_name} - {self.delivery_city}'
