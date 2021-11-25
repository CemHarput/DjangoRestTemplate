from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('plant-list/', views.PlantList, name="plant-list"),
    path('plant-detail/<str:pk>/', views.PlantDetail, name="plant-detail"),
    path('plant-create', views.PlantCreate, name="plant-create"),
    path('plant-update/<str:pk>', views.PlantUpdate, name="plant-update"),
    path('plant-delete/<str:pk>', views.PlantDelete, name="plant-delete"),

]
