from django.urls import path
from .views import internship_list

urlpatterns = [
    path('', internship_list, name='home'),
    path('internships/', internship_list, name='internships'),
]

from django.urls import path
from .views import internship_list, apply_internship

urlpatterns = [
    path('', internship_list),
    path('internships/', internship_list),
    path('apply/<int:internship_id>/', apply_internship),
]
