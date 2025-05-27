from django.urls import path, include
#from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

from .view.lab_view import LabView
from .view.user_view import UserView
from .view.teacher_view import TeacherView
from .view.scheduled_view import ScheduledView
from .view.scheduled_for_lab import ScheduledForLabView
from .view.scheduled_for_teacher import ScheduledForTeacherView



router = DefaultRouter()
router.register(r'scheduled', ScheduledView, basename='scheduled') # Cria automaticamente GET, POST, PUT, DELETE
router.register(r'user', UserView,  basename='user') # Cria automaticamente GET, POST, PUT, DELETE
router.register(r'lab', LabView, basename="lab") # Cria automaticamente GET, POST, PUT, DELETE
router.register(r'teacher', TeacherView, basename="teacher") # Cria automaticamente GET, POST, PUT, DELETE

#scheduled_lab = routers.NestedDefaultRouter(router, r'lab', lookup='lab')
#scheduled_lab.register(r'scheduled', LabView, basename='lab-scheduled')

urlpatterns = [
    path('', include(router.urls)),
    path('lab/<int:id>/scheduled/', ScheduledForLabView.as_view()),
    path('teacher/<int:id>/scheduled/', ScheduledForTeacherView.as_view()),
]