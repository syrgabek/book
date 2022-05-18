from django.db import models


class Book(models.Model):
    GENRE = (
        ('ROMACE', "romace"),
        ("ADVENTURES", "priklyucheniya"),
        ('ANIME', "anime"),

    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    createa_data= models.DateField(auto_now_add=True)
    updeted_data = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='')
    author = models.CharField(max_length=25, null=True)
    gengre = models.CharField(max_length=90, choices=GENRE, null=True)

    def __str__(self):
        return self.title

class Bookdetails(models.Model):
    text=models.TextField()
    created_date = models.DateField(auto_now_add=True)

class BookComet(models.Model):
    text=models.TextField()
    created_date = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='books_comment')

class Review(models.Model):
    text = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)



