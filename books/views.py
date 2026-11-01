
from rest_framework import viewsets
from .models import Book, Author, Category
from .serializers import (
    BookSerializer,
    AuthorSerializer,
    CategorySerializer,
)
from .permissions import ReadOnlyOrAdmin


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related(
        'author', 'category'
    ).all()

    serializer_class = BookSerializer
    permission_classes = [ReadOnlyOrAdmin]

    search_fields = ['title', 'isbn']

    filterset_fields = [
        'author',
        'category',
        'published_date',
    ]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [ReadOnlyOrAdmin]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyOrAdmin]
