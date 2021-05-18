import os
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import CommentForm
from .models import Comment
from se_project import settings
from .models import Book, RBook
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404


# Create your views here.


class BooksList(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            books = Book.objects.all()
            books = books.filter(name__startswith=search_input)
            context['books'] = books
            # context['books'] = context['books'].filter(name__startswith=search_input)
        context['search_input'] = search_input
        return context


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = ['name', 'pdf', 'image', 'description']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreate, self).form_valid(form)


class RequestedBookCreate(LoginRequiredMixin, CreateView):
    model = RBook
    template_name = 'requested_book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RequestedBookCreate, self).form_valid(form)


class RequiredBooksList(LoginRequiredMixin, ListView):
    model = RBook
    context_object_name = 'rbooks'
    template_name = 'required_books_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            rbooks = RBook.objects.all()
            products = RBook.filter(title__startswith=search_input)
            context['rbooks'] = rbooks
        context['search_input'] = search_input
        return context


def book_detail(request, pk):
    template_name = 'post_detail.html'
    book = get_object_or_404(Book, id=pk)
    comments = Comment.objects.filter(book=book.id)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.book = book
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def BookDetail(request, pk):
    book = Book.objects.get(id=pk)
    comments=Comment.objects.filter(book=book.id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    form = CommentForm(
        initial={'user': request.user, 'book': book})
    context = {'form': form, 'user': request.user.username, 'book': book,'comments':comments}
    return render(request, 'book_detail.html', context)
