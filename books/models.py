
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)

    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='books'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='books'
    )

    isbn = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
