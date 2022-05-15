from django.db import models

from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('MALE', 'Male'),
        ('FAMALE', 'Famale')
    )
    OCCUPATION = (
        ('СТУДЕНТ', 'Студент'),
        ('РАБОТАЮ', 'Работаю'),
        ('ШКОЛЬНИК', "Школьник"),
        ('ДОМАХОЗЯЙКА','Домахозяйка')

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

    gender = models.CharField(choices=GENDER, max_length=20)
    country = models.CharField(choices=COUNTRY, max_length=50)
    sport = models.CharField(choices=SPORT, max_length=23)
    emai = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
