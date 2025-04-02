1. Título:

Suite de Pruebas Automatizadas para Urban Grocers: Creación de Usuario y Kits de Productos, con Validación del Parámetro firstName

2. Descripción:

Este proyecto automatiza las pruebas unitarias para la creación de usuarios, la generación de un authToken y la creación de kits de productos. Se enfoca en validar el parámetro firstName dentro de una función que modifica el contenido del cuerpo de la solicitud.

3. Tabla de Contenidos:

Introducción
Instalación
Uso
Estructura del Proyecto
Tecnologías Utilizadas
Contribuciones
Licencia

4. Introducción

Objetivo: El propósito de este proyecto es automatizar las pruebas para verificar la funcionalidad de creación de kits de productos en Urban Grocers. Se centra en validar el comportamiento del campo name en la solicitud de creación de kits, utilizando una lista de comprobación previamente definida.

Alcance: El proyecto cubre la automatización de pruebas para el campo name en la creación de kits de productos. Esto incluye casos positivos (nombres válidos con caracteres especiales, espacios o números) y negativos (nombres vacíos, demasiado largos o con tipos de datos incorrectos).

Exclusiones: Otras funcionalidades de la API: Este proyecto se enfoca exclusivamente en la creación de kits de productos y la validación del campo name. No cubre otras funcionalidades de la API de Urban Grocers, como gestión de usuarios, productos, pedidos, etc.

Interfaz gráfica y pruebas manuales: No se incluyen pruebas manuales ni validaciones relacionadas con la interfaz gráfica. El enfoque es exclusivamente en la API.

Motivación: El objetivo es automatizar todas las pruebas de la lista de comprobación para asegurar que:

Las respuestas de la API coincidan con los resultados esperados.
Los casos válidos devuelvan un código 201 y los inválidos un código 400.
El repositorio esté bien estructurado, documentado y listo para revisión.

5. Instalación

Requisitos previos:
Python 3.6 o superior
Paquetes: pytest y requests
Pasos de instalación:
Clonar el repositorio: git clone https://github.com/tu-usuario/qa-project-Urban-Grocers-app-es

Crear un entorno virtual:
python -m venv venv

Activar el entorno virtual:
source venv/bin/activate (Linux/Mac) o venv\Scripts\activate (Windows)

Instalar las dependencias:
pip install pytest requests

6. Uso

Para ejecutar todas las pruebas, utiliza el siguiente comando:
pytest

Opciones de ejecución:

Para ver detalles adicionales:
pytest -v

Para instalar la librería requests:
pip install requests o pip3 install requests

7. Estructura del Proyecto

configuration.py: Contiene la URL y endpoints de la API.

data.py: Contiene los datos de solicitud POST (crear usuario, crear kit y headers).

sender_stand_request.py: Define las funciones para crear un nuevo usuario y un kit, asociando el kit al usuario mediante el authToken.

create_kit_name_kit_test.py: Incluye las pruebas unitarias, tanto positivas como negativas.

7. Tecnologías Utilizadas

Lenguaje de programación: Python
Frameworks de testing: pytest
Otras librerías: requests, unittest


8. Contribuciones

Cómo contribuir:

Realiza un fork del repositorio, crea una rama para tu contribución y abre un pull request.

Sigue las guías de estilo y lineamientos de código.

Convenciones de código:

Asegúrate de seguir las convenciones de PEP 8 para mantener la consistencia del código.

9. Licencia

Este proyecto está licenciado bajo la MIT License, lo que permite su uso y distribución de forma libre y flexible.
