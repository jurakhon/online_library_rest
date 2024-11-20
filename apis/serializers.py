from rest_framework import serializers
from .models import Book, Author, Borrow, Genre, Publisher

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    genres = serializers.StringRelatedField(many=True)
    publisher = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Borrow
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name',]

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
