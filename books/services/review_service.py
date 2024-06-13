from books.models import Review
from books.serializers.review_serializer import ReviewSerializer


class ReviewService:

    @staticmethod
    def get_reviews_by_book_idx(idx):
        reviews = Review.get_reviews_by_book_idx(idx)
        return ReviewSerializer(reviews, many=True).data