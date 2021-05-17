import os
from django.shortcuts import render
from se_project import settings
from .models import Book
from django.http import HttpResponse, Http404


# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {'books': books})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404

