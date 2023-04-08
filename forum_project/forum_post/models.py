from django.db import models

# Create your models here.
# Class: ForumPost
class ForumPost(models.Model):
    # Fields
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Meta
    class Meta:
        ordering = ['-created_at']

    # Methods
    def __str__(self):
        return self.title
    