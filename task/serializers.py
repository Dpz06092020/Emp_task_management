from rest_framework import serializers
from task.models import TaskSheet


class FetchTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSheet
        fields = ['employee_name', 'task', 'time', 'review_status', 'review_comment']

