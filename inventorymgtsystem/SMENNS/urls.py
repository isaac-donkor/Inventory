from django.urls import path

from . import views

urlpatterns = [
    path('/', views.gold_calculator, name='gold_calculator'),
    path('send-email/', views.send_email, name='send_email')
]