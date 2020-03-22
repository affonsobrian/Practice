from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)


class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    edition = models.IntegerField(null=False, blank=False)
    publication_year = models.IntegerField(null=False, blank=False)
    authors = models.ManyToManyField(Author, related_name='books', related_query_name='book')
