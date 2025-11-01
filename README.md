Entrega Final
Comisión 78130
Herman Frias
hermanfrias@hotmail.com


# AmandaBoutique
Proyecto Amanda Boutique, un showroom, para una diseñadora de vestidos de quinceañeras hechos a la medida.

Instrucciones:

• Ir al disco y directorio donde se quiere crear el proyecto

• Clonar el repositorio de GitHub en la carpeta:
    -- git clone https://github.com/hermanfrias/AmandaBoutique.git .

• En la carpeta AmandaBoutique crear el ambiente virtual y activarlo:
    -- python -m venv .venv .
    -- .venv/Scripts/Activate

• Instalar las librerias que se encuentran en requirements.txt:
    -- pip install -r requirements.txt

• Instalar las base de datos o modelos:
    -- py manage.py makemigrations
    -- py manage.py migrate 

• Levantar el servidor virtual:
    -- python manage.py runserver

• Abrir el navegardor y colorar ests dirección:
    -- http://127.0.0.1:8000/ o http://localhost:8000/

• Uso:
    -- El botón de Inicio del navbar siempre llevara a la página de inicio.
    -- El botón de catalogo a un apartado donde se verían en un futuro el catalogo de producto, por ahora solo hay ejemplos.
    -- El botón Sobre Amanda, los llevara a unas sección descriptiva de Amanda Boutique y del creador de este proyecto Herman Frias
    -- El botón de Contacto, los llevara a la información de contacto.
    -- El botón de Admin, los llevara la la sección donde se crean y listan las diferentes bases de datos.
    -- Si el usuario no esta logeado le aparecera en el NAVBAR las opciones de Login y Registrarse, en caso que no lo este le saldran las opciones de Login y Logout.

• En Panel de Administración, Encontraran los botones:
    -- Administración, este pasara a la administración de Djando de usuarios, grupos y base de datos.
    -- También hay 3 botones para la carga de información de las bases de datos de Catalogo, Clientes y Proveedores.
    -- Están los botones para listar las mismas bases de datos

• Las views de las bases de datos de Catalogo y PerfilUsuario fueron creadas como funciones y las bases de datos de Clientes y Proveedores como clases.

• El video explicativo del proyecto lo puedene encontrar en:
    -- https://drive.google.com/file/d/1U6SMOO1pwpx70HiVOjLVgbK6tzPRcMLz/view?usp=sharing


