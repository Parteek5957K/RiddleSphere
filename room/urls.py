from django.urls import path
from . import views

urlpatterns = [
    path('bunker/', views.roomvisit, name='roomv'),
    path('bunker-room/', views.roombunker, name='room-bunker'),
    path('library/', views.roomvisit2, name='roomv2'),
    path('graveyard/', views.roomvisit3, name='roomv3'),
    path('library-room/', views.roomlibrary, name='room-library'),
    path('bunker-room/get_answer/', views.get_answer, name='get_answer'),
    path('quiz/', views.quizques, name='quiz'),
    path('submit_game/', views.submit_game, name='submit_game'),
    path('get_serial_message/', views.get_serial_message, name='get_serial_message'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
]
