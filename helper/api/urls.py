from django.urls import path
from rest_framework.routers import DefaultRouter

import api.views.colleges as college_views

router = DefaultRouter()

router.register(r'college', college_views.CollegeView, basename="colleges")

urlpatterns = [
] + router.urls