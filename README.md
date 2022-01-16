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

3. Problemas
    - Autodocumentación no se genera de forma correcta
        - Fuentes consultadas:
            - https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
            - https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365
            - https://www.sphinx-doc.org/
            - https://www.youtube.com/watch?v=b4iFyrLQQh4
        - Comentarios:
            - Probé con diferentes estructuras de archivos, obtuve el mismo resultado
    SOLUCIONADO:
        - La autodocumentación no se generaba de manera correcta debido a que no estaba activado el ambiente virtual 
        - Instalación del tema "sphinx-rtd-theme"
    - Usando raw SQL, las validaciones de la cláusula WHERE no funcionan para campo description de property  
    SQL utilizado para intentar corregirlo (sin funcionar):  
    ```
    SELECT * FROM (
        SELECT
            p.address as address,
            p.city as city,
            p.price as price,
            case  
                when p.description = '' then NULL 
            end as description,
            s.name as name,
            p.year as year
        FROM status_history sh
        LEFT JOIN status s ON s.id = sh.status_id
        LEFT JOIN property p ON p.id = sh.property_id
        WHERE s.name='{}'
        AND (p.address IS NOT NULL OR p.address <> "")
        AND (p.year IS NOT NULL OR p.year <> "")
        AND (p.description IS NOT NULL OR p.description <> "")
        AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
        ORDER BY sh.update_date DESC
    ) as A
    WHERE A.description IS NOT NULL;
    ```

### Estructura de archivos

Actual
```
.
├── LICENSE
├── README.md
├── app.py
├── docs/
├── database
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── db.cpython-310.pyc
│   │   └── models.cpython-310.pyc
│   ├── db.py
│   └── models.py
├── requirements.txt
└── utils
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   └── utils.cpython-310.pyc
    └── utils.py
```  

Anterior
```
.
├── LICENSE
├── README.md
├── app.py
├── docs/
├── requirements.txt
├── models.py
├── db.py
└── utils
``` 
 

