from django.urls import path
from . import views

urlpatterns = [
    # ...existing code...
    path('blog/', views.BlogListView.as_view(), name='blog-list'),
    # ...existing code...
]