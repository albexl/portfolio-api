from django.urls import include, path
from rest_framework.routers import DefaultRouter

from project import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]
