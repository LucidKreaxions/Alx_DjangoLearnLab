from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer


class BookList(ListAPIView):
    """
    API View that lists all books (Read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet that provides CRUD operations for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
