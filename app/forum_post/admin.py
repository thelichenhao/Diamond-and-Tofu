from django.contrib import admin
from .models import ForumPost, ForumComment, Topic
# Register your models here.

admin.site.register(ForumPost)
admin.site.register(ForumComment)
admin.site.register(Topic)
