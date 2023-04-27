from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(
        verbose_name='пользователь',
        to=User,
        on_delete=models.CASCADE
    )
    sm_pp = models.SmallIntegerField(
        verbose_name='sm_pp',
        validators=[MaxValueValidator(5)]
    )

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class Book(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=200
    )
    pages = models.PositiveIntegerField(
        verbose_name='количество страниц'
    )
    authors = models.ManyToManyField(
        verbose_name='авторы',
        to=Author,
        related_name='books'
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self) -> str:
        return self.title
