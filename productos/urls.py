from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='producto-list'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/nuevo/', views.ProductoCreateView.as_view(), name='producto-create'),
    path('producto/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto-update'),
    path('producto/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto-delete'),
]