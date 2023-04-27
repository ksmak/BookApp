from rest_framework import serializers

from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    """Author serializer."""

    class Meta:
        model = Author
        fields = ('user', 'sm_pp')


class BookSerializer(serializers.ModelSerializer):
    """Book serializer."""

    class Meta:
        model = Book
        fields = ('title', 'pages')


class ListBookSerializer(serializers.ModelSerializer):
    """ListBook serializer."""
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class ListAuthorSerializer(serializers.ModelSerializer):
    """ListAuthor serializer."""
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = "__all__"
