from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from forum_login.models import CustomUser

# Content of post/comment

class Content(models.Model):
    title = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    votes = models.IntegerField(default=0)
    unvotes = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    
# Class of topic
class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
# Create your models here.
# Class: ForumPost
class ForumPost(Content):
    # Fields
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    # Meta
    class Meta:
        ordering = ['-created_at']

    # Methods
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    

# Class: Comment
class ForumComment(Content):
    # Fields
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    # Meta
    class Meta:
        ordering = ['-created_at']

    # Methods
    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])
