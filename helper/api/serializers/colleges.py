from rest_framework import serializers
from api.models import colleges as college_models


class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = college_models.College
        fields = ['name', 'url', 'is_national', 'created',
                  'city', 'street', 'address'
                  ]


class CollegeDepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = college_models.CollegeDepartment
        fields = ['name', 'college']