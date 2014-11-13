from django.shortcuts import render
from .models import Cliente, Producto, Factura, Detalle
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .forms import ClienteForm, ProductoForm, FacturaForm, DetalleForm

def factura(request):
    if request.method=='POST':
        formulario=FacturaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/imprimir')
    else:
        formulario=FacturaForm()
    return render_to_response('facturaciones/factura.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def clientes(request):
    clientes=Cliente.objects.all()
    return render(request, 'facturaciones/clientes.html',{'clientes':clientes})

def clienteAdd(request):
    if request.method=='POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/clientes')
    else:
        formulario=ClienteForm()
    return render_to_response('facturaciones/clienteAdd.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))
def clienteEdit (request, id):
        cliente_edit= Cliente.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ClienteForm(request.POST, instance = cliente_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/clientes")
        else:
            formulario = ClienteForm(instance= cliente_edit)
        return render_to_response('facturaciones/clienteEdit.html',
                    {'formulario': formulario},
                    context_instance = RequestContext(request))
def clienteDelete (request, id):
    cliente_delete = get_object_or_404(Cliente, pk=id)
    cliente_delete.delete()
    return HttpResponseRedirect("/clientes")

def productos(request):
    productos=Producto.objects.all()
    return render(request, 'facturaciones/productos.html',
                  {'productos':productos})

def productoAdd(request):
    if request.method=='POST':
        formulario=ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/productos')
    else:
        formulario=ProductoForm()
        return render_to_response('facturaciones/productoAdd.html',
                                  {'formulario':formulario},
                                  context_instance=RequestContext(request))

def productoEdit (request, id):
        producto_edit= Producto.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ProductoForm(request.POST, instance = producto_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/productos")
        else:
            formulario = ProductoForm(instance= producto_edit)
        return render_to_response('facturaciones/productoEdit.html',
                    {'formulario': formulario},
                    context_instance = RequestContext(request))

def productoDelete (request, id):
    producto_delete = get_object_or_404(Producto, pk=id)
    producto_delete.delete()
    return HttpResponseRedirect("/productos")

#================================================

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('usuarios/noactivo.html',
                                              context_instance=RequestContext(request))
            else:
                return render_to_response('usuarios/nousuario.html',
                                          context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('usuarios/ingresar.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('usuarios/privado.html',
                              {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')
