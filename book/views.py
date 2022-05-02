from django.shortcuts import render,get_object_or_404

from . import models, forma
from django.shortcuts import redirect, reverse

from django. views import generic




class BookListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset


class BookDetailView(generic.DetailView):
    template_name = "books_deteil.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)


class BookCreateView(generic.CreateView):
    template_name = "book_add.html"
    form_class = forma.BookForm
    queryset = models.Book.objects.all()
    success_url = "/book/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forma.BookForm
    success_url = "/book/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)


class BookDeleteView(generic.DeleteView):
    success_url = "/book"
    template_name = "confic_delee.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)





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

