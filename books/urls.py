from django.urls import path
from books import views

urlpatterns = [
    path("books/", views.book_list, name='book-list'),
    path("books/<str:idx>/", views.book_detail, name='book-detail'),
]