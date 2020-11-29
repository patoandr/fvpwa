from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Gestion.forms import *
from Gestion.models import  *
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
import os
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password


#########panxo
from django.db import connection
import cx_Oracle
#########panxo

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')    

@login_required
def menu(request):
    listarPedido = Pedido.objects.all()
    listarPedido = Pedido.objects.filter(estado_pedido = 1)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(listarPedido,5)
        listarPedido = paginator.page(page)
    except:
        raise Http404
    variables={
        'entity' : listarPedido,
        'paginator': paginator
    }

    return render(request,'menu.html', variables )

####################   INICIO  CRUD USUARIO ####################
@login_required
def ingUsuario(request):
    form = formUsuario()
    pais = Pais.objects.all()
    rol = Roles.objects.all()
    usuario = Usuario.objects.all()
    print(form)
    if request.method == 'POST':
        print('Se genera el post')
        form = formUsuario(request.POST)
        print('Entro aqui')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.contrasena = make_password(request.POST.get('contrasena'))
            nombre = request.POST.get('username')
            email = request.POST.get('email')
            passw = request.POST.get('contrasena')
            user = User.objects.create_user(nombre,email,passw)
            user.save()
            value = form.cleaned_data['id_rol']
            g = Group.objects.get(name=value)
            g.user_set.add(User.objects.last())
            print("1")
            instance.save()  
            messages.success(request,"Usuario Creado Correctamente")
        else:
           messages.error(request,"No se ha podido crear usuario, Favor revisar datos")        
    #users=Usuario.objects.all()
    return render (request, 'usuarios.html',{'form':form,'pais':pais,'rol':rol, 'usuario':usuario})
# def register(request):
#     #mensaje=""
#     group = Group.objects.all()
#     if request.method == 'POST':
#         print("se genera el post")
#         form = CustomUserForm(request.POST)
#         if form.is_valid():
#             print("1")
#             form.save()
#             value = form.cleaned_data['group']
#             g = Group.objects.get(name=value)
#             g.user_set.add(User.objects.last())
#             #mensaje = "Usuario Creado correctamente"
#             messages.success(request,"Usuario Creado Correctamente")
#         else:
#             #mensaje = "Hubo un error"
#             messages.error(request,"No se ha podido crear usuario, Favor revisar datos")

#     users=AuthUser.objects.all()
#     return render(request, 'usuarios.html', {'group':group, 'users': users})   

@login_required
def list_users(request):
    users=AuthUser.objects.all()
    return render(request, "usuarios.html", {'users': users})

@login_required
def delete_user(request, username):
    print("Este es el usuario: "+username)
    #buscar el usuario a eliminar

    # g = Usuario.objects.get(id_usuario=str(id))     
    # g.delete()
    # print("Usuario:" +str(g))  
    # g = AuthUserGroups.objects.get(username=str(username))     
    # g.delete()
    userDJ=AuthUser.objects.get(username=username)
    print(userDJ.username)
    foranea = AuthUserGroups.objects.get(user=userDJ.pk)    
    foranea.delete()
    userDJ.delete()
    users=Usuario.objects.get(username=(username))
    users.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect ('usuarios')


def modify_user(request,username):
    #buscar el usuario para luego modificar
    users = Usuario.objects.get(username=username)
    usersDJ = AuthUser.objects.get(username=username)
    group = Roles.objects.all()
    groupDJ = Group.objects.all()
    pais = Pais.objects.all()
    variables = {
        'usuario':users,
        'usuarioDJ':usersDJ,
        'group':group,
        'groupDJ':groupDJ,
        'pais':pais,
    }
    if request.POST:
        # usuario = usuario()
        users.rut_usuario = request.POST.get('rut_usuario')
        users.ap_paterno = request.POST.get('ap_paterno')
        users.ap_materno = request.POST.get('ap_materno')
        users.nombres = request.POST.get('nombres')
        users.direccion = request.POST.get('direccion')
        #users.id_pais = request.POST.get('id_pais')
        users.fono = request.POST.get('fono')
        users.email = request.POST.get('email')
        #users.id_rol = request.POST.get('id_rol')
        users.username = request.POST.get('username')
        usersDJ.username = request.POST.get('username')
        users.contrasena = make_password(request.POST.get('contrasena'))

        u = User.objects.get(username=users.username)
        ncontra = request.POST.get('contrasena')
        u.set_password(ncontra)
        

        # value = request.POST.get('group')
        # value = request.POST.get('pais')
        # p = Pais.objects.get(name=value)
        # p.user_set.add(Usuario.objects.last())
        pais.id_pais = request.POST.get('id_pais')
        # g = Group.objects.get(name=value)
        # g.user_set.add(Usuario.objects.last())
        group.id_rol = request.POST.get('g.id_rol')
        groupDJ.id = request.POST.get('g.id')

        try:
            usersDJ.save()
            users.save()
            u.save()
            messages.success(request, 'Datos modificados correctamente')
        
        except:
            messages.error(request, 'No se ha podido modificar ')

        return redirect('usuarios')
        
    return render(request, 'registrar_usuarios.html',variables)
    # return render(request, 'usuarios.html', {'group':group,'usuario': users})   
#########################  FIN CRUD USUARIOS ##################################

######################### INICIO CRUD REGISTRAR USUARIOS PARA VISTAS #############################

def registrar_usuarios(request):
    group = Group.objects.all()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            value = form.cleaned_data['group']
            g = Group.objects.get(name=value)
            g.user_set.add(User.objects.last())

    users=AuthUser.objects.all()
    return render(request, 'registrar_usuarios.html', {'group':group, 'users': users})

######################### FIN CRUD REGISTRAR USUARIOS PARA VISTAS #############################


def vista_admin(request):

    return render (request, 'views/view_admin.html')






######################### INICIO CRUD CLIENTE INTERNO PEDIDO ############################

def nuevo_pedido(request):

    return render (request, 'views/view_cliente_interno.html')

#agregue yo


 #########panxo  listado proveedores
def admproductores(request):
    data = {
        'proveedores':listado_proveedores()
    }
    return render(request, 'admproductores.html',data)

def listado_proveedores():
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    out_cur = djang_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROVEEDORES",  [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

@login_required
def ingProductos(request, username):
    print("Este es el usuario: "+username)
    form = formProd()
    proveedor = Usuario.objects.get(username=username)
    nombre = Nombre.objects.all()
    print(proveedor.id_usuario)
    producto = Producto.objects.filter(id_usuario=proveedor.id_usuario)
    calidad = Calidad.objects.all()
    if request.method == 'POST':
        print("se genera el post")
        form = formProd(request.POST)
        print("Entro aqui")
        # print(form)
        if form.is_valid():
            print("1")
            form.save()
            messages.success(request, 'Producto ingresado correctamente')

        #return redirect('ingProductos')


    return render (request, 'ingProductos.html',{'form':form,'proveedor':proveedor,'producto':producto,'calidad':calidad,'nombre':nombre})
 #########panxo


 
 #########panxo  listado usuarios

def listado_user(request):
    data = {
        'mostrarusua':listado_usuarios()
    }
    return render(request, 'usuarios.html',data)

def listado_usuarios():
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    out_cur = djang_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_USERNAME",  [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista
 #########panxo

##listar regiones  y registrar proveedores
def rproveedor(request):
    data = {
        'mostrarr':listado_region(),
        'verid':listado_idp()
    }

    if request.method == 'POST':
        idproveedor = request.POST.get('idproveedor')
        rut = request.POST.get('rut')
        appaterno = request.POST.get('appaterno')
        apmaterno = request.POST.get('apmaterno')
        nombres = request.POST.get('nombres')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        region = request.POST.get('region')
        salida = agregar_proveedor(idproveedor,rut,appaterno,apmaterno,nombres,direccion,telefono,correo,region)

        if salida == 1:
            data ['mensaje'] = 'Agregado correctamente'
        else:
            data ['mensaje'] = 'No se ha podido guadar'

    return render(request, 'rproveedor.html',data)

## mostrar regiones
def listado_region():
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    out_cur = djang_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_REGIONES",  [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

##el mas grande de los proveedores+1
def listado_idp():
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    out_cur = djang_cursor.connection.cursor()

    cursor.callproc("SP_ID_PROVEEDOR",  [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


   ##agregar proveedor
def agregar_proveedor(idproveedor,rut,appaterno,apmaterno,nombres,direccion,telefono,correo,region):
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    salida =cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PROVEEDOR', [idproveedor,rut,appaterno,apmaterno,nombres,direccion,telefono,correo,region, salida])
    return salida.getvalue()




##########VISTA de contratos
def crearContrato(request):
    form = formcontrato()
    proveedor = Usuario.objects.filter(id_rol=2)
    contratos = Contratos.objects.all()
    print(form)
    if request.method == 'POST':
        print('Se genera el post')
        form = formcontrato(request.POST)
        print('Entro aqui')
        if form.is_valid():
            print("1")
            form.save()

    return render (request, 'contratos.html',{'form':form,'proveedor':proveedor, 'contratos':contratos})

def modificarContratos(request,id_contrato):
    #buscar el contrato para luego modificar
    contrato = Contratos.objects.get(id_contrato=id_contrato)
    proveedor = Usuario.objects.filter(id_rol=2)
    
    variables = {
        # 'form': formcontrato(instance=contrato),
        'contrato':contrato,
        'proveedor':proveedor,
    }
    if request.POST:
        # contrato.id_contrato = request.POST.get('id_contrato')
        contrato.fecha_inicio = request.POST.get('fecha_inicio')
        contrato.fecha_termino = request.POST.get('fecha_termino')

        try:
            contrato.save()
            messages.success(request, 'Datos actualizados correctamente')
            return redirect('contratos')
        
        except:
            messages.error(request, 'No se ha podido actualizar ')

        return redirect('contratos')
        
    return render(request, 'contratos_modificar.html',variables)

@login_required
def eliminarContratos(request, id_contrato):
    contratos=Contratos.objects.get(id_contrato=id_contrato) 
    contratos.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect ('contratos')

########### CRUD TRANSPORTISTA ##################

def transportista(request):
    form = formcamion()
    usuario = Usuario.objects.filter(id_rol=6)
    camion = Camion.objects.all()
    print(form)
    if request.method == 'POST':
        print("se genera el post")
        form = formcamion(request.POST)
        print("Entro aqui")
        # print(form)
        if form.is_valid():
            print("1")
            form.save()
            messages.success(request, 'camion ingresado correctamente')
        else:
           messages.error(request,"No se ha podido ingresar camión, Favor revisar datos")

    return render (request, 'views/view_transportista.html',{'form':form,'usuario':usuario,'camion':camion})

def ingPedido(request):
    form = formPedido()
    usuario = Usuario.objects.filter(id_rol=4)
    camion = Camion.objects.all()
    pais = Pais.objects.all()
    # pedido = Pedido.objects.get(id_pedido=id_pedido)
    # pedido = Pedido.objects.all()
    print(form)
    if request.method == 'POST':
        print("se genera el post")
        form = formPedido(request.POST)
        print("Entro aqui")
        # print(form)
        if form.is_valid():
            print("1")
            form.save()
            messages.success(request, 'Pedido ingresado correctamente')
            return redirect('rcompra_detalle')
        else:
           messages.error(request,"No se ha podido ingresar pedido, Favor revisar datos")  

        #return redirect('ingProductos')

    return render (request, 'rcompra.html',{'form':form,'usuario':usuario,'camion':camion,'pais':pais})    

def rcompra_detalle(request):
    form = formrcompra_detalle()
    detalle_pedido = DetallePedido.objects.all()
    producto = Producto.objects.all()
    pedido = Pedido.objects.all()
    print(form)
    if request.method == 'POST':
        print("se genera el post")
        form = formrcompra_detalle(request.POST)
        print("Entro Aqui")
        if form.is_valid():
            print("1")
            form.save()
            messages.success(request, 'Detalle ingresado correctamente')
        else:
           messages.error(request,"No se ha podido ingresar el detalle de tu compra, Favor revisar datos")              
    return render (request, 'rcompra_detalle.html',{'form':form, 'detalle_pedido':detalle_pedido, 'producto':producto, 'pedido':pedido})

##envio de correo solicitud de compra
def feriacarro(request):
    usuario = Usuario.objects.all()
    if request.method =="POST":   
       subject = request.POST["cliente"]
       message = request.POST["pedido"] + " solicitado para el correo " + request.POST["correo"]
       email_from = settings.EMAIL_HOST_USER
       recipient_list=["virtual.feriavirtual2020@gmail.com"]
       send_mail(subject, message, email_from, recipient_list)

    return render(request, 'feriacarro.html',{'usuario':usuario})
    


def comprando(request):
     return render(request, 'comprando.html', {})

##Ver Stock Disponible para validadr por correo
def stockexternos(request):
    data = {
        'stockexternos':listado_stocke()
    }
    return render(request, 'stockexternos.html',data)

def listado_stocke():
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    out_cur = djang_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_STOCKE",  [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista
##Ver Stock Disponible para validadr por correo


##ingresar compra cliente externo
# def rcompra(request):
#     pais = Pais.objects.all()
#     if request.method == 'POST':
#         Id_usuario = request.POST.get('Id_usuario')
#         fpedido = request.POST.get('fpedido')
#         ndestinatario = request.POST.get('ndestinatario')
#         pais = request.POST.get('pais')
#         ciudad = request.POST.get('ciudad')
#         direccion = request.POST.get('direccion')
#         telefono = request.POST.get('telefono')
#         camionero = request.POST.get('camionero')
#         epedido = request.POST.get('epedido')
#         salida = agregar_pedidoex(Id_usuario,fpedido,ndestinatario,pais,ciudad,direccion,telefono,camionero,epedido)

#         if salida == 1:
#             'Agregado correctamente'
#         else:
#             'No se ha podido guadar'

#     return render(request, 'rcompra.html',{'pais':pais})


##ingresar compra cliente externo
def agregar_pedidoex(Id_usuario,fpedido,ndestinatario,pais,ciudad,direccion,telefono,camionero,epedido):
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    salida =cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PEDIDOEX', [Id_usuario,fpedido,ndestinatario,pais,ciudad,direccion,telefono,camionero,epedido,salida])
    return salida.getvalue()


@login_required
def publicarSaldos(request):
    form = formSaldos()
    saldos = Saldos.objects.all()
    frutas = Nombre.objects.all()
    print(form)
    if request.method == 'POST':
        print('Se genera el post')
        form = formSaldos(request.POST)
        print('Entro aqui')
        if form.is_valid():
            print("1")
            form.save()

    return render (request, 'saldos.html',{'form':form,'saldos':saldos, 'frutas':frutas})

@login_required
def delete_saldos(request, id_saldos):
    saldos=Saldos.objects.get(id_saldos=id_saldos)   
    saldos.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect ('saldos')

def modify_saldos(request,id_saldos):
    #buscar el saldo para luego modificar
    saldo = Saldos.objects.get(id_saldos=id_saldos)   
    variables = {
        'saldo':saldo,
    }
    if request.POST:
        saldo.montos_saldos = request.POST.get('montos_saldos') 
        # saldo.fecha_publicacion = request.POST.get('fecha_publicacion')

        try:
            saldo.save()            
            messages.success(request, 'Montos Actualizados correctamente')
        
        except:
            messages.error(request, 'No se ha podido modificar ')

        return redirect('saldos')   
    return render(request, 'saldos_modificar.html',variables)

def modificarPedido(request,id_pedido):
    listarPedido = Pedido.objects.get(id_pedido=id_pedido)
    estado = Estados.objects.all()
    variables = {
        'lp': listarPedido,
        'estado': estado,
    }
    if request.POST:
        listarPedido.fono_destinatario = request.POST.get('fono_destinatario')
        listarPedido.ciudad_destinatario = request.POST.get('ciudad_destinatario')
        listarPedido.direccion_destinatario = request.POST.get('direccion_destinatario')
        #listarPedido.fecha_pedido = request.POST.get('fecha_pedido')
        listarPedido.fecha_envio = request.POST.get('fecha_envio')
        listarPedido.fecha_entrega = request.POST.get('fecha_entrega')
        #var = listarPedido.estado_pedido = request.POST.get('estado_pedido')
        var = request.POST.get('estado_pedido')
        #print(var)
        listarPedido.estado_pedido = Estados.objects.get(estado_pedido=var)
        try:
            listarPedido.save()
            messages.success(request, 'Datos actualizados correctamente')
        except:
            messages.error(request, 'No se ha podido actualizar ')
        return redirect('menu')
    return  render(request, 'pedido_modificar.html', variables)

def nuevo_pedido_interno(request,username):
    #__lte es mejor que y __gte es mayor que!!!!
    saldo = Saldos.objects.filter(montos_saldos__lte = 10000)
    form = formPedido()
    print(username)

    cliente = Usuario.objects.get(username=username)
    camion = Camion.objects.all()
    pais = Pais.objects.all()
    variables = {
        'saldo':saldo,
        'cliente':cliente,
        'camion': camion,
        'pais':pais,
        'fomr':form
    }
    print(form)
    if request.method == 'POST':
        print("se genera el post")
        form = formPedido(request.POST)
        print("Entro aqui")
        # print(form)
        if form.is_valid():
            print("1")
            form.save()

            messages.success(request, 'Pedido ingresado correctamente')            
        else:
           messages.error(request,"No se ha podido ingresar pedido, Favor revisar datos")   
        
    return  render(request, 'listar_pedido_interno.html', variables)


def comprarSaldoFruta(request, id_saldos):
    form = formsaldo_detalle()
    saldosDetalle = SaldosDetalle.objects.all()
    saldoAll = Saldos.objects.get(id_saldos=id_saldos)
    saldo = Saldos.objects.all()
    pedido = Pedido.objects.last()
    primero = request.POST.get('stock_fruta')#montos saldo
    segundo = request.POST.get('cantidad')
    tercero = request.POST.get('precio_fruta')#precio de la fruta
    # segundo2 = request.POST.get('cantidad')
    print(form)
    if request.method == 'POST':
        print("se genera el post")
        form = formsaldo_detalle(request.POST)
        print("Entro Aqui")
        if form.is_valid():
            print("1")
            resultado = (int(primero) - int(segundo))
            precio_total = (int(segundo) * int(tercero))
            saldoAll.montos_saldos = resultado
            saldosDetalle.total = precio_total
            form.save()
            saldoAll.save()
            messages.success(request, 'Detalle ingresado correctamente')
        else:
           messages.error(request,"No se ha podido ingresar el detalle de tu compra, Favor revisar datos")              
    return render (request, 'agregar_pedido_interno.html',{'form':form, 'saldo':saldo, 'saldoAll':saldoAll,'pedido':pedido,'saldosDetalle':saldosDetalle})

def pagos(request):
     return render(request, 'pagos.html', {})

def listarPedido(request):    
    usuario = Usuario.objects.filter(id_rol=3)
    
    
    listarPedido = Pedido.objects.all()
        #meter el usuario que esta solicitando
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(listarPedido,5)
        listarPedido = paginator.page(page)
    except:
        raise Http404
    variables={
        'entity' : listarPedido,
        'paginator': paginator,
        'usuario':usuario
    }

    return render(request,'reporte_interno.html', variables )


def listarPedidoInterno(request):    
    usuario = Usuario.objects.filter(id_rol=3)        
    listarPedido = Pedido.objects.all()
    username = ""
    if request.POST.get('username'):
        username = str(request.POST.get('username'))
        u = Usuario.objects.get(username=username)
        print(u.id_usuario)
        listarPedido = Pedido.objects.filter(id_usuario=u.id_usuario)    
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listarPedido,10)
        listarPedido = paginator.page(page)
    except:
        raise Http404    
    variables={
        'entity' : listarPedido,
        'paginator': paginator,
        'usuario':usuario,
        'username': username
    }

    return render(request,'reporte_interno.html', variables )

def listarPedidoExterno(request):    
    usuario = Usuario.objects.filter(id_rol=4)        
    listarPedido = Pedido.objects.all()
    username = ""
    if request.POST.get('username'):
        username = str(request.POST.get('username'))
        u = Usuario.objects.get(username=username)
        print(u.id_usuario)
        listarPedido = Pedido.objects.filter(id_usuario=u.id_usuario)    
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listarPedido,10)
        listarPedido = paginator.page(page)
    except:
        raise Http404    
    variables={
        'entity' : listarPedido,
        'paginator': paginator,
        'usuario':usuario,
        'username': username
    }

    return render(request,'reporte_externo.html', variables )





def solicitud(request):
    usuario = Usuario.objects.all()
    if request.method =="POST":   
       subject =["Nuevo registro"]
       message ="Para el Rut: " +  request.POST["rut"]  +'\n' +  "Apellido Paterno: " + request.POST["appaterno"] +'\n' + "Apellido Materno "  + request.POST["apmaterno"] +'\n' +  "Nombre usuario: " + request.POST["nombres"] +'\n' +  "Con Direccion en: " + request.POST["direccion"] +'\n' +   "Con numero telefonico:  " + request.POST["telefono"] +'\n' +  "Solicitado para el correo: " + request.POST["correo"] +'\n' +  "Con nombre de usuario: " + request.POST["usuario"]+'\n' +  "Con contraseña solicitada: " + request.POST["contrasena"] +'\n' +  "Del pais: " + request.POST["pais"] +'\n' +  "Para el Rol solicitado de: " + request.POST["id_rol"]
       email_from = settings.EMAIL_HOST_USER
       recipient_list=["virtual.feriavirtual2020@gmail.com"]
       send_mail(subject, message, email_from, recipient_list)

    return render(request, 'solicitud_registro.html',{'usuario':usuario,'mostrarr':listado_pais,'mostrarrol':listado_rol})
    

##Listado de los roles.
def listado_rol():
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    out_cur = djang_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_ROLES",  [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

## mostrar paises
def listado_pais():
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    out_cur = djang_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PAISES",  [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

##listar PAIS  y registrar CLIENTES
def rcliente(request):
    data = {
        'mostrarr':listado_pais(),
        'mostrarrol':listado_rol()
    }

    if request.method == 'POST':
        rut = request.POST.get('rut')
        appaterno = request.POST.get('appaterno')
        apmaterno = request.POST.get('apmaterno')
        nombres = request.POST.get('nombres')
        direccion = request.POST.get('direccion')
        pais = request.POST.get('pais')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        id_rol = request.POST.get('id_rol')
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        salida = agregar_cliente(rut,appaterno,apmaterno,nombres,direccion,pais,telefono,correo,id_rol,usuario,contrasena)

        if salida == 1:
            data ['mensaje'] = 'Agregado correctamente'
        else:
            data ['mensaje'] = 'No se ha podido guadar'

    return render(request, 'rcliente.html',data)


##agregar cliente
def agregar_cliente(rut,appaterno,apmaterno,nombres,direccion,pais,telefono,correo,id_rol,usuario,contrasena):
    djang_cursor = connection.cursor()
    cursor = djang_cursor.connection.cursor()
    salida =cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CLIENTE', [rut,appaterno,apmaterno,nombres,direccion,pais,telefono,correo,id_rol,usuario,contrasena, salida])
    return salida.getvalue()