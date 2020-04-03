from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    '''
    分类
    '''
    name = models.CharField(max_length=100)

class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length=100)

class Post(models.Model):
    '''
    文章
    '''
    #标题
    title = models.TextField()

    body = models.TextField()
    #文章创建时间和最后修改时间
    create_time = models.DateField()
    modified_time = models.DateField()

    #文章摘要
    excerpt = models.CharField(max_length=200,blank=True)

    #类型关联,标题关联
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    #作者
    author = models.ForeignKey(User,on_delete=models.CASCADE)