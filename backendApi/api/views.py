from .serializers import ProjectSerializer
from rest_framework import permissions
from rest_framework import viewsets
from .models import Projects

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows projects to be viewed and edited."""
    queryset = Projects.objects.all().order_by('-date_added')
    serializer_class = ProjectSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]