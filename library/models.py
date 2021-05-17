from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='media')
    image = models.ImageField(upload_to='pics',blank=True,null=True)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name