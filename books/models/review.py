from django.db import models

from books.models.base import BaseModel
from books.models.book import Book
from books.models.user import Author


class Review(BaseModel):
    RATING_CHOICES = (
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="reviews", null=True
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        unique_together = ("book", "owner")

    def __str__(self) -> str:
        return f"Review for Book {self.book.title} by {self.owner.first_name} {self.owner.last_name}"

    @staticmethod
    def get_reviews_by_book_idx(idx: str):
        reviews = Review.objects.filter(book__idx=idx)
        return reviews
