from django.shortcuts import render
from .models import ForumPost
from .forms import PostCreateForm
from django.views.generic import ListView, DetailView, CreateView

class PostListView(ListView):
    model = ForumPost
    template_name = 'forum_post/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Forum Posts'
        return context
    
    def get_queryset(self):
        return ForumPost.objects.all().order_by('-created_at')

# Create your views here.
class PostDetailView(DetailView):
    model = ForumPost
    template_name = 'forum_post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = ForumPost.objects.get(id=self.kwargs['post_id'])
        context.update({
            'title': post.title,
            'author': post.author,
            'body': post.body,
        })
        return context
    
class PostCreateView(CreateView):
    model = ForumPost

    template_name = 'forum_post/post_create.html'
    fields = ['title', 'author', 'body']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create a Forum Post'
        return context