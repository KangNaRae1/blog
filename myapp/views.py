from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

# Create your views here.
def home(request):
    blogs=Blog.objects
    blog_list=Blog.objects.all()
    paginator=Paginator(blog_list,3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs, 'posts':posts})

def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    blogs=Blog.objects
    return redirect('/')

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def edit(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request,'edit.html',{'blog':blog_detail})

def destroy(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    blog_detail.delete()
    return redirect('/')

def update(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    blog_detail.title=request.GET['blog_title']
    blog_detail.pub_date=timezone.datetime.now()
    blog_detail.body=request.GET['blog_body']
    blog_detail.save()
    return render(request,'detail.html',{'blog':blog_detail})

def blogpost(request):
    if request.method=='POST':
        form=BlogPost(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form=BlogPost()
        return render(request,'new.html',{'form':form})
