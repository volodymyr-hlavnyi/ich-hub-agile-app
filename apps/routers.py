from django.urls import path, include

urlpatterns = [
    'tasks/', include('apps.tasks.urls')

]
