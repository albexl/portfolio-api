from django.urls import include, path
from rest_framework.routers import DefaultRouter

from project import views

router = DefaultRouter()

router.register(r'project_info', views.ProjectInfoViewSet,
                basename='project_info')

urlpatterns = [
    path('', include(router.urls))
]
