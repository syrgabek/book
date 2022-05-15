
from django.urls import path
from . import views, models


# add_name = "parser_urls"

urlpatterns = [

    path("parser/", views.ParserFormView.as_view(), name="parser_view"),
    path("parser/d/", views.ParserListView.as_view(
        queryset=models.ParserBook.objects.order_by('-id')
    ), name="parser_book"),
    # path("parser/a/", views.RanobeListView.as_view(
    #     queryset=models.ParserBook.objects.order_by('-id')
    # ), name="parser_book"),
]