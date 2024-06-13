from typing import Tuple
from django.db.models import QuerySet
from books.models import Book
from books.serializers.book_serializer import BookSerializer
from books.helpers.logging_helper import logger



class BookService:
    def get_all_book(self, request, *args, **kwargs):
        title = request.GET.get('title')
        content = request.GET.get('content')
        created_at = request.GET.get("created_at")
        books = Book.get_all_books(kwargs)
        if title:
            books = books.filter(title__icontains=title)
        if content:
            books = books.filter(content__icontains=content)
        if created_at:
            books = books.filter(created_at=created_at)
        serializer = BookSerializer(books, many=True)
        return serializer.data

    def get_book_by_idx(self, idx):
        book = Book.get_book_by_idx(idx)
        if book:
            return BookSerializer(book).data
        return None

    def get_book_by_title(self, title: str):
        book = Book.get_book_by_title(title)
        if book:
            return BookSerializer(book).data
        return None

    def create_new_book(self,data) -> Tuple[QuerySet, bool]:
        """
        Return
            Serializer.ReturnDict, bool
            True if ReturnDict is error
            False if ReturnDict is data
        """
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info("New book created")
            return serializer.data, True
        else:
            logger.error(f"BookService.create_new_book :: ValueError :: {serializer.errors}")
            return serializer.errors, False

    def update_book(self, book_idx: str, new_data) -> Tuple[QuerySet, bool]:
        """
        Return
            Serializer.ReturnDict, bool
            True if ReturnDict is error
            False if ReturnDict is data
        """
        old_data = Book.objects.filter(idx=book_idx).first()
        serializer = BookSerializer(old_data,data=new_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Book Updated")
            return serializer.data, False
        else:
            logger.error(f"BookService.updated_book :: ValueError")
            return serializer.errors, True


    def delete_book(self, book_idx: str) -> bool:
        book = Book.objects.filter(idx=book_idx).first()
        if book:
            book.delete()
            return True
        return False