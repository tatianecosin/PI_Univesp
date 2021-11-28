from django.urls import path
from .views import ListaClienteView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('', ListaClienteView.as_view(), name='cliente.index'),
    path('novo/', ClienteCreateView.as_view(), name='cliente.novo'),
    path('editar/<int:pk>', ClienteUpdateView.as_view(), name='cliente.editar'),
    path('remover/<int:pk>', ClienteDeleteView.as_view(), name='cliente.remover')
]