from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import default_storage
from .forms import RegistrationForm, RoomForm, PuzzleForm, RoomRoleForm, RoomPublishDateForm
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    if 'signup' in request.POST:
        registerProfile(request)
    if 'login' in request.POST:
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

def userProfile(request):
    context={}
    return render(request, 'user-profile.html', context)

def logoutUser(request):
    if 'signup' in request.POST:
        registerProfile(request)
    logout(request)
    return redirect('home')


def registerProfile(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {}
    return render(request, 'home.html', context)

class CreateRoomWizard(SessionWizardView):
    template_name = 'room-create.html'
    form_list = [RoomForm, PuzzleForm, RoomRoleForm, RoomPublishDateForm]
    file_storage = default_storage

    def done(self, form_list, form_dict, **kwargs):
        room = form_dict['0'].save()

        for i in range(1, 4):
            form = form_dict[str(i)]
            if i == 1:
                for file_form in form:
                    puzzle = file_form.save(commit=False)
                    puzzle.room = room
                    puzzle.save()
            elif i == 2:
                for user_form in form:
                    role = user_form.save(commit=False)
                    role.room = room
                    role.save()
            elif i == 3:
                publish_date = form.save(commit=False)
                publish_date.room = room
                publish_date.save()

        return redirect('home')

'''
from django.contrib.auth.decorators import user_passes_test
def is_admin(user):
    return user.is_authenticated and user.is_staff
@user_passes_test(is_admin)
def admin_only_view(request):
    ...
'''

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
