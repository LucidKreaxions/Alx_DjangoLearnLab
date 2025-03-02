from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # ✅ Import views as a module

urlpatterns = [
    # Existing URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Book Management URLs
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),


    # Role-Based Access URLs
    path('admin_view/', views.admin_view, name='admin_view'),
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('admin/', views.admin_view, name='admin_page'),

    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),



]

