from django.forms import ModelForm
from .models import User, Feedback, Room, Puzzle,RoomRole, RoomPublishDate
from django.contrib.auth.forms import UserCreationForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'url', 'theme', 'story', 'custom_intro']


class PuzzleForm(ModelForm):
    class Meta:
        model = Puzzle
        fields = ['puzzle_number', 'file']


class RoomRoleForm(ModelForm):
    class Meta:
        model = RoomRole
        fields = ['user', 'role']


class RoomPublishDateForm(ModelForm):
    class Meta:
        model = RoomPublishDate
        fields = ['publish_date']


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating']