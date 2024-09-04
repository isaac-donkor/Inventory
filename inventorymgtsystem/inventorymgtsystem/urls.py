from django.urls import path
from inventorymgtsystem.views import send_email, gold_calculator
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', gold_calculator, name='gold_calculator'),
    path('admin/', admin.site.urls),
    path('', include('SMENNS.urls')),
    path('send-email/', send_email, name='send_email')
    ]
