from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BlogViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
