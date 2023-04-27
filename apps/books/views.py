from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.db.models import QuerySet

from .models import Book, Author
from .serializers import (
    ListBookSerializer,
    ListAuthorSerializer
)


class ListBookView(APIView):
    """Books View."""

    def get(
        self,
        request: Request
    ) -> Response:
        queryset: QuerySet = Book.objects.prefetch_related('authors').all()
        serializer: ListBookSerializer = \
            ListBookSerializer(
                queryset,
                many=True
            )

        return Response(serializer.data)


class ListAuthorView(APIView):
    """Author View."""

    def get(
        self,
        request: Request
    ) -> Response:
        queryset: QuerySet = Author.objects.select_related(
            'user').prefetch_related('books').all()
        serializer: ListAuthorSerializer = \
            ListAuthorSerializer(
                queryset,
                many=True
            )

        return Response(serializer.data)
