from django.urls import path
from Gestion.views import *
from django.contrib.auth import views as auth_views

from django.http import HttpResponseRedirect

# ,quienessomos, afterlogin       

urlpatterns = [
    path('', index, name="index"),
    path('login/', auth_views.LoginView.as_view(), name='login'),    
    path('login/menu/', menu, name="menu"),
    path('menu/', menu, name="menu"),
    path('usuarios/', ingUsuario, name="usuarios"),
    path('listar/', list_users, name="listar_user"),
    path('delete/user/<username>/', delete_user, name="delete_user"),
    path('usuarios/modificar/<username>/', modify_user, name="modify_user"),
    path('registrar_usuarios/', registrar_usuarios, name="registrar_usuarios"),
    path('view_admin/', vista_admin, name="vista_admin"),
    path('view_nuevo_pedido/', nuevo_pedido, name="nuevo_pedido"),
    path('ingresar/productos/<username>/', ingProductos, name="ingProductos"),
    path('contratos/', crearContrato, name="contratos"),
    path('contratos/eliminar/<id_contrato>', eliminarContratos, name="eliminarContratos"),
    path('contratos/modificar/<id_contrato>', modificarContratos, name="modificarContratos"),
    path('saldos/', publicarSaldos, name="saldos"),
    path('salditos/delete/<id_saldos>/', delete_saldos, name="delete_saldos"),
    path('salditos/modificar/<id_saldos>/', modify_saldos, name="modify_saldos"),
    path('menu/modificarDetalle/<id_pedido>', modificarPedido, name="modificarPedido"),
    path('nuevo_pedido/interno/<username>', nuevo_pedido_interno, name="nuevo_pedido_interno"),
    path('nuevo_pedido/interno/pedido_interno/<id_saldos>', comprarSaldoFruta, name="comprarSaldoFruta"),
    path('pagos/', pagos, name="pagos"),
    path('listar/pedidos/', listarPedido, name="listarPedido"),
    path('listar/pedidos/interno/', listarPedidoInterno, name="listarPedidoInterno"),
    path('listar/pedidos/externo/', listarPedidoExterno, name="listarPedidoExterno"),


#########panxo listado proveedores
    path('admproductores/', admproductores, name="admproductores"),
    path('usuarios/', listado_user, name="listado_user"),
    path('rproveedor/', rproveedor, name="rproveedor"),
    path('rcliente/', rcliente, name="rcliente"),
    path('solicitud/', solicitud, name="solicitud"),


     path('feriacarro/', feriacarro, name="feriacarro"), 

#########panxo  


    path('transportista/', transportista, name="transportista"),
    path('stockexternos/', stockexternos, name="stockexternos"),
    path('comprando/', comprando, name="comprando"), 
    path('rcompra/', ingPedido, name="rcompra"),
    path('rcompra_detalle/', rcompra_detalle, name="rcompra_detalle"),
]