from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def bloglist(request):
    blogs = Blog.objects.all()
    return render(request, 'bloglist.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})