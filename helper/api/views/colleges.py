from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
import api.models.colleges as college_models
import api.serializers.colleges as college_serializers


# Create your views here.
class CollegeView(ReadOnlyModelViewSet):
    model = college_models.College
    serializer_class = college_serializers.CollegeSerializer
    queryset = model.objects.all()

