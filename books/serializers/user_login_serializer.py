from rest_framework import serializers
from books.models.user import Author
from books.helpers.auth_utils import hash_raw_password

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        extra_kwargs = {
            'password': {'write_only': True}
        }
        fields = ('id', 'first_name', 'last_name', 'email', 'password',)

    # def create(self, validated_data):
    #     print(validated_data)
    #     validated_data['password'] = hash_raw_password(validated_data['password'])
    #     return super(AuthorSerializer, self).create(validated_data)
    
class AuthorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=64)