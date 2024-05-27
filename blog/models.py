from django.db import models
from datetime import date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    excerpt = models.TextField()
    author = models.CharField(max_length=255)
    date = models.DateField()
    content = models.TextField()  # Store sections as HTML content
    quote = models.TextField(blank=True, null=True)
    quoter = models.CharField(max_length=255, blank=True, null=True)
    conclusion = models.TextField()
    call_to_action = models.TextField()

    def __str__(self):
        return self.title
    
