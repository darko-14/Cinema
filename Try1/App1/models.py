from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    image = models.ImageField(default='\media\default.jpg', upload_to='profile_pics')
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=100, default="")
    cast = models.CharField(max_length=100, default="")
    director = models.CharField(max_length=30, default="")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date1 = models.DateTimeField(default=timezone.now)
    date2 = models.DateTimeField(default=timezone.now)
    date3 = models.DateTimeField(default=timezone.now)
    date4 = models.DateTimeField(default=timezone.now)
    date5 = models.DateTimeField(default=timezone.now)
    price = models.PositiveSmallIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# class Dates(models.Model):
#     movie = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True,)
#     day = models.CharField(max_length=15, default="")
#     date1 = models.DateTimeField(default=timezone.now)
#     date2 = models.DateTimeField(default=timezone.now)
#     date3 = models.DateTimeField(default=timezone.now)
#     date4 = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return str(self.movie)

