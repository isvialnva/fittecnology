from django.urls import path, include
from .views import logout_view


urlpatterns = [
    path('session/', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name='logout'),
]
