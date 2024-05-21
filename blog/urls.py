from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name="blog-home"),
    path("<slug:slug>", views.dynamic_post, name="dynamic-post"),
]