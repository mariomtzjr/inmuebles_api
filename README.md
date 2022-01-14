# inmuebles_api
Ejercicio de una herramienta en la que los usuarios puedan consultar los inmuebles disponibles para la venta. En esta herramienta los usuarios deben ser capaces de ver tanto los inmuebles vendidos como los disponibles. Con el objetivo de hacer más fácil la búsqueda, se espera que los usuarios puedan aplicar diferentes filtros a la búsqueda.

## Requerimientos o tecnologías
- Python v3.7
- Flask 2.0.2
- Flask-SQLAlchemy 2.5.1
- Flask-RESTful 0.3.9

## Implementación

1. Modelo de datos
2. Parámetros de conexión a BD
3. Creación del proyecto
4. Creación de los modelos de acuerdo al punto 1
5. Instalación de dependencias
6. Establecer endpoint para listado de inmuebles
7. Establecer parámetros de consulta
    - pre_venta
    - en_venta
    - vendido
8. Establecer parámetros de filtrado
    - Año de construcción
    - Ciudad
    - Estado
9. Establecer la información a mostrar por cada inmueble
    - Dirección
    - Ciudad
    - Estado
    - Precio de venta
    - Descripción

### Dudas
1. ¿Cómo limito las búsquedas de acuerdo al número de parámetros en el query string con el ORM?
    - or para buscar por city o state o year
    - validaciones de acuerdo a los argumentos? *** Solución

2. Cambios:
    - Añadir campo state
        ALTER TABLE habi_db.property
        ADD COLUMN state VARCHAR(50) AFTER address;


