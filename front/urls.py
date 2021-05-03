from django.urls import path

from .views import (
    HomeView, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView,
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    AddAddressView, AddressDeleteView, CourseLinkView, CourseUnlinkView
)

app_name = 'front'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('course/', CourseListView.as_view(), name='course-list'),
    path('course/add/', CourseCreateView.as_view(), name='course-add'),
    path('course/edit/<int:pk>/', CourseUpdateView.as_view(), name='course-edit'),
    path('course/delete/<int:pk>/', CourseDeleteView.as_view(), name='course-delete'),
    path('student/', StudentListView.as_view(), name='student-list'),
    path('student/add/', StudentCreateView.as_view(), name='student-add'),
    path('student/edit/<int:pk>/', StudentUpdateView.as_view(), name='student-edit'),
    path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('address/add/<int:student_id>/', AddAddressView.as_view(), name='address-add'),
    path('address/delete/<int:pk>/<int:student_id>/', AddressDeleteView.as_view(), name='address-delete'),
    path('course/link/<int:student_id>/', CourseLinkView.as_view(), name='course-link'),
    path('course/unlink/<int:pk>/<int:student_id>/', CourseUnlinkView.as_view(), name='course-unlink'),
]