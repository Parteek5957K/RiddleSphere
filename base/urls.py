from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('#', views.logoutUser, name='signout'),

path('feedback/', views.feedback_view, name='feedback_view'),
]
