from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
from books.models.user import Author
from books.models.book import Book


def is_user_or_admin(request, book_idx:str) -> bool:
    book_obj = Book.objects.filter(idx=book_idx).first()
    if not (request.user == book_obj.owner or isinstance(request.user, get_user_model())):
        return False
    return True

class IsLoggedIn(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, Author) or isinstance(request.user, get_user_model())

class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view, obj):
        return get_user_model() or request.user == obj.owner