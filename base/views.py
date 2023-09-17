from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from .forms import FeedbackForm


# Create your views here.

def home(request):
    loginprofile(request)
    context = {}
    return render(request, 'home.html', context)


def loginprofile(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=username, password=password)


        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {}
    return render(request, 'home.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def feedback_view(request):
    pass
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('thank_you_page')  # Redirect to a thank you page or any other page
#     else:
#         form = FeedbackForm()
#
#     return render(request, 'feedback.html', {'form': form})
