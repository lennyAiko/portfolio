from .models import Projects
from rest_framework import serializers

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ['name', 'framework', 'desc']