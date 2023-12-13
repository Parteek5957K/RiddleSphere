from django.db import models

# Create your models here.
class Puzzle(models.Model):
    name=models.CharField(max_length=25, null=True)

class EscapeRoom(models.Model):
    title=models.CharField(max_length=100, null=True)
    description=models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.title