from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post, Comment
from .forms import CommentForm


class BlogView(View):
    def get(self, request):
          posts = Post.objects.all().order_by("-date")
          return render(request, "blog/blog.html", {
               "posts": posts
          })

class Blog_detailsView(View):

     def get(self, request, slug):
          posts = Post.objects.all()
          post = get_object_or_404(posts, slug=slug)
          form = CommentForm()
          return render(request, "blog/blog-detail.html" , {
               "post": post,
               "latest_post": posts.order_by("-date")[:5],
               "all_posts": posts,
               "tags": post.tags.all(),
               "c_count":post.comments.count(),
               "comments": post.comments.order_by("-c_date"),
               "form": form
          })
     
     def post(self, request, slug):
          posts = Post.objects.all()
          post = get_object_or_404(posts, slug=slug)
          form = CommentForm(request.POST)

          if form.is_valid():
               new_comment = Comment(post=post,
                                     c_name = form.cleaned_data['name'],
                                     c_email = form.cleaned_data['email'],
                                     c_comment = form.cleaned_data['comment'])
               new_comment.save()
               form = CommentForm()
          
          return render(request, "blog/blog-detail.html" , {
               "post": post,
               "latest_post": posts.order_by("-date")[:5],
               "all_posts": posts,
               "tags": post.tags.all(),
               "c_count":post.comments.count(),
               "comments": post.comments.order_by("-c_date"),
               "form": form
          })
     

