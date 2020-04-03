from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,'index.html',context={'post_list':post_list})