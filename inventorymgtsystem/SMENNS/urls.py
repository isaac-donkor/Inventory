from django.urls import path

from . import views

urlpatterns = [
    
    path("gold_calculator/", views.gold_calculator, name='gold_calculator'),
    path('send_email/', views.send_email, name='send_email')
]