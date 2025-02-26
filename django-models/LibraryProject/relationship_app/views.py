from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth.decorators import user_passes_test

# Function-Based View (FBV)- Lists all books.
def list_books(request):
    books = Book.objects.all() # Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View (CBV) - Displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='Member') # Create a UserProfile with default 'Member'
            return redirect('login') # Redirect to login after successful registration
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})

# Role Check Functions
def is_admin(user):
    return user.is_authenticated and (user.is_superuser or (hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'))

def is_librarian(user):
    return user.is_authenticated and (hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian')

def is_member(user):
    return user.is_authenticated and (hasattr(user, 'userprofile') and user.userprofile.role == 'Member')

# Admin View - Only accessible to Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin.html')

# Librarian View - Only accessible to Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html')

# Member View - Only accessible to Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member.html')
