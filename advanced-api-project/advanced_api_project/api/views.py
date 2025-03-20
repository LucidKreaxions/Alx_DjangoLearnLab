from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookListView(generics.ListAPIView):  # Change from ListCreateAPIView to ListAPIView
    """List all Books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, write for authenticated users


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update, Delete a single book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, edit/delete for authenticated users

