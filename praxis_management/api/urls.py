from django.contrib import admin
from django.urls import path, include,re_path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users',views.UserViewSet,basename='users') #prefix should be api
router.register('doctors',views.DoctorViewSet,basename='doctors') #prefix should be api
router.register('nurses',views.NurseViewSet,basename='nurses')
router.register('patients',views.PatientViewSet,basename='patients')

urlpatterns = [
    path("", include(router.urls)),
]
