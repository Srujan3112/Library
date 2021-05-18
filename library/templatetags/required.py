from django import template
from library.models import Book

register = template.Library()


@register.simple_tag
def return_book(request, id_val):
    try:
        book = Book.objects.get(id=id_val)
    except:
        return None
    return book
