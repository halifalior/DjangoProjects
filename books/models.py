from django.db import models

class Book(models.Model):

    DRAMA = 'DR'
    BIOGRAPHY = 'BI'
    CHILDREN = 'CH'
    FANTASY = 'FA'
    ROMANCE = 'RO'
    BOOKS_CHOICES = [
        (DRAMA, 'דרמה'),
        (BIOGRAPHY, 'ביוגרפיה'),
        (CHILDREN, 'ילדים'),
        (FANTASY, 'פנטזיה'),
        (ROMANCE, 'רומן'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    image = models.FilePathField(path='books\static\img')
    genre = models.CharField(
        max_length=2,
        choices=BOOKS_CHOICES,
        default=DRAMA
    )


