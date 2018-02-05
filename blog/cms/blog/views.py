from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def list_of_post(request):
    post = Post.objects.all()
    return render(request, 'blog/post/list_of_post.html', {'post':post})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post/post_detail.html', {'post':post})