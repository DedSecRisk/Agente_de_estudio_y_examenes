# Especificación para evolucionar el generador de Guías + Exámenes interactivos

## 1. Objetivo

Modificar el agente/generador actual para que cada material generado tenga una experiencia de estudio más organizada y rápida, sin abandonar el formato actual de HTML offline.

La prioridad inmediata **NO es migrar a React, Next.js, Vue, backend, login o base de datos**.

La prioridad es:

1. Mejorar la presentación visual de las guías.
2. Evitar que una guía sea una sola página enorme.
3. Permitir navegar rápidamente entre temas mediante una **Ruta rápida**.
4. Mostrar solamente el tema que el usuario está estudiando.
5. Mantener todo el contenido generado disponible dentro del HTML.
6. Generar automáticamente un examen interactivo asociado a cada guía.
7. Guardar el progreso del examen en el navegador.
8. Mostrar resultados al finalizar.
9. Identificar los temas que requieren repaso.
10. Permitir regresar directamente desde el resultado del examen al tema correspondiente de la guía.

---

# 2. Principios que NO deben romperse

El agente debe conservar:

- HTML5.
- CSS3.
- JavaScript vanilla.
- Funcionamiento offline.
- Compatibilidad con navegadores modernos.
- Impresión de la guía cuando sea posible.
- Generación automática desde Python.
- Estructura de contenido generada por el agente.
- El estilo visual oscuro existente como base, salvo que se indique explícitamente otro diseño.
- La posibilidad de generar todo el material sin depender de un servidor.

## No introducir todavía

No migrar el proyecto a:

- React.
- Next.js.
- Vue.
- Angular.
- Base de datos.
- Backend obligatorio.
- Sistema de usuarios.
- Autenticación.
- Pagos.
- Framework CSS obligatorio.

Estas tecnologías podrán evaluarse posteriormente, pero no forman parte de esta etapa.

---

# 3. Experiencia objetivo

La experiencia final debe ser aproximadamente:

```text
GUÍA
│
├── Dashboard / Introducción
│
├── Ruta rápida
│   ├── Tema 1
│   ├── Tema 2
│   ├── Tema 3
│   ├── Tema 4
│   └── ...
│
├── Tema activo
│   ├── Teoría
│   ├── Ejemplos
│   ├── Tablas
│   ├── Diagramas
│   ├── Código
│   ├── Puntos clave
│   └── Repaso
│
├── Anterior / Siguiente
│
└── Examen
    ├── Preguntas
    ├── Progreso
    ├── Guardado automático
    ├── Resultado
    ├── Resultado por tema
    ├── Temas a repasar
    └── Botones para regresar a la guía
```

---

# 4. Problema actual que debe resolverse

Actualmente las guías pueden contener una gran cantidad de contenido en una única página.

Esto provoca:

- demasiado scroll;
- dificultad para localizar un tema;
- poca sensación de progreso;
- dificultad para regresar rápidamente a una sección;
- dificultad para estudiar únicamente un tema;
- poca relación visual entre guía y examen.

La solución no es eliminar contenido.

La solución es **organizar el contenido en temas navegables**.

---

# 5. Nueva estructura de la guía

Cada guía debe estar dividida en temas independientes.

Ejemplo:

```html
<section id="tema-tcp-ip" class="tema activo">
    ...
</section>

<section id="tema-subnetting" class="tema">
    ...
</section>

<section id="tema-routing" class="tema">
    ...
</section>
```

La clase `.activo` determina qué tema se muestra.

CSS mínimo:

```css
.tema {
    display: none;
}

.tema.activo {
    display: block;
}
```

El contenido de los temas que no están activos **no debe eliminarse del HTML**.

Simplemente debe ocultarse visualmente.

---

# 6. IDs obligatorios para los temas

Cada tema debe tener un identificador único y estable.

Ejemplo:

```text
tcp-ip
subnetting
routing
switching
vpn
firewalls
```

El ID debe:

- ser único;
- no contener espacios;
- ser estable entre generaciones cuando sea posible;
- utilizarse tanto en la guía como en los resultados del examen.

Ejemplo:

```json
{
  "id": "subnetting",
  "nombre": "Subnetting"
}
```

---

# 7. Modelo de datos de la guía

El agente debe generar primero una estructura lógica de la guía y posteriormente renderizarla en HTML.

Ejemplo:

```json
{
  "curso": "Redes",
  "titulo": "Guía de Redes",
  "temas": [
    {
      "id": "tcp-ip",
      "nombre": "TCP/IP",
      "orden": 1
    },
    {
      "id": "subnetting",
      "nombre": "Subnetting",
      "orden": 2
    },
    {
      "id": "routing",
      "nombre": "Routing",
      "orden": 3
    }
  ]
}
```

La estructura puede ampliarse según las necesidades del generador.

---

# 8. Ruta rápida

La guía debe tener una navegación visible denominada:

**Ruta rápida**

Su función es permitir saltar inmediatamente al tema deseado.

Ejemplo visual:

```text
┌────────────────────────────────────────────┐
│ RUTA RÁPIDA                                │
├────────────────────────────────────────────┤
│ [Introducción] [TCP/IP] [Subnetting]       │
│ [Routing] [Switching] [VPN] [Firewall]     │
│ [Examen]                                    │
└────────────────────────────────────────────┘
```

En desktop puede utilizar una distribución horizontal o grid.

En móvil debe adaptarse.

---

# 9. Comportamiento de la Ruta rápida

Al seleccionar un tema:

1. Ocultar el tema actualmente visible.
2. Mostrar el tema seleccionado.
3. Actualizar el estado visual del botón seleccionado.
4. Hacer scroll hacia el inicio del contenido.
5. Guardar el último tema visitado.

Ejemplo:

```javascript
function mostrarTema(id) {
    document.querySelectorAll(".tema").forEach(function(tema) {
        tema.classList.remove("activo");
    });

    var tema = document.getElementById("tema-" + id);

    if (!tema) return;

    tema.classList.add("activo");

    localStorage.setItem("ultimoTema", id);

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}
```

El selector exacto puede adaptarse a la implementación final.

---

# 10. Recordar el último tema

Cuando el usuario vuelva a abrir la guía, debe intentarse recuperar el último tema visitado.

Ejemplo:

```javascript
var ultimoTema = localStorage.getItem("ultimoTema");

if (ultimoTema) {
    mostrarTema(ultimoTema);
}
```

Si no existe:

```text
mostrar el primer tema.
```

No debe producirse un error si el tema guardado ya no existe.

---

# 11. Navegación Anterior / Siguiente

Cada tema debe tener navegación:

```text
← Tema anterior       Tema siguiente →
```

Ejemplo:

```javascript
function siguienteTema() {
    // determinar el índice actual
    // mostrar el siguiente tema
}

function anteriorTema() {
    // determinar el índice actual
    // mostrar el tema anterior
}
```

En el primer tema:

- ocultar o desactivar "Anterior".

En el último tema:

- ocultar o desactivar "Siguiente".

---

# 12. Indicador de progreso de la guía

Opcionalmente se puede mostrar:

```text
Tema 3 de 10
██████████░░░░░░░░░░ 30%
```

Esto debe calcularse automáticamente a partir del número real de temas.

No escribir manualmente el porcentaje.

---

# 13. Contenido interno de cada tema

La estructura interna actual de las guías debe conservarse.

Cada tema puede contener:

- explicación;
- conceptos;
- definiciones;
- tablas;
- ejemplos;
- código;
- comandos;
- diagramas;
- gráficos;
- casos prácticos;
- puntos clave;
- errores frecuentes;
- preguntas de repaso.

El cambio principal es de **organización y navegación**, no de eliminación del contenido.

---

# 14. Relación entre guía y examen

Cada guía generada debe tener automáticamente un examen asociado.

Ejemplo:

```text
/redes/
    guia.html
    examen.html
```

O, si el generador requiere un único archivo:

```text
/redes/
    index.html
```

con acceso a:

```text
Guía
Examen
```

La implementación puede conservar el formato actual del proyecto, pero debe existir una relación clara entre:

```text
GUÍA ↔ EXAMEN
```

---

# 15. Generación automática del examen

El agente debe generar preguntas a partir del contenido real de la guía.

No deben generarse preguntas desconectadas del temario.

Cada pregunta debe tener:

- ID.
- Tema.
- Pregunta.
- Opciones.
- Respuesta correcta.
- Explicación.
- Opcionalmente dificultad.

Ejemplo:

```json
{
  "id": "q01",
  "tema": "tcp-ip",
  "pregunta": "¿Qué función cumple TCP?",
  "opciones": {
    "A": "Asignar direcciones IP",
    "B": "Proporcionar transporte orientado a conexión",
    "C": "Resolver nombres DNS",
    "D": "Enrutar paquetes"
  },
  "respuesta": "B",
  "explicacion": "TCP proporciona transporte orientado a conexión..."
}
```

---

# 16. Etiquetado obligatorio por tema

Este punto es fundamental.

**Toda pregunta debe estar asociada a un tema.**

Ejemplo:

```json
{
  "q01": {
    "respuesta": "B",
    "tema": "tcp-ip"
  },
  "q02": {
    "respuesta": "C",
    "tema": "subnetting"
  }
}
```

Esto permitirá posteriormente calcular:

```text
Resultado general
+
Resultado por tema
+
Temas a repasar
```

Sin esta relación no será posible identificar correctamente qué áreas necesita reforzar el estudiante.

---

# 17. Examen interactivo

El comportamiento base debe conservar el concepto del examen interactivo actual.

Debe incluir:

- preguntas de opción múltiple;
- contador de preguntas respondidas;
- barra de progreso;
- botón para mostrar resultados;
- revisión de respuestas;
- explicación de errores;
- opción para reintentar.

Ejemplo:

```text
Reactivos respondidos: 7 / 10

██████████████░░░░░░ 70%

[Mostrar resultados]
```

---

# 18. Guardado automático del examen

A diferencia del comportamiento actual, el nuevo examen debe guardar el progreso.

Utilizar inicialmente:

```javascript
localStorage
```

No utilizar backend en esta etapa.

Ejemplo de información guardada:

```json
{
  "q01": "B",
  "q02": "C",
  "q03": "A"
}
```

La clave debe estar asociada al examen.

Ejemplo:

```text
examen_redes_respuestas
```

Evitar claves genéricas que puedan sobrescribir otros exámenes.

---

# 19. Restaurar examen

Al abrir nuevamente el examen:

1. Buscar respuestas guardadas.
2. Restaurarlas.
3. Actualizar el contador.
4. Actualizar la barra de progreso.

Ejemplo conceptual:

```javascript
function guardarRespuesta(qid, respuesta) {
    respuestas[qid] = respuesta;

    localStorage.setItem(
        "examen_redes_respuestas",
        JSON.stringify(respuestas)
    );
}
```

Al cargar:

```javascript
var guardado = localStorage.getItem("examen_redes_respuestas");

if (guardado) {
    respuestas = JSON.parse(guardado);
    restaurarRespuestas();
}
```

---

# 20. No borrar automáticamente el progreso

Cerrar el navegador no debe borrar las respuestas.

El progreso solamente debe eliminarse cuando el usuario seleccione explícitamente:

```text
Reiniciar examen
```

Antes de borrar el progreso puede solicitarse confirmación:

```text
¿Seguro que quieres reiniciar el examen?
Se perderán tus respuestas actuales.
```

---

# 21. Resultado final

Al terminar el examen debe aparecer un panel de resultados.

Ejemplo:

```text
┌─────────────────────────────────────┐
│           RESULTADO                 │
│                                     │
│             18 / 25                 │
│               72%                   │
│                                     │
│ ⚠️ Buen nivel. Refuerza tus fallos.│
└─────────────────────────────────────┘
```

Debe mostrar:

- respuestas correctas;
- respuestas incorrectas;
- total;
- porcentaje;
- mensaje de retroalimentación;
- preguntas incorrectas;
- opción correcta;
- explicación.

---

# 22. Resultado por tema

Esta es una funcionalidad prioritaria.

El resultado debe agrupar las preguntas por tema.

Ejemplo:

```text
DOMINIO POR TEMA

TCP/IP
██████████████████░░ 90%

Subnetting
██████████░░░░░░░░░░ 50%

Routing
██████████████░░░░░░ 70%

VPN
████████████████████ 100%
```

El cálculo debe realizarse automáticamente.

Ejemplo:

```text
tema = subnetting
preguntas = 4
correctas = 2

resultado = 50%
```

---

# 23. Identificación automática de temas a repasar

El sistema debe detectar los temas con desempeño bajo.

Umbral inicial recomendado:

```text
>= 80%  → Dominado
60-79%  → Reforzar
< 60%   → Repasar
```

Estos valores deben estar centralizados en una configuración para poder modificarlos posteriormente.

Ejemplo:

```javascript
const UMBRALES = {
    dominado: 80,
    reforzar: 60
};
```

No convertir estos valores en reglas dispersas por el código.

---

# 24. Panel "Temas a repasar"

Si existen temas con desempeño bajo, mostrar:

```text
📚 TEMAS A REPASAR

🔴 Subnetting — 50%
🟠 Routing — 65%

[Repasar Subnetting]
[Repasar Routing]
```

Cada botón debe regresar directamente al tema correspondiente de la guía.

---

# 25. Enlace examen → guía

Cada resultado por tema debe tener un enlace/botón como:

```text
Repasar tema
```

Ejemplo:

```html
<button onclick="abrirTema('subnetting')">
    Repasar Subnetting
</button>
```

Si la guía y el examen son archivos separados, debe utilizarse el enlace correspondiente.

Ejemplo conceptual:

```text
examen.html → guia.html#tema-subnetting
```

La guía debe reconocer el hash y abrir automáticamente ese tema.

---

# 26. Compatibilidad con hash de URL

La guía debe poder recibir:

```text
guia.html#tema-subnetting
```

y mostrar automáticamente:

```text
Subnetting
```

Esto permite que el examen pueda enviar directamente al usuario al contenido que necesita repasar.

---

# 27. Arquitectura recomendada para el agente

Separar generación y presentación.

```text
/agente
│
├── generators/
│   ├── generar_guia.py
│   ├── generar_examen.py
│   └── generar_indice.py
│
├── templates/
│   ├── guia_template.html
│   ├── examen_template.html
│   └── components/
│       ├── ruta_rapida.html
│       ├── tema.html
│       ├── pregunta.html
│       └── resultado.html
│
├── assets/
│   ├── css/
│   │   └── app.css
│   └── js/
│       ├── guia.js
│       └── examen.js
│
├── content/
│   └── ...
│
└── output/
    └── ...
```

Si el proyecto actual utiliza otra estructura, no es necesario reorganizarlo completamente.

Lo importante es separar conceptualmente:

```text
Contenido
Generación
Plantilla
Estilos
Comportamiento
Salida
```

---

# 28. JavaScript de la guía

La lógica de la guía debe encargarse de:

- mostrar tema;
- ocultar temas;
- Ruta rápida;
- tema anterior;
- tema siguiente;
- progreso;
- último tema visitado;
- hash de URL.

No mezclar esta lógica con la del examen si los archivos son independientes.

---

# 29. JavaScript del examen

La lógica del examen debe encargarse de:

- detectar respuestas;
- guardar respuestas;
- restaurar respuestas;
- actualizar progreso;
- calcular resultados;
- calcular resultados por tema;
- mostrar respuestas correctas;
- mostrar explicaciones;
- detectar temas a repasar;
- enlazar a los temas correspondientes;
- reiniciar el examen.

---

# 30. Mejoras visuales deseadas

Mantener el estilo oscuro actual como base, pero hacer que la interfaz se sienta como una plataforma de estudio.

Elementos recomendados:

### Encabezado

```text
🎓 Redes

Progreso de la guía: 40%
```

### Ruta rápida

Tarjetas/botones claros.

### Tema activo

Contenido central amplio y legible.

### Navegación

```text
← Anterior                         Siguiente →
```

### Examen

Barra de progreso fija o claramente visible.

### Resultado

Tarjeta visual de puntuación.

### Dominio por tema

Barras de progreso.

---

# 31. Diseño responsive

La interfaz debe funcionar en:

- PC.
- Laptop.
- Tablet.
- Teléfono.

En pantallas pequeñas:

- Ruta rápida debe poder desplazarse horizontalmente o utilizar grid.
- Tablas deben permitir scroll horizontal.
- Los grids deben convertirse en una columna.
- Los botones deben seguir siendo fáciles de tocar.
- La navegación anterior/siguiente debe adaptarse.

Ejemplo:

```css
@media (max-width: 768px) {
    .grid2 {
        grid-template-columns: 1fr;
    }
}
```

---

# 32. Rendimiento

No sacrificar rendimiento innecesariamente.

Si se utilizan gráficos o imágenes:

- utilizar WebP/SVG cuando sea conveniente;
- utilizar `loading="lazy"` para imágenes no críticas;
- utilizar `decoding="async"` cuando corresponda;
- evitar imágenes gigantes;
- evitar JavaScript innecesario.

Para el modo offline/autocontenido se puede mantener Base64 si es necesario.

No convertir todo a un sistema complejo de assets si esto rompe la facilidad de distribución actual.

---

# 33. Modo offline

El resultado debe continuar funcionando sin conexión.

Por lo tanto:

- no depender de CDN;
- no depender de fuentes externas;
- no depender de APIs para funcionar;
- no requerir servidor para estudiar;
- `localStorage` debe ser suficiente para el progreso inicial.

---

# 34. Compatibilidad con impresión

La guía debe conservar una versión razonable para impresión.

Cuando se imprima:

- mostrar todo el contenido de los temas;
- no imprimir únicamente el tema actualmente seleccionado;
- ocultar controles innecesarios;
- ocultar botones de navegación;
- ocultar elementos interactivos que no aporten a la impresión.

Ejemplo conceptual:

```css
@media print {
    .tema {
        display: block !important;
    }

    .ruta-rapida,
    .navegacion,
    .botones-interactivos {
        display: none !important;
    }
}
```

Esto es importante porque el modo web puede ocultar temas, pero el documento impreso debe contener el material completo.

---

# 35. Accesibilidad básica

La navegación debe poder utilizarse sin depender exclusivamente del color.

Los estados deben tener:

- texto;
- iconos cuando corresponda;
- contraste suficiente;
- `aria-current` en el tema activo cuando sea apropiado;
- botones reales para acciones.

No utilizar únicamente:

```text
verde = correcto
rojo = incorrecto
```

También debe existir una indicación textual.

---

# 36. Datos del examen

La información del examen debe poder generarse de forma estructurada.

Formato recomendado:

```json
{
  "curso": "Redes",
  "total": 25,
  "preguntas": [
    {
      "id": "q01",
      "tema": "tcp-ip",
      "pregunta": "¿Qué función cumple TCP?",
      "opciones": {
        "A": "...",
        "B": "...",
        "C": "...",
        "D": "..."
      },
      "respuesta": "B",
      "explicacion": "...",
      "dificultad": "media"
    }
  ]
}
```

El HTML final puede contener estos datos embebidos para conservar el modo offline.

---

# 37. Validaciones que debe realizar el agente

Antes de generar el HTML final, validar:

### Guía

- Todos los temas tienen ID.
- Todos los IDs son únicos.
- Todos los temas tienen nombre.
- Existe un primer tema.
- La Ruta rápida apunta a temas existentes.

### Examen

- Todas las preguntas tienen ID.
- Los IDs de preguntas son únicos.
- Todas tienen exactamente una respuesta correcta.
- Todas tienen tema.
- El tema existe en la guía.
- Todas las opciones requeridas existen.
- Todas tienen explicación.

### Integración

- Cada tema utilizado por una pregunta existe.
- Cada botón "Repasar tema" apunta a un tema válido.
- El identificador usado en el examen coincide con el identificador de la guía.

Si una validación falla, el agente debe reportarla antes de producir una salida aparentemente correcta.

---

# 38. Generación de preguntas

Las preguntas deben estar relacionadas con el material generado.

Evitar:

- preguntas genéricas;
- preguntas cuya respuesta no aparece ni puede deducirse del contenido;
- preguntas ambiguas;
- preguntas con más de una respuesta razonablemente correcta;
- distractores absurdos;
- repetir exactamente la misma pregunta varias veces.

El nivel debe poder adaptarse al material.

---

# 39. Distribución por temas

El agente debe procurar que el examen represente los temas importantes de la guía.

No es obligatorio que todos los temas tengan exactamente el mismo número de preguntas.

La cantidad debe depender de:

- importancia del tema;
- cantidad de contenido;
- complejidad;
- objetivos de aprendizaje.

Pero siempre debe existir suficiente información para calcular un resultado por tema significativo.

---

# 40. Resultado y retroalimentación

El examen no debe limitarse a:

```text
72%
```

Debe responder:

```text
¿Qué tan bien lo hice?
¿Qué temas domino?
¿Qué temas necesito estudiar?
¿Dónde puedo repasar?
```

Por ello el resultado debe incluir:

```text
RESULTADO GENERAL
↓
RESULTADO POR TEMA
↓
TEMAS A REPASAR
↓
PREGUNTAS INCORRECTAS
↓
EXPLICACIONES
↓
ACCESO DIRECTO A LA GUÍA
```

---

# 41. Reintentar examen

Debe existir:

```text
🔄 Reintentar examen
```

El comportamiento debe:

1. Solicitar confirmación si existen respuestas.
2. Borrar las respuestas guardadas.
3. Desmarcar opciones.
4. Ocultar resultados.
5. Limpiar estados visuales.
6. Reiniciar progreso.
7. Regresar al inicio.

---

# 42. Historial de intentos

No es obligatorio para la primera versión.

Sin embargo, diseñar el código de manera que posteriormente sea posible guardar:

```json
{
  "fecha": "2026-10-01",
  "score": 72,
  "correctas": 18,
  "total": 25,
  "temas": {
    "tcp-ip": 90,
    "subnetting": 50,
    "routing": 70
  }
}
```

Por ahora basta con guardar el progreso actual.

---

# 43. Persistencia futura

La primera versión utiliza:

```text
localStorage
```

En una futura versión se podrá sustituir o complementar por:

```text
localStorage
        ↓
cuenta de usuario
        ↓
backend
        ↓
base de datos
```

No implementar esto todavía.

---

# 44. No duplicar lógica

Evitar generar JavaScript diferente para cada guía.

Preferir:

```text
guia.js
examen.js
```

reutilizables.

Los datos específicos de cada guía deben estar separados.

Ejemplo:

```javascript
const GUIDE_DATA = {...};
const EXAM_DATA = {...};
```

o datos embebidos equivalentes.

---

# 45. Resultado esperado del agente

Al recibir un documento/fuente para crear una guía, el agente debe producir automáticamente:

```text
1. Guía estructurada por temas
2. Ruta rápida
3. Navegación anterior/siguiente
4. Persistencia del último tema
5. Examen interactivo
6. Guardado automático de respuestas
7. Restauración del examen
8. Barra de progreso
9. Resultado final
10. Resultado por tema
11. Temas a repasar
12. Enlaces desde el examen hacia la guía
13. Botón para reintentar
14. Validación de consistencia
```

---

# 46. Flujo completo esperado

```text
FUENTE / PDF
      ↓
EXTRACCIÓN DE CONTENIDO
      ↓
ANÁLISIS DEL TEMARIO
      ↓
IDENTIFICACIÓN DE TEMAS
      ↓
GENERACIÓN DE CONTENIDO
      ↓
GENERACIÓN DE PREGUNTAS
      ↓
ASIGNACIÓN DE CADA PREGUNTA A UN TEMA
      ↓
VALIDACIÓN
      ↓
RENDERIZADO DE GUÍA
      ↓
RENDERIZADO DE EXAMEN
      ↓
SALIDA FINAL
```

---

# 47. Estructura final de archivos recomendada

Ejemplo:

```text
output/
│
└── redes/
    ├── guia.html
    └── examen.html
```

Si el proyecto actual requiere otra estructura, conservarla.

La prioridad es que el resultado sea fácil de abrir y compartir.

---

# 48. Criterios de aceptación

La implementación se considera correcta si:

### Guía

- [ ] La guía ya no se presenta como una única página interminable durante el estudio.
- [ ] Existe una Ruta rápida.
- [ ] Solo se muestra un tema a la vez.
- [ ] Se puede cambiar de tema sin recargar la página.
- [ ] Existe anterior/siguiente.
- [ ] Se guarda el último tema.
- [ ] Un hash como `#tema-subnetting` abre directamente el tema.
- [ ] En impresión se puede recuperar todo el contenido.

### Examen

- [ ] Se genera automáticamente junto con la guía.
- [ ] Tiene preguntas de opción múltiple.
- [ ] Cada pregunta tiene un tema.
- [ ] Se muestra el progreso.
- [ ] Las respuestas se guardan automáticamente.
- [ ] Las respuestas se restauran después de cerrar/abrir la página.
- [ ] Se calcula el resultado final.
- [ ] Se muestran respuestas correctas/incorrectas.
- [ ] Se muestran explicaciones.
- [ ] Se calcula resultado por tema.
- [ ] Se identifican temas a repasar.
- [ ] Se puede regresar directamente a esos temas.
- [ ] Se puede reiniciar el examen.

### Offline

- [ ] La guía funciona sin conexión.
- [ ] El examen funciona sin conexión.
- [ ] No depende de APIs externas.

### Calidad

- [ ] No existen IDs duplicados.
- [ ] No existen preguntas sin tema.
- [ ] No existen enlaces a temas inexistentes.
- [ ] No existen respuestas correctas ambiguas.
- [ ] El HTML generado es válido y funcional.

---

# 49. Orden recomendado de implementación

No intentar hacer todo simultáneamente.

## Fase 1 — Guía

Implementar:

1. Modelo de temas.
2. IDs de temas.
3. Ruta rápida.
4. Mostrar/ocultar temas.
5. Anterior/siguiente.
6. Progreso de guía.
7. Persistencia del último tema.
8. Hash de URL.

## Fase 2 — Examen

Implementar:

1. Generación automática de preguntas.
2. Etiqueta de tema.
3. Barra de progreso.
4. Resultado final.
5. Respuestas correctas/incorrectas.
6. Explicaciones.

## Fase 3 — Persistencia

Implementar:

1. Guardado en `localStorage`.
2. Restauración.
3. Reinicio controlado.

## Fase 4 — Análisis

Implementar:

1. Resultado por tema.
2. Temas a repasar.
3. Barras de dominio.
4. Enlaces examen → guía.

## Fase 5 — Pulido

Implementar:

1. Responsive.
2. Accesibilidad.
3. Impresión.
4. Optimización.
5. Validaciones automáticas.

---

# 50. Regla principal para el agente

**No cambiar el contenido educativo por mejorar la interfaz.**

La evolución debe ser principalmente:

```text
Mismo contenido
+
Mejor organización
+
Mejor navegación
+
Examen automático
+
Retroalimentación
+
Persistencia
```

El objetivo es transformar una guía larga en una **experiencia de estudio navegable**, manteniendo la generación automática y el funcionamiento offline.

---

# 51. Resultado visual deseado

La experiencia debe sentirse aproximadamente así:

```text
┌─────────────────────────────────────────────────────┐
│ 🎓 GUÍA DE REDES                                    │
│                                                     │
│ Progreso: Tema 3 de 10                              │
├─────────────────────────────────────────────────────┤
│ RUTA RÁPIDA                                         │
│                                                     │
│ [Inicio] [TCP/IP] [Subnetting] [Routing] [VPN]     │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│                  SUBNETTING                         │
│                                                     │
│  Explicación                                        │
│  ───────────────────────────────────────────────    │
│                                                     │
│  Ejemplo                                            │
│  ───────────────────────────────────────────────    │
│                                                     │
│  Puntos clave                                       │
│  ───────────────────────────────────────────────    │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│ ← Tema anterior                     Siguiente →     │
│                                                     │
├─────────────────────────────────────────────────────┤
│              📝 IR AL EXAMEN                        │
└─────────────────────────────────────────────────────┘
```

Y el examen:

```text
┌─────────────────────────────────────────────────────┐
│ 📝 EXAMEN — REDES                                  │
│                                                     │
│ Reactivos: 18 / 25                                 │
│ ██████████████░░░░░░░░░░                           │
│                                                     │
│ Pregunta 18                                         │
│ ¿Cuál...?                                           │
│                                                     │
│ ○ A. ...                                            │
│ ○ B. ...                                            │
│ ○ C. ...                                            │
│ ○ D. ...                                            │
│                                                     │
├─────────────────────────────────────────────────────┤
│                  [RESULTADOS]                       │
└─────────────────────────────────────────────────────┘
```

Resultado:

```text
┌─────────────────────────────────────────────────────┐
│                  RESULTADO                          │
│                                                     │
│                    72%                              │
│                  18 / 25                            │
│                                                     │
│ TCP/IP                                               │
│ ██████████████████░░ 90%                            │
│                                                     │
│ Subnetting                                           │
│ ██████████░░░░░░░░░░ 50%                            │
│                                                     │
│ Routing                                              │
│ ██████████████░░░░░░ 70%                            │
│                                                     │
│ 📚 TEMAS A REPASAR                                  │
│                                                     │
│ [Repasar Subnetting]                                │
│ [Repasar Routing]                                   │
│                                                     │
│ [🔄 Reintentar examen]                              │
└─────────────────────────────────────────────────────┘
```

---

# 52. Instrucción final para el agente

Implementa esta evolución **sobre la arquitectura existente**, evitando una reescritura completa.

Prioriza:

1. Funcionamiento.
2. Navegación.
3. Persistencia.
4. Relación guía/examen.
5. Retroalimentación por tema.
6. Diseño visual.
7. Optimización.

Cada modificación debe ser modular y reutilizable para que el siguiente material generado por el agente herede automáticamente estas capacidades.

**El resultado final debe permitir que una persona pueda estudiar un tema concreto rápidamente, realizar un examen, conocer su desempeño y regresar exactamente a los temas que necesita reforzar, sin perder el contenido ni depender de Internet.**
