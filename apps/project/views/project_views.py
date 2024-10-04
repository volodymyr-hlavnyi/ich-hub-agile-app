from django.utils.timezone import make_aware
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from apps.project.models.project import Project
from apps.project.serializers.project_serializers import AllProjectsSerializer, CreateProjectSerializer, \
    ProjectDetailSerializer
from datetime import datetime


class ProjectsApi(APIView):
    serializer_class = AllProjectsSerializer

    def get(self, request):
        queryset = Project.objects.all()
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)

        if date_from and date_to:
            try:
                date_from = make_aware(datetime.strptime(date_from, '%Y-%m-%d'), timezone.get_current_timezone())
                date_to = make_aware(datetime.strptime(date_to, '%Y-%m-%d'), timezone.get_current_timezone())
                queryset = queryset.filter(created_at__range=(date_from, date_to))
            except ValueError:
                pass  # Handle invalid date format if necessary

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailAPIView(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
