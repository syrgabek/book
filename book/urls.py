from django.urls import path
from . import views, models
from datetime import datetime, timedelta


start_date = datetime.today() - timedelta(days=365)

add_name = "book"

urlpatterns = [
    path("book/", views.BookListView.as_view(), name="book_all"),
    path(
        "book/latest/",
        views.BookListView.as_view(
            queryset=models.Book.objects.filter(created_date__gt=start_date).order_by(
                "-id"
            )
        ),
        name="book_latest",
    ),
    path(
        "book/detective/",
        views.BookListView.as_view(
            queryset=models.Book.objects.filter(genre="DETECTIVE").order_by("-id")
        ),
        name="book_detective",
    ),
    path(
        "book/romace/",
        views.BookListView.as_view(
            queryset=models.Book.objects.filter(genre="ROMACE").order_by("-id")
        ),
        name="book_romace",
    ),
    path(
        "book/fantasies/",
        views.BookListView.as_view(
            queryset=models.Book.objects.filter(genre="FANTASIES").order_by("-id")
        ),
        name="book_fantasies",
    ),
    path(
        "book/anime/",
        views.BookListView.as_view(
            queryset=models.Book.objects.filter(genre="ANIME").order_by("-id")
        ),
        name="book_anime",
    ),
    path("book/<int:id>/", views.BookDetailView.as_view(), name="books_detail"),
    path("book/<int:id>/update/", views.BookUpdateView.as_view(), name="books_update"),
    path("book/<int:id>/delete/", views.BookDeleteView.as_view(), name="books_delete"),
    path("add-book/", views.BookCreateView.as_view(), name="add_book")
]


