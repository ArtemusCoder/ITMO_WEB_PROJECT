from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='post_pics', default="")
    content = models.TextField()
    date_post = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='post_like')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})