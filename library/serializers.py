from rest_framework import serializers

from library.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'books')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'edition', 'publication_year', 'authors')
        read_only = ('authors',)

    """
    def create(self, validated_data):
        authors = validated_data.pop('authors', [])
        book = super(BookSerializer, self).create(validated_data)
        return book
    """