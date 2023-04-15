
# from django.contrib import admin
# from django.urls import path, include
# from . import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('', include('forum_app.urls')),
# ]

from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]

app_name = 'forum_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('region/<str:region_name>/', views.region, name='region'),
    path('interest/<str:interest_name>/', views.interest, name='interest'),
]
