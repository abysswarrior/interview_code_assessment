from django.contrib import admin
from .models import Article, Score


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Your Article admin configuration goes here
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    # Your Score admin configuration goes here
    pass
