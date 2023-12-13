from django.urls import path
from . import views

urlpatterns = [
    path('get_answer/', views.get_answer, name='get_answer'),
path('1/', views.puzzle1, name='puzzle1'),
path('2/', views.puzzle2, name='puzzle2'),
path('3/', views.puzzle3, name='puzzle3'),
path('4/', views.puzzle4, name='puzzle4'),
path('5/', views.puzzle5, name='puzzle5'),
]
