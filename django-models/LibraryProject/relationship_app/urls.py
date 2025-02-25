from django.urls import path  # ✅ Import path
from .views import list_books, LibraryDetailView  # ✅ Import both views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # ✅ Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅ Class-based view
]

