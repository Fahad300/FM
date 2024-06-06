from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, null=True)
    c_name = models.CharField(max_length=100)
    c_email = models.EmailField(max_length=50)
    c_comment = models.TextField()
    c_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.c_name

class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField(max_length=255)
    slug = models.SlugField(default="", null=False, unique=True)
    image = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete= models.SET_NULL, related_name="posts", null=True)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("dynamic-post", args=[self.slug])
    
    
