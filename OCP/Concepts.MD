# Lección 2: El Principio de Abierto/Cerrado (Open/Closed Principle - OCP)

Esta es la **"O"** de S.O.L.I.D. Es uno de los principios más importantes para crear sistemas mantenibles a largo plazo.

### Concepto y Teoría

La definición original de Bertrand Meyer establece:

> "Las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para la extensión, pero cerradas para la modificación."

#### ¿Qué significa esto en la práctica?

Significa que deberías poder **añadir nueva funcionalidad** a tu sistema **sin cambiar el código existente** que ya funciona y ha sido probado.

* **Abierto para la extensión:** Puedes hacer que tu módulo o clase haga cosas nuevas.
* **Cerrado para la modificación:** Logras esta nueva funcionalidad sin tocar el código fuente de las clases ya existentes.

Cambiar código que ya funciona es arriesgado. Podrías introducir bugs en una parte del sistema que era estable. El OCP busca minimizar ese riesgo.

La herramienta clave para lograr esto en la Programación Orientada a Objetos es la **abstracción**. En lugar de depender de clases concretas, dependemos de "interfaces" o "contratos".

**Analogía útil:** Piensa en el puerto USB-C de un portátil. El puerto en sí está **cerrado a modificaciones** (no puedes soldarle nuevos cables sin romperlo). Sin embargo, está **abierto a extensiones**: puedes conectarle un cargador, un monitor externo, un lector de tarjetas, un teclado... Se pueden crear nuevos dispositivos (extensiones) que usan la misma interfaz (el puerto) sin necesidad de modificar el portátil.

En Python, logramos esto principalmente a través de **Clases Base Abstractas (Abstract Base Classes - ABCs)** del módulo `abc`.

### Ventajas y Desventajas

#### ✅ Ventajas de aplicar OCP

* **Estabilidad y Robustez**: Al no modificar código existente, se reduce drásticamente el riesgo de introducir nuevos errores en funcionalidades que ya eran estables.
* **Mantenibilidad**: El código es más fácil de mantener porque las nuevas funcionalidades están aisladas en nuevas clases, en lugar de añadirse a clases ya grandes y complejas.
* **Flexibilidad y Reusabilidad**: El sistema se vuelve "conectable" (pluggable). Puedes añadir o cambiar funcionalidades fácilmente, fomentando la reutilización de componentes.

#### ⚠️ Desventajas o "Cuidados" a tener

* **Complejidad Inicial**: Requiere más planificación y la creación de abstracciones (interfaces, clases base). Esto puede parecer un exceso de trabajo para funcionalidades muy simples, pero paga sus dividendos a medida que el proyecto crece.
* **Predecir el futuro**: Aplicar OCP implica tener una idea de qué partes del sistema son más propensas a cambiar o extenderse. Crear abstracciones en lugares equivocados puede llevar a una complejidad innecesaria.