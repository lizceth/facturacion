from django.contrib import admin
from facturaciones.models import Cliente, Factura, Producto, Detalle

class ClienteAdmin(admin.ModelAdmin):
    list_display=['ruc', 'razon_social','direccion']

class ProductoAdmin(admin.ModelAdmin):
    list_display=['codigo', 'nombre','precio_unit']

class FacturaAdmin(admin.ModelAdmin):
    list_display=['serie', 'numero','fecha','igv_total','total','subtotal']
    list_filter=['cliente']

class DetalleAdmin(admin.ModelAdmin):
    list_display=['cantidad', 'importe','igv','base_imponible']
    list_filter=['producto','registro']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Detalle, DetalleAdmin)
