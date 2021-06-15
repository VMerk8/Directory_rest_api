from django.urls import path, include

from .views import DirectoryView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('directory', DirectoryView, basename='Directory')

urlpatterns = [
    path('api/', include(router.urls))
]
