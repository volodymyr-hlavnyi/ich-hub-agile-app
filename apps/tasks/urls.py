from django.urls import path

from apps.tasks.views.tag_views import TagApi, TagListApi

urlpatterns = [
    path('tag/<int:pk>', TagApi.as_view() ),
    path('tag/', TagListApi.as_view() ),
    ]