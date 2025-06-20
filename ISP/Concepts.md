# Lección 4: El Principio de Segregación de Interfaces (Interface Segregation Principle - ISP)

Esta es la **"I"** de S.O.L.I.D. Este principio se enfoca en asegurar que las abstracciones que creamos sean lo más ajustadas y específicas posible.

### Concepto y Teoría

La definición formal del Principio de Segregación de Interfaces es:

> "Ningún cliente (código que usa una clase) debería ser forzado a depender de métodos que no usa."

#### ¿Qué significa esto en la práctica?

En pocas palabras: **Es mejor tener muchas interfaces pequeñas y específicas que una sola interfaz grande y genérica.**

Este principio es como aplicar el Principio de Responsabilidad Única (SRP) a las interfaces. Si una clase, para implementar un "contrato" (nuestra Clase Base Abstracta), se ve obligada a implementar métodos que no tienen sentido para ella (dejándolos vacíos o con un `raise NotImplementedError`), significa que la interfaz es demasiado "gorda" y necesita ser "segregada" (dividida).

**Analogía del Restaurante:**
Imagina ir a un restaurante de lujo y que te den un único menú de 50 páginas que incluye desayunos, almuerzos, cenas, postres, carta de vinos, cócteles y menú infantil. Si solo vas a cenar, te están forzando a depender de una "interfaz" (el menú) con muchísimas opciones que no usas. Lo ideal es tener menús segregados: una carta de cenas, una carta de vinos, etc.

### Ventajas y Desventajas

#### ✅ Ventajas de aplicar ISP

* **Bajo Acoplamiento:** Las clases solo dependen de los métodos que realmente les interesan. Si una interfaz pequeña cambia, solo afectará a las clases que la implementan, no a todo el sistema.
* **Alta Cohesión y Claridad:** Las interfaces tienen un propósito claro y bien definido. El código se vuelve más fácil de entender.
* **Flexibilidad y Reusabilidad:** Es mucho más fácil para una clase implementar varias interfaces pequeñas y específicas que una sola monolítica. Esto promueve la reutilización de estas interfaces en diferentes contextos.

#### ⚠️ Desventajas o "Cuidados" a tener

* **Proliferación de Interfaces:** Si no se tiene cuidado, se puede terminar con un número muy grande de archivos/clases, cada uno con una interfaz diminuta. Hay que encontrar un balance lógico para agrupar los métodos.