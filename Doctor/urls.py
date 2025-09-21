from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='list'),
    path('create/', views.create_doctor, name='create'),
    path('update/<int:pk>/', views.update_doctor, name='update'),
    path('delete/<int:pk>/', views.delete_doctor, name='delete'),
]

    
