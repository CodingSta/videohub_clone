from django.contrib import admin
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_length')

    def content_length(self, post):
        return '{} 글자'.format(len(post.content))


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

