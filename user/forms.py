
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . models import CustomUser

class RegisteForm(UserCreationForm):
    GENDER = (
        ('MALE', 'Male'),
        ('FAMALE', 'Famale')
    )
    OCCUPATION = (
        ('СТУДЕНТ', 'Студент'),
        ('РАБОТАЮ', 'Работаю'),
        ('ШКОЛЬНИК', "Школьник"),
        ('ДОМАХОЗЯЙКА', 'Домахозяйка')

    )

    COUNTRY = (
        ('ГЕРМАНИЯ', 'германия'),
        ('францыя', 'ФРАНЦЫЯ'),

    )

    SPORT = (
        ('БАСКЕТБОЛ', 'баскетбол'),
        ('КИБЕРСПОРТ', 'Киберспорт'),
        ('валебол', 'ВАЛЕБОЛ')
    )

    gender = forms.ChoiceField(choices=GENDER, required=True)
    occupation = forms.ChoiceField(choices=OCCUPATION, required=True)
    country = forms.ChoiceField(choices=COUNTRY, required=True)
    sport = forms.ChoiceField(choices=SPORT, required=True)
    phone = forms.CharField(required=True)
    city = forms.CharField(required=True)
    address = forms.CharField(required=True)


    class Meta:
        model = CustomUser
        fields = [

            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'gender',
            'occupation',
            'country',
            'sport',
            'phone',
            'city',
            'address',
        ]

    def save(self, commit=True):
        user = super(RegisteForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

class Login(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone= forms.CharField(required=True)