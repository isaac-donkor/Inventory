from django.urls import include,path

from . import views

urlpatterns = [
    
    path("", views.sales_view, name='sales_view'),
    path("", views.smenns, name='gold_calculator'),
    path("", views.send_email, name='send_email'),
    path('admin/', admin.site.urls),

    
]