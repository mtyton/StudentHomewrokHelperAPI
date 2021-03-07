from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
import api.models.colleges as college_models
import api.serializers.colleges as college_serializers


class CollegeView(ReadOnlyModelViewSet):
    model = college_models.College
    serializer_class = college_serializers.CollegeSerializer
    queryset = model.objects.all()


class CollegeDepartmentView(ModelViewSet):
    model = college_models.CollegeDepartment
    serializer_class = college_serializers.CollegeDepartmentSerializer
    queryset = model.objects.all()


class DepartmentMajorView(ModelViewSet):
    model = college_models.DepartmentMajor
    serializer_class = college_serializers.DepartmentMajorSerializer
    queryset = model.objects.all()


class DegreeView(ModelViewSet):
    model = college_models.Degree
    serializer_class = college_serializers.DegreeSerializer
    queryset = model.objects.all()


class SemesterView(ModelViewSet):
    model = college_models.Semester
    serializer_class = college_serializers.SemesterSerializer
    queryset = model.objects.all()
