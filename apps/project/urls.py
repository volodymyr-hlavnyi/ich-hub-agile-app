from django.urls import path
from apps.project.views.project_views import ProjectsApi, ProjectDetailAPIView

urlpatterns = [
    path('projects/', ProjectsApi.as_view()),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view()),
]