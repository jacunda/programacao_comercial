# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from veiculos.models import *

class VeiculosList(ListView):
   """
   View para listar veiculos cadastrados.
   """
   model = Veiculo
   template_name = 'veiculos/listar.html'

class VeiculosNew(CreateView):
    """
    View para criação de novos veiculos.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('listar-veiculos')
    
