# Instalación 


## Requisitos
1. Instalar Flask con el siguiente comando: pip install Flask
2. Instalar las librerías para la base de datos: pip install pymysql
2. Tener un manegador de base de datos como mariadb o mysql

## Startup
1. Crear un usuario para el manejador de base de datos con el usuario "user" y contraseña "12345" con todos los permisos para que sea igual que el usuario utilizado para la conexión con la base de datos definido en el código fuente en el archivo main.py.
2. Importar la base de datos ubicado en /schema.sql
1. Entrar a la carpeta "/".
2. Ejecutar el código: flask --app main.py run
   

## Nota 
1. No se actualiza el programa cuando se guardan cambios en los archivos. Hay que reiniciar el live-server para observar los cambios. 
