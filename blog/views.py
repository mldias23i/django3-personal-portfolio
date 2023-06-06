from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # Get the total count of blogs
    blog_count = Blog.objects.count
    # Retrieve the latest 5 blogs
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs, 'blog_count': blog_count})

def detail(request, blog_id):
    # Get the blog with the specified ID or show a 404 error
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})