from django.urls import path
from .views import BooksList,RequestedBookCreate,RequiredBooksList,BookCreate,BookDetail

urlpatterns = [
    path("", BooksList.as_view(), name="index"),
    path("required/", BooksList.as_view(), name="required"),
    path("required_book/create", RequestedBookCreate.as_view(), name="required_book_create"),
    path("required_books/", RequiredBooksList.as_view(), name="required_books"),
    path("upload_book/", BookCreate.as_view(), name="upload_book"),
    path('detail/<int:pk>/',BookDetail, name='detail'),
]
