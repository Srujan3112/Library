from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='media')
    image = models.ImageField(upload_to='pics', blank=True, null=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body= models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)


class RBook(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    def __str__(self):
        return self.name


