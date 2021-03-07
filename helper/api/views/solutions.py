from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
import api.models.solutions as solution_models
import api.serializers.solutions as solutions_serializers


class WorksheetGroupView(ModelViewSet):
    model = solution_models.WorksheetGroup
    serializer_class = solutions_serializers.WorksheetGroupSerializer
    queryset = model.objects.all()


class WorksheetAuthorView(ModelViewSet):
    model = solution_models.WorksheetAuthor
    serializer_class = solutions_serializers.WorksheetAuthorSerializer
    queryset = model.objects.all()


class WorksheetView(ModelViewSet):
    model = solution_models.Worksheet
    serializer_class = solutions_serializers.WorksheetAuthorSerializer
    queryset = model.objects.all()


class TaskView(ModelViewSet):
    model = solution_models.Task
    serializer_class = solutions_serializers.TaskSerializer
    queryset = model.objects.all()


class SolutionView(ModelViewSet):
    model = solution_models.Solution
    serializer_class = solutions_serializers.SolutionSerializer
    queryset = model.objects.all()
