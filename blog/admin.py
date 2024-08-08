from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    search_fields = ['title', 'content']
    date_hierarchy = 'pub_date'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('post', 'author', 'created_at')
    search_fields = ['content']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
