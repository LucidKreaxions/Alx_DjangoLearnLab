from django.urls import path  # ✅ Import path
from django.contrib.auth.views import LoginView, LogoutView 
from .views import list_books, LibraryDetailView, register  # ✅ Import both views

urlpatterns = [
    # Existing URLs
    path('books/', list_books, name='list_books'),  # ✅ Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅ Class-based view

    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'), # Login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), # Logout view
]

