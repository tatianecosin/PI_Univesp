from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import cliente


class ListaClienteView(ListView):
    model = cliente
    QuerySet = cliente.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
            
        return queryset