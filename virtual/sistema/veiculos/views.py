# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render
class VeiculosList(View):
   """
   View para listar veiculos cadastrados.
   """
   def get(self, request):
      context = {
         'object_list': Veiculo.objects.all().order_by('marca')
      }
      return render(request, 'veiculos/listar.html', context)
