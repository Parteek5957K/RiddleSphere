from django.db import models
from django.contrib.auth.models import AbstractUser
from room.models import *


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    # avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Room(models.Model):
    name = models.CharField(max_length=255)
    url = models.SlugField(unique=True)
    theme = models.CharField(max_length=255)
    story = models.TextField()
    custom_intro = models.TextField(default='Default Intro')

class Puzzle(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    puzzle_number = models.IntegerField()
    file = models.FileField(upload_to='puzzles/')
    # Add more puzzle-related fields as needed

class RoomRole(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

class RoomPublishDate(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()

class RoomStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(EscapeRoom, on_delete=models.CASCADE)
    times = ...
    timef = ...
    hint_used = ...


class Feedback(models.Model):
    rating = models.IntegerField()
