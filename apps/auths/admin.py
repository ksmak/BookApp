from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User

    add_fieldsets = (
        ('Personal date', {
            'classes': (
                'wide'
            ),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2'
            )

        }),
        ('Permissions', {
            'classes': (
                'wide'
            ),
            'fields': (
                'is_active',
                'is_superuser',
                'groups'
            )
        })
    )

    fieldsets = (
        ('Personal data', {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password',
            )
        }),
        ('Permisions', {
            'fields': (
                'is_active',
                'is_superuser',
                'groups'
            )
        })
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser'
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
    )

    ordering = (
        'email',
        'first_name',
        'last_name',
    )


admin.site.register(User, CustomUserAdmin)
