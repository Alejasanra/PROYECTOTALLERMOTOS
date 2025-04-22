from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto, Categoria
from .forms import ProductoForm

class ProductoListView(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'productos/producto_list.html'
    ordering = ['-fecha_actualizacion']

class ProductoDetailView(DetailView):
    model = Producto
    context_object_name = 'producto'
    template_name = 'productos/producto_detail.html'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar Nuevo Producto'
        return context

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Producto'
        return context

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    context_object_name = 'producto'
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')
