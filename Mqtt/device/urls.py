from django.urls import path
from . import views

app_name = 'device'

urlpatterns = [
    path('device/<int:pk>/', views.DeviceView.as_view()),
]