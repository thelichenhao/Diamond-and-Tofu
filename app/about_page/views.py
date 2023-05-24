from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def about_page(request):
  template = loader.get_template('about_page.html')
  return HttpResponse(template.render({}, request)) 