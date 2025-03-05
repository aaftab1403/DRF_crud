from django.urls import path
from .views import TaskFlowAPI

urlpatterns = [
    path('', TaskFlowAPI.as_view()),
    path('add/',TaskFlowAPI.as_view()),
    path('update/<int:id>/', TaskFlowAPI.as_view(), name="task-update"),
    path('delete/<int:id>/', TaskFlowAPI.as_view(), name="task-delete"),
]