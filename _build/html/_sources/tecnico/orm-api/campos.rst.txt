.. _campos:

######
Campos
######

Los campos son importados mediante la clase fields. Con ellos podemos incorporar a nuestro modelo la estructura de datos y ciertos atributos sobre los mismos (requerido, etiqueta en vistas, etc.)

.. _sintaxis_campos:

********
Sintaxis
********

Los campos se definen después de los atributos indicando el nombre del campo con la siguiente sintaxis

.. code-block:: python

	field_name : fields.Type(Atributes)

Modificando Type  y Atributes  por el tipo y los atributos correspondientes al campo.

.. _tipos_campos:

*****
Tipos
*****

Los tipos de campos de los que disponemos gracias al ORM son:

- Char:
- Boolean:
- Float:
- Integer:
- Binary:
- Html:
- Image:
- Monetary:
- Selection:
- Text:
- Date:
- Datetime:
- Many2one:
- One2many:
- Many2many:
- Reference:
- Many2oneReference:

.. _atributos_campos:

*********
Atributos
*********

Los atributos disponibles para los campos son:

- string
- help
- readonly
- required
- index
- default
- states
- groups
- company_dependent
- copy
- store
- group_operator
- compute
- compute_sudo
- inverse
- search
- related
- Otros atributos dependientes del tipo de campo

.. _campos_automaticos:

******************
Campos Automáticos
******************

Al inicializar cualquier modelo el ORM automáticamente nos creará ciertos campos básicos para el modelo registrado:
id

- create_date
- create_uid
- write_date
- write_uid

.. _campos_reservados:

*****************
Campos Reservados
*****************

Alguno campos, si bien no son creados automáticamente por el ORM, tienen un nombre con un significado especial que los provee de ciertas funcionalidades, que podremos incorporar al modelo simplemente definiendo el campo:

- name:
- active:
- state:
- parent_id:
- parent_path:
- company_id:

*****************
Campos Calculados
*****************

*************************************
Herencia y definiciones incrementales
*************************************







