from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
    blog = Blog.objects.order_by('-published')[:3]
    count =Blog.objects.count()

    return render(request, 'blog/blog.html', {'blogs': blog})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})