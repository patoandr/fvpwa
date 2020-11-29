DROP TABLE calidad CASCADE CONSTRAINTS;

DROP TABLE claves CASCADE CONSTRAINTS;

DROP TABLE usuario CASCADE CONSTRAINTS;

DROP TABLE contratos CASCADE CONSTRAINTS;

DROP TABLE detalle_pedido CASCADE CONSTRAINTS;

DROP TABLE error CASCADE CONSTRAINTS;

DROP TABLE estados CASCADE CONSTRAINTS;

DROP TABLE nombre CASCADE CONSTRAINTS;

DROP TABLE pais CASCADE CONSTRAINTS;

DROP TABLE pedido CASCADE CONSTRAINTS;

DROP TABLE producto CASCADE CONSTRAINTS;

DROP TABLE region CASCADE CONSTRAINTS;

DROP TABLE roles CASCADE CONSTRAINTS;

DROP TABLE camion CASCADE CONSTRAINTS;

DROP TABLE saldos CASCADE CONSTRAINTS;

DROP TABLE saldos_detalle CASCADE CONSTRAINTS;

CREATE TABLE calidad (
    id_calidad       INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    nombre_calidad   VARCHAR2(100) NOT NULL,
    descripcion      VARCHAR2(100) NOT NULL
);

ALTER TABLE calidad ADD CONSTRAINT calidad_pk PRIMARY KEY ( id_calidad );

CREATE TABLE claves (
    id             INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    id_origen      INTEGER NOT NULL,
    tabla_origen   VARCHAR2(20) NOT NULL,
    nombre         VARCHAR2(100) NOT NULL,
    clave          VARCHAR2(10) NOT NULL
);

ALTER TABLE claves ADD CONSTRAINT claves_pk PRIMARY KEY ( id );

CREATE TABLE usuario (
    id_usuario    INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    rut_usuario   VARCHAR2(10) NOT NULL,
    ap_paterno    VARCHAR2(100) NOT NULL,
    ap_materno    VARCHAR2(100) NOT NULL,
    nombres       VARCHAR2(100) NOT NULL,
    direccion     VARCHAR2(200) NOT NULL,
    id_pais       INTEGER NOT NULL,
    fono          INTEGER NOT NULL,
    email         VARCHAR2(100) NOT NULL,
    id_rol        INTEGER NOT NULL,
    username      VARCHAR2(100) NOT NULL,
    contrasena    varchar2(100) not null
);

ALTER TABLE usuario ADD CONSTRAINT usuario_pk PRIMARY KEY ( id_usuario );

CREATE TABLE contratos (
    id_contrato     INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    id_usuario    INTEGER NOT NULL,
    fecha_inicio    DATE NOT NULL,
    fecha_termino   DATE
);

ALTER TABLE contratos ADD CONSTRAINT contratos_pk PRIMARY KEY ( id_contrato );

CREATE TABLE detalle_pedido (
    id_detalle_pedido       INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    id_pedido     INTEGER NOT NULL,
    id_producto     INTEGER NOT NULL,
    precio_unidad   INTEGER,
    kilos           INTEGER,
    total           INTEGER
);

ALTER TABLE detalle_pedido ADD CONSTRAINT detalle_pedido_pk PRIMARY KEY ( id_detalle_pedido );

CREATE TABLE error (
    id_error      INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    descripcion   VARCHAR2(200) NOT NULL,
    tipo_error    VARCHAR2(200) NOT NULL
);

ALTER TABLE error ADD CONSTRAINT error_pk PRIMARY KEY ( id_error );

CREATE TABLE estados (
    estado_pedido   INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    descripcion     VARCHAR2(20) NOT NULL
);

ALTER TABLE estados ADD CONSTRAINT estados_pk PRIMARY KEY ( estado_pedido );

CREATE TABLE nombre (
    id_nombre     INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    descripcion   VARCHAR2(100) NOT NULL
);

ALTER TABLE nombre ADD CONSTRAINT nombre_pk PRIMARY KEY ( id_nombre );

CREATE TABLE pais (
    id_pais       INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    descripcion   VARCHAR2(100) NOT NULL
);

ALTER TABLE pais ADD CONSTRAINT pais_pk PRIMARY KEY ( id_pais );

CREATE TABLE pedido (
    id_pedido                INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    id_usuario               INTEGER NOT NULL,
    fecha_pedido             DATE NOT NULL,
    fecha_envio              DATE,
    fecha_entrega            DATE,
    nombre_destinatario      VARCHAR2(100) NOT NULL,
    id_pais                  INTEGER NOT NULL,
    ciudad_destinatario      VARCHAR2(100),
    direccion_destinatario   VARCHAR2(100) NOT NULL,
    fono_destinatario        INTEGER NOT NULL,
    id_camion                integer not null,
    estado_pedido            INTEGER NOT NULL
);

ALTER TABLE pedido ADD CONSTRAINT pedido_pk PRIMARY KEY ( id_pedido );

CREATE TABLE producto (
    id_producto         INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    id_nombre           INTEGER NOT NULL,
    id_usuario          INTEGER NOT NULL,
    id_calidad          INTEGER NOT NULL,
    kilos_producto      INTEGER NOT NULL,
    precio_producto     INTEGER NOT NULL,
    stock_producto      INTEGER NOT NULL,
    fecha_ingreso       DATE NOT NULL,
    fecha_actualizada   DATE
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( id_producto );

CREATE TABLE region (
    id_region   INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    nombre      VARCHAR2(100) NOT NULL
);

ALTER TABLE region ADD CONSTRAINT region_pk PRIMARY KEY ( id_region );

CREATE TABLE roles (
    id_rol        INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    descripcion   VARCHAR2(100) NOT NULL
);

ALTER TABLE roles ADD CONSTRAINT roles_pk PRIMARY KEY ( id_rol );

CREATE TABLE camion (
    id_camion          INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    id_usuario         integer not null,
    nombre             VARCHAR2(500) NOT NULL,
    descripcion        VARCHAR2(500) NOT NULL,
    tamano             VARCHAR2(100) NOT NULL,
    capacidad_carga    VARCHAR2(100) NOT NULL,
    patente            VARCHAR2(10) NOT NULL
);

ALTER TABLE camion ADD CONSTRAINT camion_pk PRIMARY KEY ( id_camion );

CREATE TABLE saldos (
    id_saldos       INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    montos_saldos   INTEGER,
    id_nombre       INTEGER,
    precio_fruta    INTEGER,
    fecha_publicacion DATE
);

CREATE TABLE saldos_detalle (
    id_saldo_detalle       INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL,
    id_saldos       INTEGER NOT NULL,
    id_pedido       INTEGER NOT NULL,
    cantidad        INTEGER NOT NULL,
    total           INTEGER NOT NULL
    
);

ALTER TABLE saldo_detalle ADD CONSTRAINT saldo_detalle_pk PRIMARY KEY ( id_saldo_detalle );

ALTER TABLE saldos ADD CONSTRAINT saldos_pk PRIMARY KEY ( id_saldos );

ALTER TABLE saldos
    ADD CONSTRAINT saldos_fk FOREIGN KEY ( id_nombre )
        REFERENCES nombre ( id_nombre );

ALTER TABLE saldos_detalle
    ADD CONSTRAINT detalle_pedido_saldos_fk FOREIGN KEY ( id_saldos )
        REFERENCES saldos ( id_saldos );

ALTER TABLE saldos_detalle
    ADD CONSTRAINT detalle_ped_saldos_fk FOREIGN KEY ( id_pedido )
        REFERENCES pedido ( id_pedido );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_pais_fk FOREIGN KEY ( id_pais )
        REFERENCES pais ( id_pais );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_roles_fk FOREIGN KEY ( id_rol )
        REFERENCES roles ( id_rol );

ALTER TABLE contratos
    ADD CONSTRAINT contratos_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE detalle_pedido
    ADD CONSTRAINT detalle_pedido_pedido_fk FOREIGN KEY ( id_pedido )
        REFERENCES pedido ( id_pedido );

ALTER TABLE detalle_pedido
    ADD CONSTRAINT detalle_pedido_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE pedido
    ADD CONSTRAINT pedido_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE pedido
    ADD CONSTRAINT pedido_estados_fk FOREIGN KEY ( estado_pedido )
        REFERENCES estados ( estado_pedido );

ALTER TABLE pedido
    ADD CONSTRAINT pedido_pais_fk FOREIGN KEY ( id_pais )
        REFERENCES pais ( id_pais );

ALTER TABLE pedido
    ADD CONSTRAINT pedido_camion_fk FOREIGN KEY ( id_camion )
        REFERENCES camion ( id_camion );

ALTER TABLE producto
    ADD CONSTRAINT producto_calidad_fk FOREIGN KEY ( id_calidad )
        REFERENCES calidad ( id_calidad );

ALTER TABLE producto
    ADD CONSTRAINT producto_nombre_fk FOREIGN KEY ( id_nombre )
        REFERENCES nombre ( id_nombre );

ALTER TABLE producto
    ADD CONSTRAINT producto_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE camion
    ADD CONSTRAINT camion_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );