from django.urls import path
from . import views

namespace = 'nota'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_nota, name='crear'),
    path('detalle-nota/<int:pk>/', views.detalle_nota, name='detalle'),
    path('editar-nota/<int:pk>/', views.editar_nota, name='editar'),
    path('eliminar-nota/<int:pk>/', views.eliminar_nota, name='eliminar'),
    path('toggle-favorito/<int:nota_id>/', views.add_favorito, name='toggle_favorito'),
    path('favoritos/', views.all_favoritos, name='all_favoritos'),
]
