from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,Http404
from . import models, forma
from django.shortcuts import redirect, reverse
from datetime import datetime, timedelta

start_date = datetime.today() - timedelta(days=20)

def hello_word(request):
    return HttpRequest()

def book_all(request):
    book = models.Book.objects.order_by()
    return render(request, 'book_list.html', {'book': book})


def book_latest(request):
    book = models.Book.objects.filter(createa_data__gt=start_date).order_by('-id')
    return render(request, 'book_list.html', {'book': book})


def book_genre_romace(request):
    book = models.Book.objects.filter(gengre='ROMANCE').order_by("-id")
    return render(request, 'book_list.html', {'book': book})





def book_genre_priklyucheniya(request):
    book = models.Book.objects.filter(gengre='ADVENTURES').order_by('-id')
    return render(request, 'book_list.html', {'book': book})


def book_genre_anime(request):
    book = models.Book.objects.filter(gengre='ANIME').order_by('-id')
    return render(request, 'book_list.html', {'book': book})


def books_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, "books_deteil.html", {"book": book})





def add_book(request):
    method = request.method
    if method == "POST":
        form = forma.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse("book:book_all"))
    else:
        form = forma.BookForm()
    return render(request, "book_add.html", {'form': form})

def put_update_book(request, id):
    book_id = get_object_or_404(models.Book,id=id)
    if request.method == 'POST':
        form = forma.BookForm(instance=book_id,
                              data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("book:book_all"))
    else:
        form = forma.BookForm(instance=book_id)
    return render(request, "book_update.html", {'form': form,
                                                'book': book_id})

