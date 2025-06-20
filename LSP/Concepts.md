# Lección 3: El Principio de Sustitución de Liskov (Liskov Substitution Principle - LSP)

Esta es la **"L"** de S.O.L.I.D. Fue formulado por Barbara Liskov y, aunque su definición formal suena muy académica, su idea central es muy intuitiva.

### Concepto y Teoría

La definición formal del Principio de Sustitución de Liskov es:

> "Si S es un subtipo de T, entonces los objetos de tipo T en un programa pueden ser reemplazados por objetos de tipo S sin alterar ninguna de las propiedades deseables de ese programa."

#### ¿Qué significa esto en la práctica?

En palabras más simples: **Una clase hija (subtipo) debe ser completamente sustituible por su clase padre (tipo base) sin que el programa se rompa o se comporte de forma inesperada.**

Si tienes una función que espera un objeto de tipo `Animal` y le pasas un objeto `Perro` (que hereda de `Animal`), la función debe seguir funcionando perfectamente.

Esto implica que una clase hija:

1.  **No debe cambiar la firma de los métodos heredados:** Mismos parámetros, mismos tipos de retorno.
2.  **No debe fortalecer las precondiciones:** No puede ser más estricta con sus inputs que el padre. Si el padre acepta cualquier número, el hijo no puede aceptar solo números positivos.
3.  **No debe debilitar las postcondiciones:** El resultado del hijo debe cumplir las mismas reglas que el resultado del padre. Si el padre promete devolver siempre una lista, el hijo no puede devolver `None`.
4.  **No debe lanzar excepciones que el padre no lanzaría:** Si el método del padre nunca lanza un `ValueError`, el método del hijo tampoco debería hacerlo.

**Una violación común de LSP ocurre cuando creamos una clase hija que "restringe" o "elimina" un comportamiento del padre, en lugar de simplemente "extenderlo" o "especializarlo".**

### Ventajas y Desventajas

#### ✅ Ventajas de aplicar LSP

* **Confiabilidad:** Garantiza que la herencia y el polimorfismo funcionen como se espera. Puedes confiar en que un subtipo se comportará según el contrato de su tipo base.
* **Mantenibilidad:** Evita tener que añadir comprobaciones de tipo (`if isinstance(obj, Perro): ...`) en tu código, lo que simplifica la lógica.
* **Reusabilidad:** Las funciones que operan sobre un tipo base pueden reutilizarse con confianza con cualquier nuevo subtipo que se cree en el futuro.

#### ⚠️ Desventajas o "Cuidados" a tener

* **Jerarquías Rígidas:** Puede obligarte a pensar mucho más en tus jerarquías de clases. A veces, la herencia no es la solución, y es mejor usar composición. Si una clase hija "no encaja" del todo, probablemente no debería ser una clase hija.