from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,Http404
from . import models


def hello_word(request):
    return HttpRequest()

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def books_detail(request,id):
    try:
        book = get_object_or_404(models.Book,id = id)
        try:
            comment = models.BookComet.objects.filter(books_id = id).order_by("cd")
        except models.Book.DuesNotExist:
            print('nocomment')
    except models.Book.DuesNotExist:
        raise Http404('книга не найдена')
    return render(request,'books_detail.html',{'book':book})
