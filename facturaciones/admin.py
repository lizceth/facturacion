from django.contrib import admin
from facturaciones.models import Cliente, Factura, Producto, Detalle

class ClienteAdmin(admin.ModelAdmin):
    list_display=['ruc', 'razon_social','direccion']

class ProductoAdmin(admin.ModelAdmin):
    list_display=['codigo', 'nombre','precio_unit','afecto']

class FacturaAdmin(admin.ModelAdmin):
    list_display=['serie', 'numero','cliente','fecha','subtotal','igv_total','total']
    list_filter=['cliente','usuario']

class DetalleAdmin(admin.ModelAdmin):
    list_display=['cantidad','igv','importe']
    list_filter=['factura','producto']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Detalle, DetalleAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Factura, FacturaAdmin)
