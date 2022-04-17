from django.shortcuts import render
from django.http import HttpRequest
from . import models


def hello_word(request):
    return HttpRequest()

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})
