from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('', PostListView.as_view(), name='post_list'),
]