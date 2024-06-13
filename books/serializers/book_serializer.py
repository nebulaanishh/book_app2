from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['idx', 'title', 'content', 'image', 'owner', 'average_rating']    
    
    def get_average_rating(self, obj):
        return obj.average_rating