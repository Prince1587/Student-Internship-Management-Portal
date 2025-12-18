from django.urls import path
from .views import internship_list
from . import views

urlpatterns = [
    path('', internship_list, name='home'),
    path('internships/', internship_list, name='internships'),
]

from django.urls import path
from .views import internship_list, apply_internship

urlpatterns = [
    path('', views.internship_list, name='internship_list'),
    path('apply/<int:internship_id>/', views.apply_internship, name='apply_internship'),
    path('success/', views.application_success, name='application_success'),
]
