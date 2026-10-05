# 🎓 Agente de Estudio y Exámenes — ParetoTutor Visual

Generador **local y offline** de **guías de estudio visuales + exámenes interactivos**, pensados para
personas con **memoria visual** que se preparan para exámenes universitarios, certificaciones
o entrevistas técnicas de TI.

Cada materia se entrega como **UN SOLO archivo HTML autocontenido** con alternador
📖 **Guía** ⇄ 📝 **Examen**: estudias por temas, te examinas al momento, tu progreso se guarda
solo y al final ves tu dominio **global y por tema** con enlaces de repaso. Sin frameworks,
sin backend, sin internet: **Python + HTML + CSS + JS vanilla**, imprimible a PDF.

> 💡 Filosofía: *evolucionar, no reemplazar*. El sistema parte de guías ya validadas
> (Probabilidad, SQL, Salesforce, Entrevista Técnica) y las lleva a un estándar común v2
> con base visual compartida y validación automática obligatoria antes de cada entrega.

---

## ✨ Qué hace (en 30 segundos)

1. **Analiza tu material** — exámenes reales, apuntes, PDFs o libros en `Matería/<Nombre>/`.
2. **Prioriza con Pareto** — detecta el 20% de temas que concentran el 80% de los puntos.
3. **Genera la guía visual** — conceptos, trampas, ejemplos, fórmulas y repaso activo,
   todo con código de colores y bloques de 3 capas sobre fondo oscuro `#0F172A`.
4. **Genera el examen interactivo** — opción múltiple que **corrige cada pregunta al momento**,
   **guarda tu avance** en el navegador y te dice **qué temas repasar**.
5. **Valida antes de entregar** — ningún archivo se publica sin pasar el verificador (`APROBADO ✔`).

### 🧠 Pedagogía incorporada

`Concepto → Ejemplo → Práctica → Repaso activo → Quiz → Simulación`, con:

- 🔵 **Azul** — definiciones y conceptos clave.
- 🔴 **Rojo** — trampas, errores comunes y advertencias del examen.
- 🟢 **Verde** — ejemplos resueltos paso a paso.
- 🟠 **Naranja** — fórmulas, reglas de oro y *cheat sheets*.
- 🗺️ **Mapa/flujo** — diagramas, árboles de decisión y tablas "qué usar según qué piden".
- 🧠 **Recall** — preguntas de repaso activo con respuesta oculta (`<details>`).

Cada tema cierra con **árbol de decisión + tabla de notación/símbolos + 2 preguntas
de repaso activo**, y cada guía con **simulacro final**.

---

## 🗂️ Estructura del repositorio

| Ruta | Qué es y por qué importa |
|---|---|
| `Inicio/` | **Cerebro del agente — punto de entrada.** Empieza por `LEEME.md`: `agent.md` (rol, formato v2, comandos), `flujo_trabajo.md` (fases 1-4), `plantilla_salida.md` (plantilla por tema), `reglas_estilo_visual.md` (paleta 3 capas), `estado_actual.md` (resumen vivo para retomar), `memoria_sesion.md` (historial detallado). |
| `src/estilo_base.py` | **Base visual única v2.** CSS compartido + helpers Python (`HERO`, `B`, `TAB`, `LI`, `PRE`, `RECALL`). Evita que cada generador reinvente el diseño. |
| `src/examen_v2.js` | **Motor de examen v2.** Corrección inmediata 🟢/🔴 + justificación, guardado en `localStorage` (`ex_<materia>_respuestas`), restauración al reabrir, barra de progreso fija, resultado global + dominio por tema, panel "Temas a repasar" con salto a la guía, botón reintentar con confirmación. |
| `src/gen_guia_examen_v2.py` | **Generador combinado actual.** Une guía + examen en un solo HTML (contenido Entrevista Técnica: 12 temas + 38 preguntas). Es el modelo a replicar por materia. |
| `src/verify_v2.py` | **Validador obligatorio FASE 4.** Revisa balance HTML, vistas guía/examen, alternador, IDs únicos, anclas, radios 4×, feedback por pregunta, motor JS, JSON válido y que cada pregunta apunte a un tema existente. |
| `src/gen_visual.py`, `src/gen_visual_sql.py`, `src/gen_visual_entrevista.py` | Generadores legacy de guías (Probabilidad, SQL, Entrevista). Se migrarán a la base v2. |
| `src/gen_examenes_interactivos.py`, `src/gen_examenes_salesforce.py` | Generadores legacy de exámenes (Probabilidad 34 preg., Salesforce 60 preg.). |
| `src/verify_final.py`, `src/verify_salesforce.py` | Validadores legacy. |
| `Guias terminadas/` | **Entregables listos.** Abre cualquier `.html` en el navegador, sin instalar nada. |
| `docs/Especificacion_Agente_Guias_Examenes.md` | Especificación del sistema guía + examen (navegación por temas, examen con estado, validaciones). |
| `docs/Plan_Plataforma_Estudio_TI.md` | Roadmap futuro (rutas, plataforma, cuentas, premium). **Fuera del alcance actual.** |

> 🔒 **Privacidad y legal:** la carpeta `Matería/` (PDFs, libros, fotos de exámenes),
> los `_extract_*.txt` y los `__pycache__/` **no se versionan** (ver `.gitignore`).
> Contienen material con copyright y datos personales: cada usuario coloca allí su propio
> material **solo en local**. Lo que sí se publica es el *motor* y las *guías generadas*.

---

## 🚀 Uso

### Requisitos

- **Python 3.10+** (probado en 3.13). Sin dependencias externas para el sistema v2
  (solo librería estándar). Los generadores legacy de Probabilidad usan `matplotlib`
  para las gráficas embebidas.
- Un **navegador moderno** (Chrome, Edge, Firefox) para abrir las guías. No se necesita servidor.

### Uso rápido (consumir una guía)

1. Abre `Guias terminadas/Guia_Examen_Entrevista_Tecnica.html` con doble clic.
2. Estudia en la vista 📖 **Guía** (navega por la "Ruta rápida" de temas).
3. Cambia a 📝 **Examen** con el botón superior. Responde: cada pregunta se corrige
   **al momento** (🟢 correcta / 🔴 incorrecta + justificación con código de colores).
4. Puedes cerrar la pestaña: tu progreso **se conserva** (localStorage).
5. Al terminar, pulsa **✓ Ver resultados**: verás tu % global, tu dominio **por tema**
   (≥80% dominado · 60-79% reforzar · <60% repasar) y botones **📖 Repasar** que te
   llevan al tema exacto de la guía. **🔄 Reintentar** borra el intento (con confirmación).
6. Para papel: `Ctrl+P` → imprime a PDF (el CSS `@media print` muestra todo el contenido).

```bash
# Regenerar la guía + examen del piloto (sistema v2)
python src/gen_guia_examen_v2.py
---

## 🔄 Cómo crear una guía de una materia nueva (flujo del agente)

El agente trabaja en 4 fases (`Inicio/flujo_trabajo.md`). Resumen para humanos:

| Fase | Comando | Qué pasa |
|---|---|---|
| **1. Ingesta y análisis** | `/analizar [Materia]` | Colocas exámenes/fotos en `Matería/[Materia]/imagenes de examenes/` y libros en `.../libros/`. El agente extrae temas y devuelve tabla de frecuencias. |
| **2. Consolidación** | `/estado` | Calcula el Top 20% Pareto y **clasifica la materia**: **Tipo A** (cuantitativa: Probabilidad), **Tipo B** (herramienta: SQL, Docker), **Tipo C** (conceptual/puesto: Entrevista, ISO). Cada tipo usa su variante de plantilla. |
| **3. Producción** | `/generar_guia_visual [Materia]` | Genera con Python **UN SOLO HTML** (guía navegable por `<h2 id="tema-slug">` + examen v2 con JSON embebido) usando `src/estilo_base.py` + `src/examen_v2.js`, y lo guarda en `Guias terminadas/`. |
| **4. Validación** | automática | Ejecuta `python src/verify_v2.py` y corrige **todo** hasta `APROBADO ✔`. Nunca se entrega sin validar. |

### ✍️ Cómo añadir contenido a mano (avanzado)

El generador v2 separa **contenido → ensamblado**:
- `TEMAS = [(slug, título, prioridad, html), ...]` — cada tema usa helpers `EB.B/TAB/LI/PRE/RECALL`.
- `PREGUNTAS = [(id, slug_tema, etiqueta, enunciado, [4 opciones], índice_correcto, justificación), ...]` — el `slug_tema` **debe existir** en `TEMAS` (el validador lo exige) y cada justificación usa el código 🔵🟢🟠⚠️.
- `build_guia()` + `build_examen()` ensamblan las vistas; `build_html()` inyecta CSS + JS + JSON y escribe el HTML final.

### 📁 Dónde poner tu material (local, no versionado)

```text
Matería/
└── <NombreMateria>/
---

## 📚 Materias y entregables incluidos

| Materia | Tipo | Entregable(s) | Contenido |
|---|---|---|---|
| **Entrevista Técnica TI** ⭐ (sistema v2) | C | `Guia_Examen_Entrevista_Tecnica.html` | 12 temas + 38 preguntas. Soporte, Redes, Ciberseguridad, IAM, SQL, Python, Full-Stack, Git/Docker, IA/agentes, ISO 27001, GCP/Workspace, M365. Corrección inmediata + guardado + dominio por tema. |
| **Entrevista Técnica TI** (legacy) | C | `Guia_Visual_Entrevista_Tecnica.html` | 21 secciones + 40 preguntas con respuestas modelo. Versión anterior sin motor v2. |
| **Probabilidad y Estadística** | A | `Guia_Visual_Probabilidad.html` + `Guia_Probabilidad.md` + `Examenes_Interactivos_Probabilidad.html` + `Examen_Practica_Probabilidad.md` | Bayes, Binomial, Normal, Exponencial, Poisson, V.A. discreta/continua. 34 preguntas con soluciones paso a paso y gráficas `matplotlib`. |
| **SQL Server (T-SQL)** | B | `Guia_Visual_SQL.html` + `Examen_SQL_Resuelto.md` | DDL/DML/DCL, JOINs, triggers, stored procedures, vistas, transacciones. 60 preguntas resueltas. |
| **Salesforce FSC + Slack** | B/C | `Examenes_Interactivos_Salesforce.html` | 60 reactivos balanceados A–D con justificación por colores y árbol de decisión. |

**Estado de migración v2:** Entrevista Técnica ✅ · SQL ⏳ · Probabilidad ⏳ · Salesforce ⏳.
Las guías legacy se conservan hasta ser revalidadas con `verify_v2.py`.

---

## 🗺️ Roadmap

- [x] Base visual compartida + motor de examen v2 + validación obligatoria.
- [x] Piloto Entrevista Técnica (12 temas, 38 preguntas).
- [ ] Migrar SQL, Probabilidad y Salesforce al sistema v2 (Fase 5).
- [ ] Curso piloto "Redes TCP/IP" como ruta navegable (ver `docs/Plan_Plataforma_Estudio_TI.md`).
- 🔮 Futuro (fuera de alcance): plataforma con rutas, cuentas y premium — solo con contenido propio o licenciado (ver sección legal).

### ⚖️ Nota legal

Las guías actuales derivan en parte de materiales de terceros (libros, capacitaciones,
exámenes reales) y se publican con fin **educativo/personal**. Antes de cualquier uso
comercial o monetización: sustituir por **contenido original**, obtener licencias o
asesoría de copyright. Ver `Inicio/memoria_sesion.md` (sección publicación) y
`docs/Plan_Plataforma_Estudio_TI.md`.

---

## 🤝 Contribuir

1. Crea tu rama: `git checkout -b feat/mi-materia`.
2. Añade tu generador o contenido siguiendo el formato v2 (`TEMAS` + `PREGUNTAS` + helpers `EB.*`).
3. Valida: `python src/verify_v2.py` debe dar **APROBADO ✔**.
4. Haz commit y push; abre PR a `main` describiendo materia, nº de temas/preguntas y resultado del validador.
    ├── imagenes de examenes/   ← fotos / .md de exámenes reales
    └── libros/                 ← PDFs de referencia
```
# → Guias terminadas/Guia_Examen_Entrevista_Tecnica.html (12 temas, 38 preguntas)

# Validar antes de entregar (OBLIGATORIO — FASE 4)
python src/verify_v2.py
# → RESULTADO: APROBADO ✔ (o lista de fallos a corregir)
```
