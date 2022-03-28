from urllib import response
from api.models import garden_tasks
from api.models.garden_tasks import Garden_Tasks
from api.serializers.garden_tasks import Garden_TasksSerializer
from ..models import Garden_Tasks
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404

class Garden_TasksView(generics.CreateAPIView):
    def get(self, request):
        garden_tasks = Garden_Tasks.objects.filter(user=request.user.id)
        data = Garden_TasksSerializer(garden_tasks, many=True).data
        return Response(data)
        
    def post(self, request):
        request.data['garden_tasks'] = request.user.id
        task = Garden_TasksSerializer(data=request.data)
        if task.is_valid():
            task.save()
            return Response(task.data, status=status.HTTP_201_CREATED)
        else:
            return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)

class Garden_TaskView(generics.CreateAPIView):
    def get(self, request, pk):
        garden_task = get_object_or_404(Garden_Tasks, pk=pk)
        data = Garden_TasksSerializer(garden_task).data
        return Response(data)
    
    def delete(self, request, pk):
        garden_task = get_object_or_404(Garden_Tasks, pk=pk)
        garden_task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        garden_task = get_object_or_404(Garden_Tasks, pk=pk)
        updated_garden_task = Garden_TasksSerializer(garden_task, data=request.data, partial=True)
        if updated_garden_task.is_valid():
            updated_garden_task.save()
            return Response(updated_garden_task.data)
        else:
            return Response(updated_garden_task.errors, status=status.HTTP_400_BAD_REQUEST)

