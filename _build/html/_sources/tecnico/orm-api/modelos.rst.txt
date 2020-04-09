.. _modelos:

#Modelos


Los modelos describen las estructuras de datos utilizadas en Odoo. Gracias a la importación de la clases de python “models” y “fields” definidas en el propio ORM podremos utilizar todas las funcionalidades desarrolladas en el core de Odoo.

.. code-block:: python

	from odoo import models, fields

Cada modelo creará una instancia automáticamente en base de datos, estas instancias representan los modelos disponibles y dependen de los módulos instalados. Cada instancia de un modelo es una conjunto de registros, una tabla en la base de datos con los registros ordenados, el propio ORM nos ofrece métodos como search() o browse() para recuperar los registros de un modelo concreto.

Los modelos se definen como clases de Python, con la cabecera, atributos del modelo con el prefijo “_”, campos y funciones en una estructura como sigue:

.. code-block:: python

	class ModelName(models.Model):
		_name = 'model.name'

		field1 = fields.Char()

La estructura completa de un modelo utilizando las guías oficiales de estilo de la OCA queda:

1. **Cabecera**
2. **Atributos** privados (_name, _inherit, etc.)
3. **Métodos** Default y _default_get
4. Declaraciones de **campos** (field = …)
5. **Métodos** compute y search en el mismo orden que sus campos correspondientes
6. **Métodos** constrains (@api.constrains) y onchange (@api.onchange)
7. **Métodos** CRUD (sobreescritura de métodos básicos del ORM)
8. **Métodos** Action
9. **Métodos** propios del modelo de negocio

****************
Tipos de modelos
****************

Podemos diferenciar tres tipos principales de modelos en función de su cometido:

**Model**: Son los modelos para los datos persistentes en base de datos. Es utilizado para la gran mayoría de modelos creados en el sistema, se representan como tablas en la base de datos.

.. code-block:: python

	class ModelName(Model):

**TransientModel**: Modelos con datos temporales, se guardan en base de datos pero son limpiados periódicamente. Son utilizados para modelos temporales que no guardan históricos de registros, por ejemplo para asistentes. También se representan como tablas en la base de datos, aunque los registros de la tabla son eliminados por el propio ORM periódicamente.

.. code-block:: python

	class ModelName(TransientModel):

**AbstracModel**: Modelos que definen una estructura y métodos creados para ser incorporados mediante herencia en otros modelos añadiendole funcionalidades a modo de plantilla. Al revés que los tipos anteriores, no se reprensentan como tablas en la base de datos, sin embargo, cuando son heredados por otros tipos de modelo, añaden su estructura y funcionalidades al modelo (y su correspondiente tabla) que lo hereda.

.. code-block:: python

	class ModelName(AbstractModel):

************************
Componentes de un modelo
************************

Atributos
=========

Los atributos son definidos a continuación del encabezado y si bien la mayoría de ellos son opcionales, ya que usan valores por defecto definidos en propio ORM, permiten modificar ciertos comportamientos del modelo.

Atributos utilizados frecuentemente:

- _name
- _description
- _order
- _inherit

Atributos utilizados ocasionalmente:

- _inherits
- _rec_name


Atributos extraordinariamente utilizados:

- _sequence


- _name:
	Define el nombre del modelo, es un atributo obligatorio que sirve como identificador único en el sistema. 

.. code-block:: python
	
	_name = "model.name"

.. admonition:: Guidelines

	Los nombres de los modelos deben ir en minúsculas y, en el caso de llevar varias palabras, separadas por puntos. Utiliza nombres de modelos lo más cortos posible pero suficientemente específicos para comprender su cometido y evitar conflictos con otros modelos.


- _description:
	Atributo opcional para ofrecer una breve descripción del modelo.

.. code-block:: python
	
	_name = "Model Short Description"

- _order:
	Permite especificar el campo por defecto que se utiliza para ordenar el resultado de una búsqueda de registros en el modelo. Si no especificamos este atributo, Odoo utilizará por defecto el campo "id" para ordenar los registros. Cualquier vista o método de búsqueda que no específique el orden mediante un parámetro propio recuperará los registros por campo especificado en este atributo.

- _inherit:
	String o listados de strings que especifica uno o más modelos sobre los que heredamos.

.. tip::

	Si se establece el parámetro _name en el nuevo modelo y este no se corresponde con ninguno de los modelos especificados en el inherit, estaremos creando un nuevo modelo que copia las características de los modelos heredados (campos, vistas, métodos...) pero los implementa de modo independiente (los modelos heredados no acceden a estas nuevas características), si embargo, si el atributo _name se corresponde con uno de los modelos especificados en el _inherit, estaremos extendiendo el modelo heredado. Si no se establece el atributo _name, en el inherit debe haber exclusivamente un modelo especificado, del cual el ORM entenderá estamos ampliando (equivalente a poner el _name con el nombre del modelo heredado). Para más detalle, ver herencia #TODO: link a herencia

- _inherits:
	Utilizado para la herencia por delegación #TODO: link a herencia por delegación

- _sequence:
	Parámetro opcional y muy raramente utilizado que sirve para especificar que secuencia de postgres se debe utilizar para autonumerar el campo ID de la base de datos. La secuencia por lo general se creará de modo automático siguiente un patrón de "nombre_modelo_id_seq".

- _rec_name:
	El ORM a la hora de mostrar registros establece el campo 'name' como prioritario para identificar al registro en cuestión. Mediante este parámetro podríamos modificar el comportamiento para especificar otro campo como etiqueta de registro (por ejemplo al seleccionar una registro en un campo relacional de un formulario).

.. tip:

	Si bien el atributo _rec_name es suficiente en muchos casos, por ejemplo para que en vez del "name" se visualice un campo "code" a la hora de seleccionar registros, también es posible modificar este comportamiento de un modo más elaborado heredando el método método name_get (para especificar el campo que debe mostrar como etiqueta) y el name_search (para especificar por que campos debe filrar al escribir). #TODO: Link a name_search y name_get

- _check_company_auto:

- _parent_name:
- _parent_store:
- _abstract:
- _transient:
- _date_name:
- _fold_name:
- _auto:
	Parámetro para específicar si debe crear automáticamente una tabla en la base de datos para el modelo. Por defecto su valor ser True, si se establece a False se debe reescribir el método init() del modelo para especificar como inicializarlo.

.. note::

	Para la inmensa mayoría de casos, cuando no queremos que se inicialice en base de datos un modelo utilizaremos la clase AbstractModel para crearlo.	

- _table:
	Parámetro opcional que permite especificar el nombre de la tabla guardad en la base de datos. Por defecto tomara el valor del nombre del modelo sustituyendo los puntos por guiones bajos.

.. warning:
	
	No es recomendable modificar los comportamientos a bajo nivel del ORM sin ninguna justificación objetiva, ya que añade complejidad al mantenimiento y la compatibilidad con el trabajo de terceros. 

Campos
======

Los campos definen la estructura del modelo, de tal modo que dan forma a la tabla que el ORM creará en la base de datos.

Para más detalle: :ref:`sintaxis <campos>`.

********
Herencia
********

***********************
Herencia por delegación
***********************
