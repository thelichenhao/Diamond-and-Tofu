from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView

app_name = 'forum_post'

urlpatterns = [
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('', PostListView.as_view(), name='post_list'),
]
