from typing import Any
import time

from django.db.models import QuerySet

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

import asyncio

from .models import Book, Author
from .serializers import (
    ListBookSerializer,
    ListAuthorSerializer
)


class AsyncView(APIView):
    """Use asyncio lib."""

    def __init__(self, **kwargs: Any) -> None:
        self._data: list[str] = []

    async def get_hello(self):
        print("Start get_hello...")
        await asyncio.sleep(3)
        print("End get_hello...")
        return 'Hello'

    async def get_world(self):
        print("Start get_world.")
        await asyncio.sleep(2)
        print("End get_world.")
        return 'World'

    async def get_thenia(self):
        print("Start get_thenia.")
        await asyncio.sleep(4)
        print("End get_thenia.")
        return 'Thenia'

    async def get_krut(self):
        print("Start get_krut.")
        await asyncio.sleep(1)
        print("End get_krut.")
        return 'Krut'

    async def handle_execute(self):
        tasks: list[Any] = [
            asyncio.ensure_future(self.get_hello()),
            asyncio.ensure_future(self.get_world()),
            asyncio.ensure_future(self.get_thenia()),
            asyncio.ensure_future(self.get_krut()),
        ]

        result = await asyncio.gather(*tasks)

        return ", ".join(result)

    def get(
        self,
        request: Request
    ) -> Response:
        start = time.perf_counter()
        event_loop: Any = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)
        res = event_loop.run_until_complete(
            self.handle_execute()
        )
        event_loop.close()
        end = time.perf_counter()
        return Response({
            'data': res,
            'time': f"{end - start:.4f}s"
        })


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
