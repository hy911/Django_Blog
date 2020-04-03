from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    '''
    分类
    '''
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    '''
    文章
    '''
    # 标题
    title = models.TextField('标题', max_length=70)

    body = models.TextField('正文')
    # 文章创建时间和最后修改时间
    create_time = models.DateField('创建时间', default=timezone.now)
    modified_time = models.DateField('修改时间')

    # 文章摘要
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    # 类型关联,标题关联
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 作者
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
