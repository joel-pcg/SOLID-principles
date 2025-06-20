# Lección 1: El Principio de Responsabilidad Única (Single Responsibility Principle - SRP)

Esta es la **"S"** de S.O.L.I.D. y es el pilar sobre el que se construyen los demás principios.

### Concepto y Teoría

El Principio de Responsabilidad Única, definido por Robert C. Martin ("Uncle Bob"), establece que:

> "Una clase debe tener una, y solo una, razón para cambiar."

#### ¿Qué significa esto en la práctica?

Significa que una clase debe tener un único **trabajo** o una única **responsabilidad** bien definida. Si una clase se encarga de múltiples tareas conceptualmente diferentes, está violando este principio.

La mejor forma de pensarlo es a través de los "actores" o "departamentos" que podrían solicitar un cambio en el software. Por ejemplo:
* El departamento de **Contabilidad** podría pedir cambiar cómo se calculan los impuestos.
* El departamento de **Sistemas** podría pedir cambiar la base de datos de MySQL a PostgreSQL.
* El equipo de **UX/UI** podría pedir que un reporte se genere como PDF en lugar de JSON.

Si los tres cambios anteriores te obligan a modificar **la misma clase**, esa clase tiene demasiadas responsabilidades. Un cambio en la lógica de impuestos no debería arriesgar romper la lógica de guardado en la base de datos.

En el contexto de Python, estas responsabilidades suelen agruparse en:

* **Manejo de la persistencia**: Guardar o leer de una base de datos, un archivo local, un servicio en la nube, etc.
* **Validación de datos**: Comprobar que los datos de entrada son correctos y cumplen ciertas reglas.
* **Lógica de negocio**: Realizar cálculos complejos, aplicar reglas específicas del dominio.
* **Formateo o presentación de datos**: Generar un JSON, un XML, un PDF, un HTML, etc.
* **Comunicación con servicios externos**: Interactuar con APIs de terceros.

### Ventajas y Desventajas

#### ✅ Ventajas de aplicar SRP

* **Testabilidad**: Es mucho más fácil escribir pruebas unitarias para una clase que solo hace una cosa.
* **Mantenibilidad**: Cuando ocurre un error, el lugar a revisar es obvio. Las modificaciones son más seguras porque un cambio en una responsabilidad no afectará a otra.
* **Reusabilidad**: Una clase que solo se encarga de generar reportes en CSV puede ser utilizada en muchas partes de tu aplicación.
* **Claridad y Organización**: El código se vuelve más fácil de entender. El nombre de una clase como `UserValidator` te dice exactamente lo que hace.

#### ⚠️ Desventajas o "Cuidados" a tener

* **Sobre-ingeniería**: Si se lleva al extremo, puedes terminar con una explosión de clases muy pequeñas, lo que podría hacer que la arquitectura general sea más difícil de seguir al principio. Se necesita encontrar un balance.
* **Complejidad inicial**: Al principio, puede parecer más trabajo crear 3 clases pequeñas que una grande. El beneficio de esta inversión se manifiesta a mediano y largo plazo en la vida del proyecto.