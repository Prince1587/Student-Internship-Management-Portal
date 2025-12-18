from django.db import models
from django.contrib.auth.models import User


class Internship(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stipend = models.IntegerField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} → {self.internship.title}"

