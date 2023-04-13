# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from .models import Thread

# def home(request):
#     threads = Thread.objects.all().order_by('-created_at')
#     return render(request, 'forum_app/home.html', {'threads': threads})

from django.shortcuts import render
from .models import Thread

# def home(request):
#     popular_threads = Thread.objects.order_by('-created_at')[:5]  # Fetch 5 most recent threads as popular posts
#     regions = Thread.objects.values_list('region', flat=True).distinct()  # Fetch distinct regions
#     interests = ['NFT', 'Anime', 'Technology', 'Beauty', 'Study']  # List of interests

#     context = {
#         'popular_threads': popular_threads,
#         'regions': regions,
#         'interests': interests,
#     }
    
#     return render(request, 'forum_app/home.html', context)

# forum_app/views.py

def home(request):
    threads = Thread.objects.all()
    regions = ['Massachusetts', 'New York State']  # Add your list of regions here
    interests = ['NFT', 'Anime', 'Technology', 'Beauty', 'Study']  # Add your list of interests here
    return render(request, 'forum_app/home.html', {'threads': threads, 'regions': regions, 'interests': interests})


# forum_app/views.py

def region(request, region_name):
    threads = Thread.objects.filter(region=region_name)
    return render(request, 'forum_app/region.html', {'threads': threads, 'region_name': region_name})

def interest(request, interest_name):
    threads = Thread.objects.filter(interest=interest_name)
    return render(request, 'forum_app/interest.html', {'threads': threads, 'interest_name': interest_name})
