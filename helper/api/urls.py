from django.urls import path
from rest_framework.routers import DefaultRouter

import api.views.colleges as college_views
import api.views.solutions as solutions_views

router = DefaultRouter()

# college views urls
router.register(r'college', college_views.CollegeView, basename="colleges")
router.register(r'department', college_views.CollegeDepartmentView, basename="departments")
router.register(r'major', college_views.DepartmentMajorView, basename="majors")
router.register(r'degree', college_views.DegreeView, basename="degrees")
router.register(r'semester', college_views.SemesterView, basename="semesters")

#solution views urls
router.register(r'worksheet-group', solutions_views.WorksheetGroupView, basename="worksheetgroups")
router.register(r'worksheet-author', solutions_views.WorksheetAuthorView, basename="worksheetauthors")
router.register(r'worksheet', solutions_views.WorksheetView, basename="worksheets")
router.register(r'task', solutions_views.TaskView, basename="tasks")
router.register(r'solution', solutions_views.SolutionView, basename="solutions")

urlpatterns = [
] + router.urls