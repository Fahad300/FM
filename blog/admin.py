from django.contrib import admin
from .models import Post, Author, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tags')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('c_name', 'c_email', 'c_comment', 'c_date')
    list_filter = ('c_name',)

admin.site.register(Author)
admin.site.register(Tag)