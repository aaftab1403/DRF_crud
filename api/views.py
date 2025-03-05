from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Task
from .serializers import TaskSerializer

class TaskFlowAPI(APIView):
    
    # Retrieve all tasks
    def get(self, request):
        tasks = Task.objects.all()
        tasks_data = TaskSerializer(tasks, many=True).data
        return Response(tasks_data, status=status.HTTP_200_OK)
      
    # Create a new task
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    
    # Update a task by id
    def put(self, request, id):
        task = Task.objects.filter(id=id).first()
        if not task:
            return Response({"error": "Task not found!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete a task by id 
    def delete(self, request, id):
        task = Task.objects.filter(id=id).first()
        if not task:
            return Response({"error": "Task not found!"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"message": "Task deleted successfully!"}, status=status.HTTP_200_OK)

      
