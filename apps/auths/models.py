from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.exceptions import ValidationError
from django.db import models


class CustomUserManager(BaseUserManager):
    """User manager."""
    def create_user(self, email, password):
        if not email:
            raise ValidationError('Email required')

        user = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """User model."""
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        max_length=150,
    )
    first_name = models.CharField(
        verbose_name='first_name',
        max_length=150
    )
    last_name = models.CharField(
        verbose_name='last_name',
        max_length=150
    )
    is_active = models.BooleanField(
        verbose_name='is_active',
        default=True
    )
    is_superuser = models.BooleanField(
        verbose_name='is_superuser',
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name='is_staff',
        default=False
    )
    creation_date = models.DateTimeField(
        verbose_name='creation_date',
        auto_now_add=True
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = (
            '-creation_date',
        )
