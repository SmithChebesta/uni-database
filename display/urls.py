
from django.urls import path

from . import views
urlpatterns = [
    path('', views.tag, name='tag'),
    path('customer', views.customer, name='customer'),
    path('webapp', views.webapp, name='webapp'),
    path('service', views.service, name='service'),
    path('gateway', views.gateway, name='gateway')
]
