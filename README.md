
---
***English***

# ***Amanda Mateo Boutique***
#### **Video Demo:** https://youtu.be/XqdgIVWoqEk
### **Description**: *Amanda Mateo Boutique* is a Python project using the Django framework to create a showroom for a designer of custom-made quinceañera dresses. It also manages the databases for Catalog, Clients, Suppliers, Appointments, Cash Register Transactions, Dollar Exchange Rate, and User Profiles.

**Technologies**

- Python
- Django
- HTML
- SQLite
- Weasyprint / gtk3-runtime

*Note: gtk3-runtime is required for Weasyprint to function.*

**Description of Files and Folders**

**AmandaProject** is the main Django project where the following files were used:

- **Setting.py**: project configuration.

- **urls.py**: Project URLs.

**BoutiqueApp**: The app that displays the showroom's main page, with a dynamic section that shows the dresses in the Catalog and manages the Catalog database.

- **views.py**: Python logic.

- **forms.py**: Python logic for the database formats.

- **models.py**: Definition of the Catalog database.

- **urls.py**: URLs of the BoutiqueApp.

- **Templates Folder**: Where each of the HTML files used for managing the Catalog database are located.

- **index.html**: Showroom's main page, where the dynamic catalog, the Sabre Amanda section, Contacts, and the administration area for the different databases are displayed.

**ClientesAPP**: The app that manages the customer database.

- **views.py**: Python logic.

- **forms.py**: Python logic for database formats.

- **models.py**: Definition of the Clients database.

- **urls.py**: URLs for the ClientsApp.

- **templates folder**: Where each of the HTML files used to manage the Clients database are located.

**SuppliersApp**: The app that manages the Suppliers database.

- **views.py**: Python logic.

- **forms.py**: Python logic for database formats.

- **models.py**: Definition of the Suppliers database.

- **urls.py**: URLs for the Suppliers app.

- **templates folder**: Where each of the HTML files used to manage the Suppliers database are located.

**citas** is the app that manages the database for appointments and due dates.

- **views.py**: Python logic.

- **forms.py**: Python logic for database formats.

- **models.py**: Definition of the User Profile database.

- **urls.py**: URLs for the Appointments app.

- **Templates Folder**: Where each of the HTML files used for managing the Appointments database is located.

**flujo** is the app that manages the database for controlling the executive workflow.

- **views.py**: Python logic.

- **forms.py**: Python logic for database formats.

- **models.py**: Definition of the User Profile database.

- **urls.py**: URLs for the Appointments app.

- **Templates Folder**: This folder contains all the HTML files used to manage the MovimientoCaja and CotizacionDolar databases.

**LoginApp**: This app manages the PerfilUsuarios database.

- **views.py**: Python logic.

- **forms.py**: Python logic for the database formats.

- **models.py**: Definition of the PerfilUsuarios database.

- **urls.py**: URLs for the Proveedores app.

- **Templates Folder**: This folder contains all the HTML files used to manage the Proveedores database.

**Usage:**
- The Home button in the navbar will always take you to the home page.

- The About Amanda button will take you to a descriptive section about Amanda Mateo Boutique.

    * The Showroom button dynamically displays the different models in the Catalog database, automatically showing everything in the Catalog.

    * The Contact button takes you to the contact information.

    * The Admin button takes you to the section where the different databases are created and listed.

    * If the user is not logged in, the Login and Register options will appear in the NAVBAR. If they are not logged in, the Login and Logout options will appear.

    * In the Administration Panel, you will find the following buttons:

    * Administration: This takes you to the administration of Djando users, groups, and databases.

    * There are also six buttons for uploading information from the Catalog, Clients, Suppliers, Appointments, Cash Transactions, and Dollar Exchange Rate databases.

    * A button to view the dashboard or financial summary. - In the BoutiqueApp, the catalog list includes options to create a PDF in product list format and another option to create a PDF in catalog database format.

- The citas app includes options to add a new event and view the calendar graphically.

- The flujo app manages debit and credit information, where the amount is maintained.
---
***Español***

# ***Amanda Mateo Boutique***
#### **Video Demo:** https://youtu.be/XqdgIVWoqEk
### **Descripción**: *Amanda Mateo Boutique* es un proyecto realizado en Python con el framework de Django para crear un showroom para una diseñadora de vestidos para quinceañeras hechos a la mediada, adicionalmente para administrar las bases de datos de Catalogo, Clientes, Proveedores, cita, MovimientoCaja, CotizacionDolar y PerfilUsuarios.

**Tecnologías**

- Python
- Django
- HTML
- SQLite
- Weasyprint / gtk3-runtime

*nota: se requiere instalar gtk3-runtime, para que Weasyprint funcione*

**Descripción archivos y carpetas**

**AmandaProjecto**, es el proyecto principal de Django donde se usaron los archivos:

- **Setting.py**: configuración del proyecto.

- **urls.py**: urls del proyecto.

**BoutiqueApp**, es la app donde se muestra la página principal del showroom, con una sección dinámica que muestra los vestidos en el Catalogo y hace manejo de la base de datos de Catalogo.

- **views.py**: lógica de Python.

- **forms.py**: lógica de Python para los formatos de la base de datos.

- **models.py**: definición de la base de datos Catalogo.

- **urls.py**: urls de la app BoutiqueApp.

- **Carpeta templetes**: donde están cada uno de los HTML que se usaron para el manejo de la base de datos Catalogo.

- **index.html**: página principal del showroom, donde se ve el catálogo dinámico, la sección de sabre Amanda, Contactos y el área de administración de las diferentes bases de datos

**ClientesAPP**, es la app que maneja la base de datos de clientes.

- **views.py**: lógica de Python.

- **forms.py**: lógica de Python para los formatos de la base de datos.

- **models.py**: definición de la base de datos Clientes.
- **urls.py**: urls de la app ClientesApp.
- **Carpeta templetes**: donde estan cada uno de los HTML que se usaron para el manejo de la base de datos Clientes.

**ProveedoresApp**, es la app que maneja la base de datos de Proveedores.

- **views.py**: lógica de Python.

- **forms.py**: lógica de Python para los formatos de la base de datos.

- **models.py**: definición de la base de datos Proveedores.

- **urls.py**: urls de la app Proveedores.

- **Carpeta templetes**: donde están cada uno de los HTML que se usaron para el manejo de la base de datos Proveedores.

**citas**, es la app que maneja la base de datos de para las citas y fecha de entregas.

- **views.py**: lógica de Python.

- **forms.py**: lógica de Python para los formatos de la base de datos.

- **models.py**: definición de la base de datos Perfil Usuarios.

- **urls.py**: urls de la app citas.

- **Carpeta templetes**: donde están cada uno de los HTML que se usaron para el manejo de la base de datos Cita.

**flujo**, es la app que maneja la base de datos de para el control de flujo de ejectivo.

- **views.py**: lógica de Python.

- **forms.py**: lógica de Python para los formatos de la base de datos.

- **models.py**: definición de la base de datos Perfil Usuarios.

- **urls.py**: urls de la app citas.

- **Carpeta templetes**: donde están cada uno de los HTML que se usaron para el manejo de la base de datos MovimientoCaja y CotizacionDolar.

**LoginApp**, es la app que maneja la base de datos de PerfilUsuarios.

- **views.py**: lógica de Python.
- **forms.py**: lógica de Python para los formatos de la base de datos.

- **models.py**: definición de la base de datos Perfil Usuarios.

- **urls.py**: urls de la app Proveedores.

- **Carpeta templetes**: donde están cada uno de los HTML que se usaron para el manejo de la base de datos Proveedores.

**Uso:**
- El botón de Inicio del navbar siempre llevara a la página de inicio.
- El botón Sobre Amanda, los llevara a una sección descriptiva de Amanda Mateo Boutique.
    * El botón de Showroom muestra los diferentes modelos que estan el la base de datos Catalogo en forma dinamica, automaticamente mostrara todo lo que este el Calalogo.
    * El botón de Contacto, los llevara a la información de contacto.
    * El botón de Admin, los llevara la sección donde se crean y listan las diferentes bases de datos.
    * Si el usuario no está logeado le aparecerá en el NAVBAR las opciones de Login y Registrarse, en caso que no lo este le saldrán las opciones de Login y Logout.
    * En Panel de Administración, Encontraran los botones:
    * Administración, este pasara a la administración de Djando de usuarios, grupos y base de datos.
    * También hay 6 botones para la carga de información de las bases de datos de Catalogo, Clientes, Proveedores, cita, MovimientoCaja y CotizacionDolar.
    * Un botón para ver el dashboard o resumen financiero.
- El la app BoutiqueApp, en la lista de catalago se crearon la opción de crear un PDF el formato de lista de los productos y otra opción para crear un PDF en formato de ficha la base de datos Catalogo
- En la app citas están las opciones de agregar un nuevo evento y ver el calendario en forma gráfica.
- En la app flujo se maneja la información de débito y haber, donde el monto se mantiene en dólares, en caso que los débito o haberes es en Bolívares la app automáticamente lo convierte en dólares con la cotización del día, que está en la base de datos CotizacionDolar.
- Para poder manejar estas bases de datos se tiene que estar logeado.

**Gracias,**

**Herman Frias**

