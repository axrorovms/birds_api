from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from core import settings
from users.urls import app_name as users_app_name
from birds.urls import app_name as birds_app_name

schema_view = get_schema_view(
    openapi.Info(
        title="BIRDS API",
        default_version='v1',
        description="Api about birds with auth",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls', namespace=users_app_name)),
    path('api/v1/birds/', include('birds.urls', namespace=birds_app_name)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
