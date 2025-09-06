from django.urls import path
from . import views

namespace = 'nota'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_nota, name='crear'),
    path('detalle-nota/<int:pk>/', views.detalle_nota, name='detalle'),
]
