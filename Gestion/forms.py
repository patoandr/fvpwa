from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from Gestion.models import *
# Extendemos del original
class CustomUserForm(UserCreationForm):
    #### VALIDACION NOMBRE Y APELLIDO#####
    first_name = forms.CharField(min_length=4, max_length=20)
    last_name = forms.CharField(min_length=4, max_length=20)
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset = Group.objects.all(),required = True )

    #### VALIDAR USUARIO SI ESTA REGISTRADO #####
    def clean_username(self):
        username =self.cleaned_data["username"]
        existe = User.objects.filter(username__iexact=username).exists()
        
        if existe:
            raise ValidationError("Este usuario ya existe")
        return username

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2','group')   


class formProd(forms.ModelForm):
    ##### VALIDACION QUE INGRESEN MAYOR 1 Y MAXIMO 9999 ####
    kilos_producto = forms.IntegerField(min_value=10,max_value=1000)
    precio_producto = forms.IntegerField(min_value=10,max_value=100000)
    stock_producto = forms.IntegerField(min_value=10,max_value=100000)
    # fecha_ingreso = forms.DateField()
    # fecha_actualizada = forms.DateField()
    # fecha_ingreso = forms.DateField()
    # fecha_actualizada = forms.DateField()
    class Meta:
        model = Producto
        fields = {'id_producto','id_nombre','id_usuario','id_calidad','kilos_producto','precio_producto','stock_producto'}

class formUsuario(forms.ModelForm):
    id_pais = forms.ModelChoiceField(queryset = Pais.objects.all(),required = True)
    id_rol = forms.ModelChoiceField(queryset = Roles.objects.all(),required = True)
        #### VALIDAR USUARIO SI ESTA REGISTRADO #####
    def clean_username(self):
        username =self.cleaned_data["username"]
        existe = Usuario.objects.filter(username__iexact=username).exists()
        
        if existe:
            raise ValidationError("Este usuario ya existe")
        return username
        
    class Meta:
        model = Usuario
        fields = {'id_usuario','rut_usuario','ap_paterno','nombres','id_pais','email','id_rol','username','contrasena'}
    
class formcontrato(forms.ModelForm):
    fecha_termino = forms.DateField()
    class Meta:
        model = Contratos
        fields = {'id_contrato','id_usuario','fecha_inicio','fecha_termino'}

class formcamion(forms.ModelForm):
    
    class Meta:
        model = Camion
        fields = {'id_camion','id_usuario','nombre','descripcion','tamano','capacidad_carga','patente'}

class formPedido(forms.ModelForm):
    fecha_pedido = forms.DateField()
    class Meta:
        model = Pedido
        fields = {'id_pedido','id_usuario','fecha_pedido','fecha_envio','fecha_entrega','nombre_destinatario','id_pais','ciudad_destinatario','direccion_destinatario','fono_destinatario','id_camion','estado_pedido'}