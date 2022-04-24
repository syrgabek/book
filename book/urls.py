from django.urls import path
from . import views

add_name ='book'

urlpatterns = [
    path('hello/', views.hello_word, name='hello'),
    path('book/', views.book_all, name='book_all'),
    path('book/<int:id>/', views.books_detail, name='books_detail'),
    path('add-book/', views.add_book, name='add_book')
]
