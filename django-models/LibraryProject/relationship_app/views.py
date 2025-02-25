from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View (FBV)- Lists all books.
def list_books(request):
    book = Book.objects.all() # Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View (CBV) - Displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

