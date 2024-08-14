# Task Flow Module

## Descripción
El módulo `taskflow` para Odoo v17 permite gestionar las tareas de proyectos de manera eficiente. Este módulo proporciona una interfaz sencilla para crear y administrar tareas, asegurando que las fechas de inicio y fin sean coherentes.

## Instalación
1. Descarga o clona el repositorio del módulo `taskflow`.
2. Copia la carpeta del módulo en el directorio de addons de tu instalación de Odoo.
3. Reinicia el servidor de Odoo.
4. Ve a la interfaz de Odoo, navega a `Apps`, actualiza la lista de aplicaciones y busca `taskflow`.
5. Instala el módulo `taskflow`.

## Uso
1. Navega al menú `Taskflow` en Odoo.
2. Crea nuevas tareas proporcionando un título, descripción, fecha de inicio y fecha de fin.
3. Asegúrate de que la fecha de inicio no sea superior a la fecha de fin para evitar errores de validación.

## Dependencias
Este módulo depende únicamente del módulo `base` de Odoo y no requiere librerías adicionales.

## Script de Creación de Tareas
En la carpeta `tools` del módulo, existe un script en Python que permite crear registros en la tabla de tareas (`taskflow.task`). Este script puede ser ejecutado desde la terminal y solicita los datos de conexión a la base de datos, así como los detalles de la tarea a crear.


Autor: Wilson Contreras
Versión: 17.0.0.1
