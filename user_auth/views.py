from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.views import LoginView

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

# Function-based views
def user_login(request):
    return render(request, 'registration/login.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password'})
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, 'registration/login.html')

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password,
    })

# user_auth/views.py
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "authentication/signup.html"

def homeLogin(request):
    return render(request, 'polls/home.html')
