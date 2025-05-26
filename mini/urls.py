from django.urls import path
from mini.views import home, about, post_detail, posts_by_author, posts_by_category, posts_by_tag

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('author/<int:author_id>/', posts_by_author, name='posts_by_author'),
    path('category/<slug:category_slug>/', posts_by_category, name='posts_by_category'),
    path('tag/<slug:tag_slug>/', posts_by_tag, name='posts_by_tag'),
]