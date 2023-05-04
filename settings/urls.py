from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from books.views import (
    ListBookView,
    ListAuthorView,
    AsyncView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/books', ListBookView.as_view()),
    path('api/v1/authors', ListAuthorView.as_view()),
    path('api/v1/async', AsyncView.as_view()),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
