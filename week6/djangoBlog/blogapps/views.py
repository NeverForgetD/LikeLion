from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs' : blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.contents = request.POST['contents']
    new_blog.playtime = request.POST['playtime']
    new_blog.updated_at = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def home(request):
    return render(request, 'index.html')