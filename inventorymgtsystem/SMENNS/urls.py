from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.smenns, name='gold_calculator'),
    path("",views.gold_calculator,name='god_calculator'),
    path("", views.send_email, name='send_email'),
    
]