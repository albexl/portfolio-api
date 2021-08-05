from rest_framework import viewsets

from project.models import ProjectInfo
from project.serializers import ProjectInfoSerializer

# Create your views here.


class ProjectInfoViewSet(viewsets.ModelViewSet):

    queryset = ProjectInfo.objects.filter(show=True)
    serializer_class = ProjectInfoSerializer
