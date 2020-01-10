###########################
Documentación de referencia
   Certificación aeODOO
###########################

En este proyecto encontrarás la documentación sobre la versión community de `Odoo`_,
tanto funcional como técnica, en la que se basa las pruebas de certificación
creadas y promovidas por la `Asociación Española de Odoo`_.


***************************
Principales Características
***************************

* **100% Open Source** (`LGPL version 3`_): Toda `la documentación está disponible
  en GitHub`_
* Creada por y para la comunidad. Añade, corrige, debate y colabora en mejorar está
documentación

.. _Odoo: https://www.odoo.com
.. _`Asociación Española de Odoo: https://www.aeodoo.org
.. _`la documentación está disponible en GitHub`: https://github.com/aeodoo/documentacion

***************
Parte Funcional
***************

* **Básico**

.. toctree::
   funcional/basico/comunicacion-interna
   funcional/basico/acciones-planificadas
   funcional/basico/exportar-datos-csv-y-excel
   funcional/basico/vista-listado
   funcional/basico/vista-pivot

* **Datos Maestros**

.. toctree::
   funcional/datos-maestros/clientes
   funcional/datos-maestros/productos

* **CRM**

.. toctree::
   funcional/crm/iniciativas

* **Ventas**

.. toctree::
   funcional/ventas/productos
   funcional/ventas/tarifas-de-ventas
   funcional/ventas/comisiones

* **Logística**

.. toctree::
   funcional/logistica/almacenes-y-ubicaciones
   funcional/logistica/entrada-de-mercancia
   funcional/logistica/salida-de-mercancia
   funcional/logistica/movimientos-internos
   funcional/logistica/inventario

* **Fabricación**

.. toctree::
   funcional/fabricacion/lista-de-materiales
   funcional/fabricacion/ordenes-de-fabricacion

* **Eventos**

.. toctree::
   funcional/eventos

* **Proyectos**

.. toctree::
   funcional/proyectos/tareas
   funcional/compras/informacion-de-productos-por-proveedor
   funcional/compras/reglas-de-reabastecimiento
   funcional/compras/pedido-de-compra

* **Facturación**

.. toctree::
   funcional/facturacion/facturas-de-clientes
   funcional/facturacion/cobros
   funcional/facturacion/facturas-de-proveedores
   funcional/facturacion/pagos

* **Contabilidad**

.. toctree::
   funcional/contabilidad/plan-general-contable
   funcional/contabilidad/diarios
   funcional/contabilidad/extractos-bancarios

***************
Parte Técnica
***************

* **Previo**

.. toctree::
   tecnico/previo/python
   tecnico/previo/xml
   tecnico/previo/github
   tecnico/previo/linux

* **Entorno**

.. toctree::
   tecnico/entorno/odoo-server/instalacion-desde-github
   tecnico/entorno/odoo-server/comandos-basicos
   tecnico/entorno/odoo-server/archivo-de-configuracion
   tecnico/entorno/estructura-addons/repositorios
   tecnico/entorno/estructura-addons/actualizacion-y-control-de-versiones
   tecnico/entorno/estructura-modulo/estructura-de-archivos-y-guidelines
   tecnico/entorno/estructura-modulo/archivo-de-manifiesto

* **ORM-API**

.. toctree::
   tecnico/orm-api/modelos/tipos-de-modelos
   tecnico/orm-api/modelos/componentes-de-un-modelo
   tecnico/orm-api/modelos/herencia
   tecnico/orm-api/modelos/herencia-por-delegacion
   tecnico/orm-api/campos/sintaxis
   tecnico/orm-api/campos/tipos
   tecnico/orm-api/campos/atributos
   tecnico/orm-api/campos/campos-automaticos
   tecnico/orm-api/campos/campos-reservados
   tecnico/orm-api/campos/campos-calculados
   tecnico/orm-api/campos/herencia-y-definiciones-incrementales
   tecnico/orm-api/metodos/estructura-y-sintaxis
   tecnico/orm-api/metodos/enviroment
   tecnico/orm-api/metodos/recordset
   tecnico/orm-api/metodos/context
   tecnico/orm-api/metodos/decoradores
   tecnico/orm-api/metodos/operaciones-frecuentes/create
   tecnico/orm-api/metodos/operaciones-frecuentes/write
   tecnico/orm-api/metodos/operaciones-frecuentes/unlink
   tecnico/orm-api/metodos/operaciones-frecuentes/browse
   tecnico/orm-api/metodos/operaciones-frecuentes/search
   tecnico/orm-api/metodos/operaciones-frecuentes/update
   tecnico/orm-api/metodos/herencia
   tecnico/orm-api/metodos/defaults-y-gets
   tecnico/orm-api/metodos/compute-and-searchs
   tecnico/orm-api/metodos/constrains-y-onchanges
   tecnico/orm-api/metodos/actions-methods
   tecnico/orm-api/metodos/orm-overrides
   tecnico/orm-api/metodos/business-methods
   tecnico/orm-api/manejo-de-errores/usererror
   tecnico/orm-api/manejo-de-errores/validationerror
   tecnico/orm-api/manejo-de-errores/accessdenied
   tecnico/orm-api/manejo-de-errores/accesserror
   tecnico/orm-api/manejo-de-errores/cachemiss
   tecnico/orm-api/manejo-de-errores/missingerror
   tecnico/orm-api/manejo-de-errores/redirectwarning

* **Datos**

.. toctree::
   tecnico/datos/estructura-xml
   tecnico/datos/operaciones
   tecnico/datos/abreviaturas
   tecnico/datos/csv

* **Vistas**

.. toctree::
   tecnico/vistas/estructura-y-sintaxis/cabecera-y-atributos
   tecnico/vistas/estructura-y-sintaxis/widgets
   tecnico/vistas/estructura-y-sintaxis/uso-de-contexto
   tecnico/vistas/estructura-y-sintaxis/botones
   tecnico/vistas/estructura-y-sintaxis/filtros
   tecnico/vistas/estructura-y-sintaxis/domains
   tecnico/vistas/estructura-y-sintaxis/estilos-css
   tecnico/vistas/vista-lista
   tecnico/vistas/vista-search
   tecnico/vistas/vista-formulario
   tecnico/vistas/vista-kanban
   tecnico/vistas/vista-calendario
   tecnico/vistas/vista-grafica-y-pivot
   tecnico/vistas/vista-dashboard
   tecnico/vistas/vista-cohort
   tecnico/vistas/vista-activity
   tecnico/vistas/vista-qweb
   tecnico/vistas/vistas-embebidas
   tecnico/vistas/herencia-de-vistas

* **Dominios**

.. toctree::
   tecnico/dominios/notacion-polaca
   tecnico/dominios/dominios-en-python
   tecnico/dominios/dominios-xml
   tecnico/dominios/dominios-dinamicos

* **Actions y Menús**

.. toctree::
   tecnico/actions-y-menus/sintaxis-y-atributos
   tecnico/actions-y-menus/acciones-de-servidor
   tecnico/actions-y-menus/acciones-de-informe
   tecnico/actions-y-menus/acciones-de-ventana
   tecnico/actions-y-menus/acciones-de-url
   tecnico/actions-y-menus/acciones-de-cliente
   tecnico/actions-y-menus/acciones-planificadas

* **Seguridad**

.. toctree::
   tecnico/seguridad/grupos
   tecnico/seguridad/control-de-acceso
   tecnico/seguridad/reglas-de-registros
   tecnico/seguridad/acceso-a-campos

* **Wizards**

.. toctree::
   tecnico/wizards

* **Internacionalización**

.. toctree::
   tecnico/internacionalizacion

* **Informes**

.. toctree::
   tecnico/informes/estructura-atributos-y-guidelines
   tecnico/informes/templates
   tecnico/informes/papel
   tecnico/informes/personalizacion-de-get-report-values
   tecnico/informes/tipografia
   tecnico/informes/estilos

* **Dashboards**

.. toctree::
   tecnico/dashboards

* **Debug**

.. toctree::
   tecnico/debug/logger-y-log-level
   tecnico/debug/wdb
   tecnico/debug/pudb
   tecnico/debug/ptvsd

* **Tests y C.I.**

.. toctree::
   tecnico/tests-y-ci/tests-de-python
   tecnico/tests-y-ci/tests-de-javascript
   tecnico/tests-y-ci/tests-de-integracion
   tecnico/tests-y-ci/travis
   tecnico/tests-y-ci/coverage
   tecnico/tests-y-ci/black-y-pre-commit

* **Base da Datos**

.. toctree::
   tecnico/base-de-datos

* **Open Upgrade**

.. toctree::
   tecnico/openupgrade

* **Herramientas de Rendimiento**

.. toctree::
   tecnico/herramientas-de-rendimiento/odoo-profile
   tecnico/herramientas-de-rendimiento/pyflame-flamegraph
   tecnico/herramientas-de-rendimiento/pgbadger

* **Backend**

.. toctree::
   tecnico/backend/javascript
   tecnico/backend/widgets
   tecnico/backend/templates

* **Helpers**

.. toctree::
   tecnico/helpers

* **Frontend**

.. toctree::
   tecnico/frontend

* **Mixin Models**

.. toctree::
   tecnico/mixin-models/mail-thread
   tecnico/mixin-models/mail-alias-mixin
   tecnico/mixin-models/mail-activity-mixin
   tecnico/mixin-models/portal-mixin
   tecnico/mixin-models/utm-mixin
   tecnico/mixin-models/website-published
   tecnico/mixin-models/rating-mixin
   tecnico/mixin-models/website-seo-metadata
   tecnico/mixin-models/website-multi
   tecnico/mixin-models/website-published-multi
