from django.http import HttpResponse, JsonResponse
from django.views import View 
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from .pagination import TaskPagination
from .filters import TaskFilter
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    filterset_class = TaskFilter
    