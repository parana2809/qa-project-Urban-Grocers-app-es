# Dillinger
## _The Last Markdown Editor, Ever_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Dillinger is a cloud-enabled, mobile-ready, offline-storage compatible,
AngularJS-powered HTML5 Markdown editor.

- Type some Markdown on the left
- See HTML in the right
- ✨Magic ✨

## Features

- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
   
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
