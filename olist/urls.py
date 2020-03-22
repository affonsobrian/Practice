from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from library.views import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]