from django.urls import path
from books import views as views

urlpatterns = [
    # Author Login/Register
    path("register/", views.register_user, name='user-register'),
    path("login/", views.login, name='user-login'),
    # Books
    path("books/", views.book_list, name='book-list'),
    path("books/<str:idx>/", views.book_detail, name='book-detail'),
    path("protected/", views.protected_view, name='protected-view')
]