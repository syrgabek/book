from . import parsinc, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ('ParserBook', 'ParserBook'),
        ('New', 'New'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == "ParserBook":
            book_parser = parsinc.parser_func()
            for data in book_parser:
                models.ParserBook.objects.create(**data)
        # elif self.data['media_type'] == "New":
        #     new_parser = parsinc.parser_func2()
        #     for data in new_parser:
        #          models.ParserBook.objects.create(**data)