from django.urls import path
from .import views
urlpatterns = [
     path('',views.home),
     path('doctors',views.doctor),
     path('departments',views.department),
     path('appointment',views.appointment),
     path('aa/list',views.list),
     path('Date/<str:name>',views.DoctorDate),
]     