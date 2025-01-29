from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="API documentation for Todo App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ashkanaj10000@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
