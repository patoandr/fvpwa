# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calidad(models.Model):
    id_calidad = models.BigAutoField(primary_key=True)
    nombre_calidad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'calidad'
    
    def __str__(self):
        return self.nombre_calidad


class Camion(models.Model):
    id_camion = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    tamano = models.CharField(max_length=100)
    capacidad_carga = models.CharField(max_length=100)
    patente = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'camion'

    def __str__(self):
        return self.patente


class Claves(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_origen = models.BigIntegerField()
    tabla_origen = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'claves'


class Contratos(models.Model):
    id_contrato = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratos'

    def __str__(self):
        return self.id_usuario

    

class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    id_pedido = models.OneToOneField('Pedido', models.DO_NOTHING, db_column='id_pedido')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_tipo_detalle_pedido = models.ForeignKey('TipoDetallePedido', models.DO_NOTHING, db_column='id_tipo_detalle_pedido')
    precio_unidad = models.BigIntegerField(blank=True, null=True)
    kilos = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_pedido'

class TipoDetallePedido(models.Model):
    id_tipo_detalle_pedido = models.BigAutoField(primary_key=True)
    tipo_descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_detalle_pedido'
    
    def __str__(self):
        return self.tipo_descripcion

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Error(models.Model):
    id_error = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    tipo_error = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'error'


class Estados(models.Model):
    estado_pedido = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estados'
        
    def __str__(self):
        return self.descripcion


class Nombre(models.Model):
    id_nombre = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'nombre'

    def __str__(self):
        return self.descripcion


class Pais(models.Model):
    id_pais = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pais'

    def __str__(self):
        return self.descripcion


class Pedido(models.Model):
    id_pedido = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fecha_pedido = models.DateField()
    fecha_envio = models.DateField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    nombre_destinatario = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pais')
    ciudad_destinatario = models.CharField(max_length=100, blank=True, null=True)
    direccion_destinatario = models.CharField(max_length=100)
    fono_destinatario = models.BigIntegerField()
    id_camion = models.ForeignKey(Camion, models.DO_NOTHING, db_column='id_camion')
    estado_pedido = models.ForeignKey(Estados, models.DO_NOTHING, db_column='estado_pedido')

    class Meta:
        managed = False
        db_table = 'pedido'

    # if fecha_entrega is None:
    #     print("It doesn't match.")

import datetime
class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    id_nombre = models.ForeignKey(Nombre, models.DO_NOTHING, db_column='id_nombre')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_calidad = models.ForeignKey(Calidad, models.DO_NOTHING, db_column='id_calidad')
    kilos_producto = models.BigIntegerField()
    precio_producto = models.BigIntegerField()
    stock_producto = models.BigIntegerField()
    fecha_ingreso = models.DateField(default=datetime.datetime.now())
    fecha_actualizada = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

    # def __str__(self):
    #     return self.id_nombre


class Region(models.Model):
    id_region = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'region'


class Roles(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'roles'
    def __str__(self):
        return self.descripcion

import datetime
class Saldos(models.Model):
    id_saldos = models.BigAutoField(primary_key=True)
    montos_saldos = models.BigIntegerField(blank=True, null=True)
    id_nombre = models.ForeignKey(Nombre, models.DO_NOTHING, db_column='id_nombre')#nombre fruta
    precio_fruta = models.BigIntegerField(blank=True, null=True)
    fecha_publicacion = models.DateField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'saldos'



class SaldosDetalle(models.Model):
    id_saldo_detalle = models.AutoField(primary_key=True)
    id_saldos = models.BigIntegerField(blank=True, null=True)
    id_pedido = models.BigIntegerField(blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)    
    total = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saldos_detalle'


class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    rut_usuario = models.CharField(max_length=10)
    ap_paterno = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pais')
    fono = models.BigIntegerField()
    email = models.CharField(max_length=100)
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol')
    username = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.username