from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    skills = models.TextField()

    def __str__(self):
        return self.user.username
