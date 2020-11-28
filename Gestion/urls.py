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
    path('view_ing_producto/', ing_producto, name="ingProductos"),
    path('contratos/', crearContrato, name="contratos"),
    #path('/index}', menu, name="menu"),


#########panxo listado proveedores
    path('admproductores/', admproductores, name="admproductores"),
    path('usuarios/', listado_user, name="listado_user"),
    path('rproveedor/', rproveedor, name="rproveedor"),
    path('rcliente/', rcliente, name="rcliente"),


     path('feriacarro/', feriacarro, name="feriacarro"), 

#########panxo  


    path('transportista/', transportista, name="transportista"),
    path('stockexternos/', stockexternos, name="stockexternos"),
    path('comprando/', comprando, name="comprando"), 
    path('rcompra/', ingPedido, name="rcompra"),
]