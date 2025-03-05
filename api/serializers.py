from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    def validate_status(self, value):
        """Ensure that the status field only accepts valid choices"""
        valid_statuses = [choice[0] for choice in Task.StatusChoices.choices]
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Invalid status. Choose from {valid_statuses}")
        return value

    class Meta:
        model = Task
        fields = ['id', 'title', 'status']
