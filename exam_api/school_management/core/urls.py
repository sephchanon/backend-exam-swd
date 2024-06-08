
# core/urls.py

from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, ClassroomViewSet, TeacherViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = router.urls
