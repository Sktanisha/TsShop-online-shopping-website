from django.urls import path
from accountshop import views

urlpatterns = [
    path('', views.index, name="index"),
]