from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# PARA CONECTARSE POR DEFAULT
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# PARA CONECTARSE A POSTGRESQL SE DEBE INSTALAR psycong2
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': 'SASA',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# PARA CONECTARSE A MYSQL SE DEBE INSTALAR mysqlclient PERO EN WINDOWS TIENE UN ERROR,
# ASI QUE OTRA OPCION ES IR A LOS ARCHIVOS BINARIOS EN LA PAGINA https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
# Y BUSCAR EL QUE DIGA mysqlclient Y DEBEMOS DE PROBAR INSTALANDO CADA UNO PARA ENCONTRAR EL QUE SI SOPORTE WINDOWS
# UTILIZANDO LOS COMANDOS --> pip install rutadeladescarga\nombredelarchivo.whl
# DESPUES DEBEMOS DE INGRESAR A MSQL WORKBENCH Y CONECTARNOS AL USUARIO ROOT, ABRIR UN QUERY NEW Y PEGAR ESTOS COMANDOS:
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'sasa';
# PARA CAMBIAR EL TIPO DE AUTENTIFICACION DE LA CONTRASEÑA DE ROOT PARA QUE DJANGO PUEDA ACCEDER PORQUE CON LA NUEVA
# NO ES COMPATIBLE EN DJANGO Y SI QUEREMOS REGRESAR A SU TIPO DE AUTENTIFICACION QUE TENIA SOLO HAY QUE INGRESAR EN
# WORKBENCH LOS COMANDOS: ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'sasa';
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': 'sasa',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
