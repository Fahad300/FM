from django.contrib import admin
from .models import Post, Author, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tags')

admin.site.register(Author)
admin.site.register(Tag)