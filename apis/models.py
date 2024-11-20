from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now=True)
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.book.quantity -= 1
            self.book.save()
        else:
            if self.return_date:
                self.book.quantity += 1
                self.book.save()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} return date: {self.return_date}"
