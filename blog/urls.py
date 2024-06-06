from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogView.as_view(), name="blog-home"),
    path("<slug:slug>", views.Blog_detailsView.as_view(), name="dynamic-post"),
]