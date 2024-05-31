from django.shortcuts import render, get_object_or_404
from .models import Post


def blog(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/blog.html", {
         "posts": posts
    })

def dynamic_post(request, slug):
      posts = Post.objects.all()
      post = get_object_or_404(posts, slug=slug)
      latest_posts = posts.order_by("-date")[:5]
      return render(request, "blog/blog-detail.html" , {
         "post": post,
         "latest_post": latest_posts,
         "all_posts": posts,
         "tags": post.tags.all()
    })
