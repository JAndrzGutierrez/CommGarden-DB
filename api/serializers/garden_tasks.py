from rest_framework import serializers
from ..models.garden_tasks import Garden_Tasks

class Garden_TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden_Tasks
        fields = ('task','status', 'user', 'created_at','updated_at','id' )