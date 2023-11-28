from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name

class TeamMembers(models.Model):
    name = models.CharField(max_length=250)
    profilePic = models.ImageField(upload_to='profile')
    description = models.TextField()

    def __str__(self):
        return self.name