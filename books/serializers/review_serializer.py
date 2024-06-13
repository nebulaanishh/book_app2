from rest_framework import serializers
from books.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "rating", "review", "owner", "book"]
