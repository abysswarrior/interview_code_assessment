from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('score/<int:article_id>/', views.UserAddScoreView.as_view(), name='add-score'),
    path('articles/', views.ArticleListView.as_view(), name='article-list'),
]