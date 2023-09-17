from django.forms import ModelForm
from .models import User,Feedback

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username', 'email']


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating']