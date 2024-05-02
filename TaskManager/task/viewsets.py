from rest_framework import viewsets, status
from .models import Task
from rest_framework.response import Response
from datetime import datetime, timedelta
from .serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TasksLastSevenDaysViewSet(viewsets.ViewSet):
    def list(self, request):
        seven_days_ago = datetime.now() - timedelta(days=7)
        tasks = Task.objects.filter(
            deadline__gte=seven_days_ago, deadline__lte=datetime.now(), completed=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
