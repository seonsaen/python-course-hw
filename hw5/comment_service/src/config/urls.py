from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Comments API",
        default_version='v1',
        description="API для сервиса комментариев",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]