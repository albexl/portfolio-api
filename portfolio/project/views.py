from project.models import ProjectInfo
from project.serializers import ProjectInfoSerializer
from rest_framework import viewsets

# Create your views here.


class ProjectInfoViewSet(viewsets.ModelViewSet):

    queryset = ProjectInfo.objects.filter(show=True)
    serializer_class = ProjectInfoSerializer
