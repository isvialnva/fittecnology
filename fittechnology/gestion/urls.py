from django.urls import path, include
from .views import GestionIndex


urlpatterns = [
    path('gestion-index', GestionIndex.as_view(), name='gestion-index'),
]
