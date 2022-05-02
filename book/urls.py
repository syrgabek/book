from django.urls import path
from . import views,models
from datetime import datetime,timedelta

start_date = datetime.today() - timedelta(days=365)

add_name = "book"

urlpatterns = [
    path("book/", views.BookListView.as_view(), name="book_all"),
    path(
        "book/latest/",
        views.BookListView.as_view(
            queryset=models.Book.objects.filter(createa_data__gt=start_date).order_by(
                "-id"
            )
        ),
        name="book_latest",
    ),
   
    path(
        "book/romace/",
        views.BookListView.as_view(
            queryset=models.Book.objects.filter(gengre="ROMACE").order_by("-id")
        ),
        name="book_romace",
    ),


    path(
        "book/anime/",
        views.BookListView.as_view(
            queryset=models.Book.objects.filter(gengre="ANIME").order_by("-id")
        ),
        name="book_anime",
    ),
    path("book/<int:id>/", views.BookDetailView.as_view(), name="books_detail"),
    path("book/<int:id>/update/", views.BookUpdateView.as_view(), name="books_update"),
    path("book/<int:id>/delete/", views.BookDeleteView.as_view(), name="books_delete"),
    path("add-book/", views.BookCreateView.as_view(), name="add_book"),
]


