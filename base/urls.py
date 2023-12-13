from django.urls import path
from . import views
from .views import CreateRoomWizard

urlpatterns = [
    path('', views.home, name='home'),
    path('#', views.logoutUser, name='signout'),
path('user-profile', views.userProfile, name='user-profile'),
    path('create-room/', CreateRoomWizard.as_view(), name='create_room'),
    path('feedback/', views.feedback_view, name='feedback_view'),
]
