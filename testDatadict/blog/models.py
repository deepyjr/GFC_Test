from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=50, default='Unknow')
    created = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthDate = models.DateField()
    langage = models.CharField(max_length=3, default='FR')

