# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

class LoginView(View):
    template_name = 'login/login.html'
    
    def get(self, request):
        error_msg = ''
        return render(request, self.template_name, {'error_msg': error_msg})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # replace 'home' with the name of your home page
        else:
            error_msg = 'Invalid login credentials'
            return render(request, self.template_name, {'error_msg': error_msg})
