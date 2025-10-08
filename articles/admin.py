from django.contrib import admin

from .models import Articles

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'body',
        'author',
    ]

admin.site.register(Articles, ArticleAdmin)