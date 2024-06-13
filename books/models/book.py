from django.db import models
from django.db.models import Avg

from books.models.base import BaseModel
from books.models.user import Author

class Book(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="book_covers/")
    owner = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self) -> str:
        return self.title

    @property
    def average_rating(self):
        avg_rating = self.reviews.aggregate(average=Avg('rating'))['average']
        return avg_rating if avg_rating is not None else 0


    @classmethod
    def get_all_books(cls, *args, **kwargs):
        books = cls.objects.all()
        return books

    @classmethod
    def get_book_by_idx(cls, idx: str):
        book = cls.objects.get(idx=idx)
        return book

    @classmethod
    def get_book_by_title(cls, title: str):
        book = cls.objects.get(title=title)
        return book
