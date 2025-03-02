from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm # adding/editing book

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

# Book Management Views
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()

    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)

    return render(request, 'relationship_app.can_delete_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book.html', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')

    return render(request, 'relationship_app/delete_book.html', {'book': book})

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
