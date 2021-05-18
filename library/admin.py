from django.contrib import admin
from .models import Book,RBook,Comment
# Register your models here.
admin.site.register(Book)
admin.site.register(RBook)
admin.site.register(Comment)