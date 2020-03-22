from rest_framework import viewsets

from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = ()
    filter_fields = ('name',)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = ()
    filter_fields = ('name', 'edition', 'publication_year', 'authors')