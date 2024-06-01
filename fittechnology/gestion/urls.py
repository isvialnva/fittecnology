from django.urls import path, include
from .views import (gestionindex, ListClasificacion, AddClasificacion, DeleteClasificacion, EditClasificacion,
                    ListDatosPersona, AddDatoPersona, EditDatoPersona, ListDatoPersonaCurso, EditDatoPersonaCurso)


urlpatterns = [
    path('gestion-index', gestionindex, name='gestion-index'),
    path('grados-list', ListClasificacion.as_view(), name='grados-list'),
    path('grados-add', AddClasificacion.as_view(), name='grados-add'),
    path('grados-del/<int:pk>/', DeleteClasificacion.as_view(), name='grados-del'),
    path('grados-edit/<int:pk>/', EditClasificacion.as_view(), name='grados-edit'),
    path('datopersona-detalle/', ListDatosPersona.as_view(), name='datopersona-detalle'),
    path('datopersona-add/', AddDatoPersona.as_view(), name='datopersona-add'),
    path('datopersona-edit/<int:pk>', EditDatoPersona.as_view(), name='datopersona-edit'),
    path('cursopersona-list/<int:id_clas>', ListDatoPersonaCurso.as_view(), name='cursopersona-list'),
    path('cursopersona-edit/<int:id_clas>/<int:pk>', EditDatoPersonaCurso.as_view(), name='cursopersona-edit'),
]
