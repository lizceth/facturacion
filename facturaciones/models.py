from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    ruc=models.IntegerField(max_length=11)
    razon_social=models.CharField(max_length=100)
    direccion=models.CharField(max_length=200)
    def __unicode__(self):
        return U"%s-%s" %(self.ruc,self.razon_social)

class Producto(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    precio_unit=models.FloatField()
    afecto=models.BooleanField(default=False)


    def __unicode__(self):
        return U"%s"%self.nombre



class Factura(models.Model):
    serie=models.IntegerField(max_length=3)
    numero=models.CharField(max_length=6, unique=True)
    cliente=models.ForeignKey(Cliente)
    fecha=models.DateTimeField(auto_now_add=True)
    subtotal=models.FloatField()
    igv_total=models.FloatField()
    total=models.FloatField()
    usuario=models.ForeignKey(User)
    def __unicode__(self):
        return U" %s" %(self.numero)

class Detalle(models.Model):
    factura=models.ForeignKey(Factura)
    producto=models.ForeignKey(Producto)
    cantidad=models.IntegerField()
    importe=models.FloatField()
    igv=models.FloatField()

