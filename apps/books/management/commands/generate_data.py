import random
from typing import Any

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.models import QuerySet

import names
from random_word import RandomWords

from ...models import Book, Author


User = get_user_model()


class Command(BaseCommand):
    """Custom command for filling up database."""

    help = 'Custom command for filling up database.'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.email_patterns = [
            'gmail.com',
            'mail.ru',
            'yagoo.com',
            'yandex.com',
            'tempmail.com'
        ]

    def generate_authors(self) -> QuerySet[Author]:

        emails = []

        for _ in range(1000):
            emails.append((
                f"{names.get_first_name()}@"
                f"{self.email_patterns[random.randrange(0, len(self.email_patterns))]}"  # noqa
            ))

        emails = set(emails)

        user_patterns = []

        for email in emails:
            user_patterns.append({
                'first_name': names.get_first_name(),
                'last_name': names.get_last_name(),
                'email': email
            })

        users = User.objects.bulk_create(
            [
                User(
                    email=user_p['email'],
                    first_name=user_p['first_name'],
                    last_name=user_p['last_name'],
                    password='12345'
                )
                for user_p in user_patterns
            ]
        )

        return Author.objects.bulk_create(
            [
                Author(
                    user=user,
                    sm_pp=random.randint(1, 5)
                )
                for user in users
            ]
        )

    def generate_books(self, authors) -> None:
        r = RandomWords()

        books = Book.objects.bulk_create(
            [
                Book(
                    title=r.get_random_word(),
                    pages=random.randrange(1000),
                )
                for _ in range(1000)
            ]
        )

        for book in books:
            book.authors.set([
                authors[random.randrange(0, len(authors))]
            ])

        Book.objects.bulk_update(books, ['authors'])

    def handle(self, *args: Any, **kwargs: Any) -> None:
        authors: QuerySet[Author] = self.generate_authors()
        self.generate_books(authors=authors)
