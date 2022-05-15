from django.shortcuts import redirect

from django.urls import reverse
from django.views import generic
from . import models, forms


class ParserFormView(generic.FormView):
    template_name = "parser.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect(reverse("parser_book"))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)


class ParserListView(generic.ListView):
    template_name = "parserbook_list.html"
    queryset = models.ParserBook.objects.all()


    def get_queryset(self):
        return self.queryset


class RanobeListView(generic.ListView):
    template_name = "ranobe.html"
    queryset = models.ParserBook.objects.all()

    def get_queryset(self):
        return self.queryset