from rest_framework import routers

from .viewsets import TaskViewSet, TasksLastSevenDaysViewSet

router = routers.SimpleRouter();
router.register('tasks', TaskViewSet);
router.register('tasksLastSevenDays', TasksLastSevenDaysViewSet, 'tasks_last_seven_days');

urlpatterns = router.urls
