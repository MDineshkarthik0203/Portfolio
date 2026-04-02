from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(APIView):

    # GET /api/projects/
    # Returns all projects
    def get(self, request):
        projects = Project.objects.all().order_by('-created_at')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    # POST /api/projects/
    # Add a new project
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):

    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return None

    # GET /api/projects/1/
    # Get one project by id
    def get(self, request, pk):
        project = self.get_project(pk)
        if project is None:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    # PUT /api/projects/1/
    # Update a project
    def put(self, request, pk):
        project = self.get_project(pk)
        if project is None:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE /api/projects/1/
    # Delete a project
    def delete(self, request, pk):
        project = self.get_project(pk)
        if project is None:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response({'message': 'Project deleted'}, status=status.HTTP_200_OK)
