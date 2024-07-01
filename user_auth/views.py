from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.views import LoginView

# Function-based views
def user_login(request):
    """
    Render the login page.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        The rendered login page.
    """
    return render(request, 'registration/login.html')

def authenticate_user(request):
    """
    Authenticate and login the user.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        Redirects to the index page if authentication is successful,
        otherwise re-renders the login page with an error message.
    """
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
    """
    Display the authenticated user's information.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        The rendered user information page.
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password,
    })

# user_auth/views.py

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "authentication/signup.html"

def homeLogin(request):
    """
    Render the home page after login.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        The rendered home page.
    """
    return render(request, 'polls/home.html')
