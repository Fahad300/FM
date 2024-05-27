from django.shortcuts import render, get_object_or_404
from .models import Post

posts = Post.objects.all()

def blog(request):
    return render(request, "blog/blog.html", {
         "posts": posts
    })

def get_latest_items(model, date_field, limit=5):
    return model.objects.all().order_by(f'-{date_field}')[:limit]

def dynamic_post(request, slug):
      s_post = get_object_or_404(Post, slug=slug)
      latest_posts = get_latest_items(Post, 'date')
      return render(request, "blog/blog-detail.html" , {
         "post": s_post,
         "latest_post": latest_posts,
         "all_posts": posts
    })
