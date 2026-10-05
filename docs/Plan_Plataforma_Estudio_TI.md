# Plataforma de Estudio y Preparación para Entrevistas TI

## 1. Visión del proyecto

La plataforma busca evolucionar de una colección de guías HTML
enriquecidas a una **plataforma educativa interactiva**, enfocada
inicialmente en estudiantes y personas que se preparan para entrevistas
de TI.

El objetivo no es desechar el sistema actual, sino evolucionarlo
progresivamente:

``` text
PDF / Fuentes
     ↓
Extracción con Python
     ↓
Contenido estructurado (Markdown / JSON)
     ↓
Generadores Python
     ↓
Plantillas HTML
     ↓
Web educativa interactiva
     ↓
Backend + cuentas + progreso
     ↓
Monetización
```

### Objetivos principales

-   Facilitar el aprendizaje mediante rutas estructuradas.
-   Convertir contenido teórico en experiencias de aprendizaje
    interactivas.
-   Permitir práctica mediante preguntas y simulaciones.
-   Registrar el progreso del usuario.
-   Mantener un modo offline/impresión a PDF.
-   Preparar la plataforma para futuras cuentas de usuario.
-   Permitir una futura modalidad gratuita y premium.
-   Mantener buen rendimiento en equipos y dispositivos móviles.

------------------------------------------------------------------------

# 2. Estado actual

Actualmente el proyecto utiliza:

-   Python 3.13.
-   Scripts `.py` para generar contenido.
-   Markdown para guías y exámenes.
-   `pypdf` para extracción de información.
-   Matplotlib para gráficas.
-   HTML5 + CSS3.
-   JavaScript vanilla.
-   HTML autocontenido.
-   Diseño orientado a lectura y PDF.
-   Preguntas interactivas mediante JavaScript.
-   `localStorage` como posible mecanismo inicial para guardar progreso.

### Características actuales

-   Tema oscuro.
-   Navegación mediante índice/TOC.
-   Bloques visuales de información.
-   Tarjetas mediante clases CSS.
-   Preguntas mediante `<details><summary>`.
-   Simulacro/interactividad.
-   Gráficas incrustadas mediante Base64.
-   Diseño sin dependencias pesadas.
-   Funcionamiento offline.

### Problema principal identificado

El principal cuello de botella no es el tamaño del HTML ni el
rendimiento bruto.

El problema principal es la **arquitectura de navegación y presentación
del contenido**.

Actualmente el proyecto se parece más a:

> Documento HTML enriquecido.

La evolución buscada es:

> Plataforma educativa estructurada.

------------------------------------------------------------------------

# 3. Nueva experiencia del usuario

La plataforma debería organizarse alrededor de una ruta de aprendizaje.

## Flujo propuesto

``` text
Inicio
  ↓
Dashboard
  ↓
Ruta de aprendizaje
  ↓
Curso / Área
  ↓
Módulo
  ↓
Lección
  ↓
Teoría
  ↓
Ejemplo
  ↓
Práctica
  ↓
Preguntas
  ↓
Quiz
  ↓
Simulación
  ↓
Progreso
```

------------------------------------------------------------------------

# 4. Dashboard

El Dashboard será la pantalla principal del usuario.

## Elementos principales

### Hero

Mensaje principal:

> Prepárate para tu próxima entrevista de TI.

Debe mostrar:

-   Objetivo de aprendizaje.
-   Progreso general.
-   Acción principal.
-   Curso o módulo actual.

### Continuar estudiando

Mostrar:

-   Último módulo visitado.
-   Porcentaje completado.
-   Próxima lección.
-   Botón para continuar.

Ejemplo:

``` text
┌───────────────────────────────────────┐
│ Continuar estudiando                  │
│ Redes - TCP/IP                        │
│ ███████████████░░░░ 72%               │
│                                       │
│ [ Continuar lección ]                 │
└───────────────────────────────────────┘
```

### Rutas de aprendizaje

Ejemplo:

``` text
Soporte TI
████████░░ 80%

Redes
██████░░░░ 60%

Ciberseguridad
████░░░░░░ 40%

Cloud
██░░░░░░░░ 20%
```

------------------------------------------------------------------------

# 5. Organización del contenido

El contenido debe dividirse progresivamente.

## Nivel 1 --- Área

Ejemplos:

-   Soporte TI
-   Redes
-   Ciberseguridad
-   IAM
-   Cloud
-   Microsoft 365
-   Hardware
-   SQL
-   Python
-   Full Stack
-   Git / Docker
-   IA
-   ISO
-   Jira

## Nivel 2 --- Curso

Ejemplo:

``` text
Redes
└── Fundamentos de redes
└── TCP/IP
└── Routing
└── Switching
└── VPN
└── Troubleshooting
```

## Nivel 3 --- Módulo

Cada módulo contiene varias lecciones.

## Nivel 4 --- Lección

Cada lección debería seguir una estructura consistente:

``` text
Concepto
   ↓
Explicación
   ↓
Ejemplo
   ↓
Aplicación práctica
   ↓
Pregunta de recuperación
   ↓
Quiz
```

------------------------------------------------------------------------

# 6. Modelo de aprendizaje

La plataforma debe priorizar aprendizaje activo.

## Estructura recomendada

### 1. Concepto

Explicación breve y clara.

### 2. Ejemplo

Aplicación del concepto en un escenario real.

### 3. Práctica

Ejercicio que obligue al usuario a aplicar el conocimiento.

### 4. Active Recall

Preguntas para recordar sin consultar inmediatamente la respuesta.

### 5. Quiz

Evaluación automática.

### 6. Simulación

Escenario similar a una entrevista o problema real de TI.

------------------------------------------------------------------------

# 7. Sistema de progreso

Se propone utilizar cuatro estados:

  Estado        Significado
  ------------- --------------------------------------------------
  No iniciado   El usuario todavía no estudia el contenido
  En progreso   El usuario comenzó el contenido
  Completado    Terminó la lección
  Dominado      Superó satisfactoriamente la práctica/evaluación

## Ejemplo

``` text
TCP/IP

✓ Conceptos básicos
✓ Modelo TCP/IP
✓ Direccionamiento IP
→ Subnetting
○ Routing
○ Troubleshooting
```

------------------------------------------------------------------------

# 8. Persistencia inicial

En la primera etapa se puede utilizar:

``` javascript
localStorage
```

para guardar:

-   Lecciones visitadas.
-   Progreso.
-   Resultados de quizzes.
-   Última posición.
-   Preferencias básicas.

Esto permite desarrollar la experiencia sin necesidad inmediata de
backend.

Posteriormente:

``` text
localStorage
      ↓
API
      ↓
Base de datos
```

permitirá sincronizar el progreso entre dispositivos.

------------------------------------------------------------------------

# 9. Sistema de quizzes

El sistema actual de preguntas interactivas puede evolucionar hacia una
experiencia más completa.

## Interfaz propuesta

``` text
Pregunta 4 de 10

¿Cuál es la función principal de DNS?

○ Asignar direcciones MAC
○ Resolver nombres de dominio
○ Cifrar tráfico
○ Administrar usuarios

[ Responder ]

████████████░░░░░░ 40%
```

Después de responder:

``` text
✓ Respuesta correcta

DNS permite resolver nombres de dominio
a direcciones IP.

[ Siguiente pregunta ]
```

## Elementos

-   Número de pregunta.
-   Progreso.
-   Opciones.
-   Validación.
-   Explicación.
-   Puntuación.
-   Resultado final.
-   Opción para repetir.

------------------------------------------------------------------------

# 10. Simulaciones

La simulación debe acercarse a situaciones reales de trabajo.

## Ejemplo

``` text
ESCENARIO

Un usuario informa que no tiene conexión
a Internet.

¿Qué revisarías primero?

A) Reinstalar Windows
B) Verificar conexión física y configuración IP
C) Cambiar el equipo
D) Formatear el disco
```

Después de responder:

-   Mostrar razonamiento.
-   Explicar por qué.
-   Mostrar procedimiento recomendado.
-   Relacionar con conocimientos anteriores.

Esto permite evaluar **criterio técnico**, no solamente memoria.

------------------------------------------------------------------------

# 11. Diseño visual

## Paleta propuesta

``` text
Background principal: #0B1120
Background secundario: #111827
Cards:                #172033
Borders:              #263449

Texto principal:      #F8FAFC
Texto secundario:     #94A3B8

Primary:              #38BDF8
Success:              #22C55E
Warning:              #F59E0B
Error:                #EF4444
Accent:               #6366F1
```

## Uso semántico

Los colores deben comunicar significado.

``` text
Azul      → Información / navegación
Verde     → Correcto / completado
Amarillo  → Advertencia / atención
Rojo      → Error / riesgo
Morado    → Elementos especiales
```

No utilizar los colores únicamente como decoración.

------------------------------------------------------------------------

# 12. Tipografía

Mantener una fuente del sistema para evitar dependencias innecesarias.

Propuesta:

``` css
font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
```

Ventajas:

-   Menor carga.
-   Buena compatibilidad.
-   Sin dependencia de fuentes externas.
-   Buen rendimiento.

------------------------------------------------------------------------

# 13. Componentes visuales

Los bloques actuales como:

``` text
.bloque
.b-azul
.b-verde
.b-rojo
.b-naranja
```

pueden evolucionar hacia componentes consistentes.

Ejemplo:

``` text
┌────────────────────────────────────┐
│ CONCEPTO                            │
│                                    │
│ Explicación del concepto...        │
│                                    │
│ Ejemplo práctico...                │
└────────────────────────────────────┘
```

Componentes futuros:

-   Cards.
-   Alertas.
-   Progress bars.
-   Badges.
-   Quiz cards.
-   Flashcards.
-   Tabs.
-   Accordions.
-   Timeline.
-   Code blocks.
-   Simulaciones.

------------------------------------------------------------------------

# 14. Navegación

El índice actual es funcional, pero debe evolucionar.

## Desktop

Sidebar o navegación lateral.

``` text
┌──────────────┬───────────────────────────┐
│ Curso        │                           │
│              │       Contenido           │
│ ✓ Módulo 1   │                           │
│ ✓ Módulo 2   │                           │
│ → Módulo 3   │                           │
│ ○ Módulo 4   │                           │
│              │                           │
└──────────────┴───────────────────────────┘
```

## Mobile

Convertir la navegación en:

-   Menú desplegable.
-   Drawer.
-   Índice colapsable.

El TOC actual de dos columnas debe convertirse en una sola columna en
pantallas pequeñas.

------------------------------------------------------------------------

# 15. Responsive Design

Debe existir una estrategia específica para:

-   Desktop.
-   Laptop.
-   Tablet.
-   Smartphone.

## Ajustes móviles

### Grids

De:

``` css
grid-template-columns: repeat(2, 1fr);
```

a:

``` css
grid-template-columns: 1fr;
```

### TOC

De:

``` css
column-count: 2;
```

a:

``` css
column-count: 1;
```

### Tablas

Permitir desplazamiento horizontal:

``` css
overflow-x: auto;
```

### Texto

Reducir tamaños de títulos y espacios sin sacrificar legibilidad.

------------------------------------------------------------------------

# 16. Arquitectura técnica propuesta

Actualmente el contenido y la presentación están demasiado unidos.

La siguiente etapa debe separar:

``` text
Contenido
Presentación
Lógica
Assets
Generación
```

## Estructura propuesta

``` text
/project
│
├── generators/
│   ├── generar_guias.py
│   ├── generar_examenes.py
│   └── generar_indice.py
│
├── content/
│   ├── soporte.json
│   ├── redes.json
│   ├── seguridad.json
│   ├── sql.json
│   └── python.json
│
├── templates/
│   └── guia.html
│
├── assets/
│   ├── css/
│   │   └── app.css
│   │
│   ├── js/
│   │   ├── app.js
│   │   ├── quiz.js
│   │   ├── progress.js
│   │   └── search.js
│   │
│   └── img/
│
└── dist/
    ├── index.html
    ├── soporte.html
    ├── redes.html
    └── seguridad.html
```

------------------------------------------------------------------------

# 17. Python como generador

No es necesario abandonar Python.

Python puede continuar siendo el núcleo de generación.

``` text
Fuentes
   ↓
Python
   ↓
Procesamiento
   ↓
JSON / Markdown
   ↓
Template
   ↓
HTML
```

Esto permite:

-   Automatizar contenido.
-   Regenerar cursos.
-   Crear exámenes.
-   Crear índices.
-   Crear estadísticas.
-   Mantener consistencia.

------------------------------------------------------------------------

# 18. Separación de CSS

Actualmente el CSS está incrustado en el HTML.

Para la versión web se recomienda:

``` text
assets/css/app.css
```

Ventajas:

-   Caché del navegador.
-   Menos HTML repetido.
-   Mantenimiento más sencillo.
-   Cambios globales más rápidos.

Sin embargo, debe mantenerse una opción de generación:

``` text
Web → CSS externo
Offline/PDF → CSS incrustado
```

------------------------------------------------------------------------

# 19. JavaScript

No es necesario migrar inmediatamente a React, Vue o Next.js.

El JavaScript vanilla actual es suficiente para la primera evolución.

Se puede modularizar:

``` text
app.js
quiz.js
progress.js
search.js
auth.js
```

Utilizar:

``` html
<script type="module">
```

o:

``` html
<script defer>
```

cuando corresponda.

La migración a un framework puede evaluarse posteriormente si la
complejidad del producto realmente lo requiere.

------------------------------------------------------------------------

# 20. Optimización de imágenes

Actualmente las gráficas de Matplotlib se pueden insertar como Base64.

Esto es útil para:

-   HTML autocontenido.
-   Uso offline.
-   Generación de PDF.

Pero para una plataforma web se recomienda generar archivos
independientes:

``` text
PNG
↓
WebP / SVG
```

y utilizarlos como assets.

## Estrategia híbrida

### Web

``` text
HTML
+
CSS
+
JS
+
WebP/SVG
```

### Offline/PDF

``` text
HTML autocontenido
+
Base64
```

De esta manera no se pierde la capacidad offline.

------------------------------------------------------------------------

# 21. Carga de imágenes

Para imágenes que no son críticas:

``` html
<img
    src="imagen.webp"
    loading="lazy"
    decoding="async"
>
```

No aplicar lazy loading a una imagen principal que sea parte del
contenido visible inicialmente.

Cuando corresponda, utilizar:

``` html
fetchpriority="high"
```

para el recurso principal.

------------------------------------------------------------------------

# 22. Búsqueda interna

Una característica importante será incorporar búsqueda.

## Propuesta

Generar:

``` text
search-index.json
```

con información como:

``` json
{
  "title": "TCP/IP",
  "module": "Redes",
  "url": "/curso/redes/tcp-ip.html",
  "keywords": [
    "tcp",
    "ip",
    "networking"
  ]
}
```

El navegador puede realizar una búsqueda local sin necesidad inicial de
backend.

------------------------------------------------------------------------

# 23. Modularización del contenido

Evitar una única página HTML gigantesca.

En lugar de:

``` text
guia-completa.html
```

utilizar:

``` text
/curso/
    soporte.html
    redes.html
    ciberseguridad.html
    iam.html
    cloud.html
    microsoft365.html
    hardware.html
    sql.html
    python.html
```

Posteriormente se puede dividir todavía más:

``` text
/curso/redes/
    fundamentos.html
    tcp-ip.html
    subnetting.html
    routing.html
    troubleshooting.html
```

------------------------------------------------------------------------

# 24. Rendimiento

El HTML actual no necesita una optimización extrema si ronda decenas de
KB.

Las prioridades deberían ser:

1.  Arquitectura.
2.  Navegación.
3.  Modularización.
4.  Assets reutilizables.
5.  Optimización de imágenes.
6.  Caché.
7.  JavaScript eficiente.
8.  Compresión.
9.  Minificación cuando tenga sentido.

No sacrificar legibilidad del código únicamente por reducir unos KB.

------------------------------------------------------------------------

# 25. Accesibilidad

La plataforma debe considerar desde el inicio:

-   Contraste adecuado.
-   Navegación mediante teclado.
-   Labels correctos.
-   Estados de foco visibles.
-   Uso correcto de headings.
-   `aria-*` cuando sea necesario.
-   Mensajes de error comprensibles.
-   No depender únicamente del color.

También considerar:

``` css
@media (prefers-reduced-motion: reduce) {
    /* reducir o desactivar animaciones */
}
```

------------------------------------------------------------------------

# 26. Arquitectura futura con backend

Cuando se necesiten cuentas y sincronización:

``` text
Frontend
    ↓
API
    ↓
Backend
    ↓
Base de datos
```

Una opción natural para el backend, debido al uso actual de Python,
sería evaluar:

``` text
FastAPI
```

La decisión definitiva puede hacerse posteriormente.

------------------------------------------------------------------------

# 27. Modelo de datos inicial

Entidades principales:

``` text
users
courses
modules
lessons
questions
quiz_attempts
progress
subscriptions
entitlements
```

Relación conceptual:

``` text
User
 │
 ├── Progress
 ├── Quiz Attempts
 └── Subscription
          │
          └── Entitlements

Course
 │
 └── Module
       │
       └── Lesson
             │
             └── Questions
```

------------------------------------------------------------------------

# 28. Autenticación

Cuando exista backend:

-   Contraseñas almacenadas mediante hashes seguros.
-   No almacenar contraseñas en texto plano.
-   Evaluar Argon2id o bcrypt.
-   Sesiones seguras.
-   Cookies `HttpOnly`.
-   Cookies `Secure`.
-   Política `SameSite`.
-   Expiración de sesiones.
-   Revocación de sesiones.
-   Protección CSRF cuando corresponda.

------------------------------------------------------------------------

# 29. Protección del contenido premium

Una regla fundamental:

> Ocultar contenido premium con CSS o JavaScript no constituye una
> protección real.

Si el contenido premium ya fue enviado al navegador, técnicamente puede
ser recuperado.

La arquitectura correcta será:

``` text
Usuario
   ↓
Autenticación
   ↓
Backend
   ↓
Verificación de entitlement
   ↓
¿Tiene acceso?
   ├── Sí → entregar contenido
   └── No → 403 / Paywall
```

El servidor debe decidir qué contenido puede recibir cada usuario.

------------------------------------------------------------------------

# 30. Control de sesiones

Para reducir el uso compartido de cuentas se pueden considerar:

-   Límite razonable de sesiones simultáneas.
-   Registro de sesiones.
-   Identificación de dispositivos/sesiones.
-   Revocación manual.
-   Detección de patrones anómalos.

Evitar implementar DRM excesivo.

------------------------------------------------------------------------

# 31. Modelo de monetización

Se propone inicialmente un modelo:

> Freemium + contenido premium.

## Contenido gratuito

Podría incluir:

-   Conceptos básicos.
-   Algunos módulos.
-   Número limitado de preguntas.
-   Simulación básica.
-   Algunas descargas.

## Contenido premium

Podría incluir:

-   Todos los módulos.
-   Banco completo de preguntas.
-   Simulaciones ilimitadas.
-   Progreso sincronizado.
-   Rutas de aprendizaje.
-   Estadísticas.
-   Certificados.
-   Descargas completas.

------------------------------------------------------------------------

# 32. Posibles modelos comerciales

No es necesario decidir los precios todavía.

Se pueden evaluar:

### Suscripción mensual

``` text
Acceso continuo
```

### Compra individual

``` text
Comprar un módulo/curso
```

### Bundle

``` text
Paquete de varios cursos
```

### Modelo híbrido

``` text
Contenido gratuito
+
Cursos premium
+
Paquetes
```

La elección debe hacerse después de validar qué contenido genera mayor
valor para los usuarios.

------------------------------------------------------------------------

# 33. Funciones futuras

Una vez establecida la base técnica se pueden incorporar:

-   Flashcards.
-   Preguntas adaptativas.
-   Retos diarios.
-   Rachas de estudio.
-   Logros.
-   Estadísticas.
-   Ranking personal.
-   Simulaciones de entrevistas.
-   Certificados.
-   Historial de resultados.
-   Recomendaciones de estudio.
-   Rutas personalizadas.
-   Recordatorios.
-   Panel administrativo.
-   Gestión de contenido.
-   Analytics.

------------------------------------------------------------------------

# 34. Roadmap de desarrollo

## Fase 1 --- Rediseño visual

Objetivo:

Convertir el documento actual en una experiencia de estudio más clara.

### Tareas

-   Crear Dashboard.
-   Crear tarjetas de cursos.
-   Mejorar navegación.
-   Mejorar responsive.
-   Definir sistema visual.
-   Mejorar componentes.
-   Mejorar quizzes.

------------------------------------------------------------------------

## Fase 2 --- Arquitectura

Objetivo:

Separar contenido, presentación y lógica.

### Tareas

-   Separar CSS.
-   Modularizar JavaScript.
-   Separar contenido.
-   Crear templates.
-   Crear generadores.
-   Dividir contenido en páginas.
-   Crear assets reutilizables.

------------------------------------------------------------------------

## Fase 3 --- Optimización

Objetivo:

Mejorar rendimiento y mantenibilidad.

### Tareas

-   Convertir imágenes.
-   Eliminar Base64 de la versión web.
-   Implementar caché.
-   Optimizar carga.
-   Lazy loading.
-   Compresión.
-   Minificación cuando sea conveniente.
-   Search index.

------------------------------------------------------------------------

## Fase 4 --- Progreso

Objetivo:

Permitir que el usuario mantenga su avance.

### Primera versión

``` text
localStorage
```

### Segunda versión

``` text
Cuenta
↓
API
↓
Base de datos
```

------------------------------------------------------------------------

## Fase 5 --- Backend

Objetivo:

Convertir la plataforma en un producto multiusuario.

### Tareas

-   API.
-   Usuarios.
-   Autenticación.
-   Cursos.
-   Lecciones.
-   Preguntas.
-   Progreso.
-   Sesiones.
-   Entitlements.

------------------------------------------------------------------------

## Fase 6 --- Monetización

### Tareas

-   Definir contenido gratuito.
-   Definir contenido premium.
-   Sistema de pagos.
-   Suscripciones.
-   Entitlements.
-   Paywall.
-   Gestión de acceso.

------------------------------------------------------------------------

## Fase 7 --- Producto educativo

Agregar:

-   Flashcards.
-   Simulaciones.
-   Retos.
-   Estadísticas.
-   Logros.
-   Certificados.
-   Rutas personalizadas.

------------------------------------------------------------------------

# 35. Prioridades recomendadas

Orden de implementación:

``` text
1. Dashboard
2. Organización por módulos
3. Mobile UX
4. Separación contenido/template
5. Sistema de búsqueda
6. Progreso local
7. Quiz mejorado
8. Optimización de imágenes
9. Backend
10. Autenticación
11. Monetización
12. Analytics
```

------------------------------------------------------------------------

# 36. Principio de evolución

No se debe reconstruir todo desde cero.

El proyecto actual ya proporciona una base funcional:

``` text
Python
Markdown
HTML
CSS
JavaScript
Matplotlib
```

La estrategia debe ser:

``` text
EVOLUCIONAR
    ↓
NO REEMPLAZAR INMEDIATAMENTE
```

La infraestructura actual puede convertirse progresivamente en una
plataforma más robusta.

------------------------------------------------------------------------

# 37. Arquitectura objetivo

``` text
                    ┌───────────────────┐
                    │      USUARIO      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    FRONTEND WEB   │
                    │                   │
                    │ Dashboard         │
                    │ Cursos            │
                    │ Lecciones         │
                    │ Quiz              │
                    │ Simulaciones      │
                    │ Progreso          │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │       API         │
                    └─────────┬─────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
       ┌────────────┐  ┌────────────┐  ┌────────────┐
       │ Usuarios   │  │ Contenido  │  │ Progreso   │
       └────────────┘  └────────────┘  └────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    Base de datos  │
                    └───────────────────┘
```

------------------------------------------------------------------------

# 38. Principio general del producto

La plataforma debe dejar de pensar únicamente en:

> "¿Cómo mostrar una guía?"

y empezar a pensar en:

> "¿Cómo ayudar al usuario a aprender, practicar, comprobar y demostrar
> que domina un tema?"

La diferencia fundamental está en pasar de **contenido** a **experiencia
de aprendizaje**.

------------------------------------------------------------------------

# 39. MVP recomendado

La primera versión realmente útil de la plataforma no necesita backend
ni pagos.

El MVP puede contener:

``` text
Dashboard
   ↓
Cursos
   ↓
Módulos
   ↓
Lecciones
   ↓
Preguntas
   ↓
Quiz
   ↓
Progreso local
```

Tecnologías:

``` text
Python
HTML
CSS
JavaScript Vanilla
JSON
localStorage
```

Esto permite validar la experiencia antes de invertir en:

``` text
Backend
Base de datos
Autenticación
Pagos
Infraestructura
```

------------------------------------------------------------------------

# 40. Criterio para futuras decisiones técnicas

Antes de agregar una nueva tecnología, responder:

1.  ¿Resuelve un problema real?
2.  ¿Mejora la experiencia del usuario?
3.  ¿Mejora el mantenimiento?
4.  ¿Mejora el rendimiento?
5.  ¿Es necesaria en esta etapa?
6.  ¿Aumenta considerablemente la complejidad?

Si la respuesta es no, mantener la solución actual.

------------------------------------------------------------------------

# 41. Meta final

La evolución propuesta es:

``` text
GUÍAS
  ↓
GUÍAS INTERACTIVAS
  ↓
PLATAFORMA DE ESTUDIO
  ↓
PLATAFORMA CON CUENTAS
  ↓
PLATAFORMA PREMIUM
```

La ventaja principal del proyecto actual es que ya existe una cantidad
importante de contenido y un sistema automatizado de generación.

La prioridad debe ser convertir ese contenido en una **experiencia de
aprendizaje organizada, medible y escalable**.
