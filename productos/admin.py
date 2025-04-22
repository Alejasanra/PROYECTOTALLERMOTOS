from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'precio', 'stock', 'fecha_actualizacion')
    list_filter = ('categoria', 'fecha_creacion')
    search_fields = ('nombre', 'codigo', 'descripcion')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'codigo', 'descripcion')
        }),
        ('Información de inventario', {
            'fields': ('precio', 'stock', 'categoria')
        }),
        ('Información de sistema', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
