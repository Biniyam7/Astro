from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class zodiac(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    content_2 = models.TextField(default='DEFAULT VALUE')
    content_3 = models.TextField(default='DEFAULT VALUE')
    marriage = models.TextField(default='DEFAULT VALUE')
    marriage_2 = models.TextField(default='DEFAULT VALUE')
    career = models.TextField(default='DEFAULT VALUE')
    career_2 = models.TextField(default='DEFAULT VALUE')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

