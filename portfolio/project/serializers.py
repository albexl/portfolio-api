from rest_framework import serializers

from project.models import ProjectInfo


class ProjectInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectInfo
        fields = '__all__'
