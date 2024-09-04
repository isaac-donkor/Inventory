from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('gold-calculator/', views.gold_calculator, name='gold_calculator'),
    path('send-email/', views.send_email, name='send_email')
]