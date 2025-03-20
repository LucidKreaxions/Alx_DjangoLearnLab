from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookListCreateView(generics.ListAPIView):
    """List & Create Books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, write for authenticated users


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrive, Update, Delete a single book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, edit/delete for authenticated users
