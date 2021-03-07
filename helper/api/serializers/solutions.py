from rest_framework import serializers
from api.models import solutions as solutions_models


class WorksheetGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = solutions_models.WorksheetGroup
        fields = ['department_major', 'degree', 'semester']


class WorksheetAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = solutions_models.WorksheetAuthor
        fields = ['name', 'surname', 'academic_title', 'college']


class WorksheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = solutions_models.Worksheet
        fields = ['title', 'author']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = solutions_models.Task
        fields = ['worksheet', 'description']


class SolutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = solutions_models.Solution
        fields = ['task', 'solution_file', 'solution_text', 'solution_rate']
