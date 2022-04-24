from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,Http404
from . import models, forma
from django.shortcuts import redirect, reverse

def hello_word(request):
    return HttpRequest()

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def books_detail(request,id):
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
