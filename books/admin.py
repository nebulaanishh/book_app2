from django.contrib import admin
from .models import Book, Review, Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'owner', 'image')    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'rating', 'owner', 'book')