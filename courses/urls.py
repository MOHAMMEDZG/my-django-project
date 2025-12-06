from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),#Page d'accueil
    path('course_level/<str:level>/', views.course_level, name='course_level'),  # Page d'accueil affichant les cours
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path("regional_exams/", views.regional_exams, name="regional_exams"),
    path("exercises_list/", views.exercises_list, name="exercises_list"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('instructor/add/', views.instructor_add_course, name='instructor_add_course'),
]
