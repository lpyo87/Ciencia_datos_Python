Luis Pedro Pérez - 22008067
Ciencia de Datos en Python
#Investigación #1: Git, GitHub y Markdown
> # Git
Git es un sistema de control de versiones distribuido lo cual implica una copia en un repositorio en la nube, teniendo copias en un repositorio local. El cual por medio de comandos se llegan a sincronizar las mismas.
## Comandos

Dentro de la terminal se utilizan los comandos para poder utilizar git. Existen diversos comandos de git dentro de los cuales se tienen los siguientes:
 - **git init**: Se utiliza para inicializar el folder o proyecto/repositorio a trabajar.
 - **git add**: Se utiliza para poder guardar o salvar ya sea todos o cambios específicos realizados en el archivo del proyecto que se esté trabajando.
    - Para grabar únicamente los cambios realizados a un archivo, después del comando ***git add*** se puede agregar el **nombre con extensión** del archivo a sincronizar.
    - Para grabar todos los cambios realizados en los archivos del repositorio, después del comando ***git add*** se le agrega un punto **"."** quedando así ***git add .*** .
    - Estos comandos hacen que se agregen los archivos a sincronizar a una etapa de staging donde se posteriormente se subirán al repositorio de la nube.
- **git commit** se encarga de guardar los cambios acumulados con la intención de poder regresar a estos, de ser necesario. Es importante que para llevar un registro de las actualizaciones de los archivos por lo que se le agrega el parámetro **-m** donde el mensaje de los cambios deben de ir entre comillas dobles ("").
**git commit -m "mensaje"**
- **git log** comando utilizado para ver el registro de los cambios realizados al repositorio.
- **git status** se utiliza para visualizar las modificaciones realizadas a los archivos del repositorio. Asímismo indica el código SHA de actualización para poder restaurar la información de los archivos en caso fuera necesaria.
- **git checkout** comando utilizado para restaurar el estado de uno o varios archivos. Este código se utiliza en conjunto con el código SHA obtenido del comando ***git status***.

> # GitHub
[GitHub](https://github.com/) es un sitio web  en el cual se puede sincronizar las aplicaciones o el progreso de los proyectos realizados bajo el sistema Git. De esta manera, sirve de almacenamiento para que otras personas puedan descargarlos, ver los códigos y versiones de los archivos para poder realizarles cambios y se pueda aportar en los mismos creando posibles ramificaciones.
Para eso se necesita crear un usuario, y repositorios los cuales servirán como carpetas para organizar los proyectos y de esta manera poder tener una clasificación de archivos por proyecto.
Los repositorios pueden ser públicos o privados dependiendo de la necesidad o nivel de confidencialidad de los archivos. 