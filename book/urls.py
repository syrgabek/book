from django.urls import path
from . import views

add_name ='book'

urlpatterns = [
    path('hello/', views.hello_word, name='hello'),
    path('book/', views.book_all, name='book_all'),
    path('book/latest/', views.book_latest, name='book_latest'),
    path('book/anime/', views.book_genre_anime, name='book_anime'),
    path('book/priklyucheniya/', views.book_genre_priklyucheniya, name='book_priklyucheniya'),
    path('book/romace/', views.book_genre_romace, name='book_romace'),

    path('book/<int:id>/', views.books_detail, name='books_detail'),
    path('book/<int:id>/update/', views.put_update_book, name='books_detail'),
    path('add-book/', views.add_book, name='add_book')
]
