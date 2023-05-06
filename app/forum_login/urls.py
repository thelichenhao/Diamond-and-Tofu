# urls.py
from django.urls import path
from .views import LoginView, RegisterView, LogoutView

app_name = 'forum_login'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
