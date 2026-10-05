# Tracker de Avance Visual por Materia

**Directorio Base:** `C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\`
**Materia Actual:** PROBABILIDAD

**Checklist de Ingesta:**
- [x] Fotos de exámenes analizadas (10 imágenes → 8 exámenes únicos / 40 reactivos).
- [x] PDFs de libros analizados (Probabilidad y Estadística, 388 pp.).

**Diseño Visual Planeado (aplicado):**
- Bayes / Prob. Total -> Diagrama de flujo de ramas + tabla.
- Binomial -> Gráfica de barras (matplotlib) + tabla.
- Normal -> Tabla "Qué usar según lo que piden".
- Exponencial -> Tabla "Quiero → uso".
- V.A. Continua / Discreta -> Tablas de fórmulas.
- Otros temas (Condicional, Geométrica, Poisson, Hipergeom., Combinatoria) -> Tablas visuales + formulario.

**Estado del Entregable:**
- [x] Guía generada aplicando la Metodología de Colores (Azul, Rojo, Verde, Naranja).
- [x] Archivo `Guia_Visual_Probabilidad.html` guardado en `...\Guias terminadas\`
- [x] Nota: se eligió HTML+CSS (imprimible a PDF) porque `python-docx` no pudo usarse (Windows bloqueó la DLL de lxml por política de App Control).

**Entregable 2 — Exámenes Interactivos (23-Ago-2026):**
- [x] Archivo `Examenes_Interactivos_Probabilidad.html` guardado en `...\Guias terminadas\` (53 KB).
- [x] 8 exámenes reales separados por sección con menú de navegación (anclas exam1–exam8).
- [x] 34 preguntas en formato opción múltiple (A–D, botones de radio interactivos).
- [x] Cada pregunta tiene botón "🔍 Ver Solución" con explicación detallada paso a paso.
- [x] Cada solución indica "✅ Respuesta correcta: A)" y aplica los 4 colores: 🔵 Concepto, 🟠 Fórmula, 🟢 Desarrollo/Respuesta, ⚠️ Trampa.
- [x] Incluye: Árbol de Decisión, Tabla de Notación, Fórmulas Maestras, Repaso Activo.
- [x] Validación automática aprobada (`verify_final.py`): 34 preguntas × 4 opciones = 136 radios OK; sin opciones duplicadas; valores de la respuesta correcta verificados numéricamente contra cada solución; divs balanceados (297/297); JS `toggleSolution` funcional.
- [x] Generador reproducible: `gen_examenes_interactivos.py` en el directorio raíz.

---

# Materia Actual: **Entrevista Técnica** (Estudio de examen)

**Directorio de ingesta:** `...\Matería\Trabajo\` → `Guia_Entrevista_Tecnica_Christian_Garcia.pdf` (36.7 KB, 5 págs., texto extraído en `_extract_trabajo.txt`, 8.1 KB). Sin imágenes ni libros; se complementó con investigación web (Google Cloud, Advisera ISO 27001, Check Point EDR, Okta RBAC/ABAC, IBM RAG, DigitalOcean subnetting, SQLNoir JOINs).

**Contexto del candidato:** Christian Aldair García Ochoa — Soporte TI · Infraestructura · Ciberseguridad · Automatización. Métricas: 278 tickets · 98.6% efectividad · 66 tickets IAM · 15 manuales IA · 80% avance política accesos · Full-Stack.

**Entregable generado (23-Sep-2026):**
- [x] `Guia_Visual_Entrevista_Tecnica.html` en `...\Guias terminadas\` (62.7 KB / 87 bloques div).
- [x] Estilo visual estricto: fondo `#0F172A`, bloques 3 capas (azul/rojo/verde/naranja/mapa/recall), imprimible a PDF, sin links externos.
- [x] Contenido completo del PDF (21 secciones): perfil + métricas defensables, árbol de decisión de diagnóstico, tabla de notación (40+ siglas), Soporte TI, Redes, Ciberseguridad, IAM, GCP/Workspace, M365, Hardware, SQL, Python/C++/automatización, Full-Stack, Git/Docker, IA/agentes, ISO 27001, Jira/Monday.
- [x] **40 preguntas de entrevista** del PDF con respuestas modelo (Soporte 5, Redes 9, Seguridad 10, Cloud/GCP 6, SQL 6, Desarrollo 8, IA 6).
- [x] Tabla de prioridad Pareto (12 áreas ordenadas por profundidad), guion de 60-90 seg (PAR-hT), plantilla de incidente, repaso activo (5 preguntas), regla de honestidad ISO 27001.
- [x] Validado (`_verify_entrevista.py`): 87/87 div, 23/23 tablas, 28/28 ul, 174/174 tr, 423/423 td balanceados; termina en `</html>`; 41 anclas sin rotas; sin caracteres residuales de extracción PDF.
- [x] Generador reproducible: `gen_visual_entrevista.py` en el directorio raíz.

# Materia Actual: **SQL** (Estudio de examen)

**Directorio de ingesta:** `...\Materia\SQL\` → solo `Examen_SQL.md` (sin imágenes ni libros).

**Proyecto:** Sistema de Gestión Hospitalaria en SQL Server (DDL + DML + DCL + Triggers + Procedures + Vistas + 7 fases + 60 preguntas).

**Entregables generados (26‑Ago‑2026):**
- [x] `Examen_SQL_Resuelto.md` en `...\Guias terminadas\` (50.8 KB / 858 líneas).
- [x] Resuelve el **desarrollo implementado**: SQL Server (Transact‑SQL puro, sin MySQL): CREATE TABLE (7 tablas, PK/FK, IDENTITY, CHECK, ON DELETE/UPDATE), ALTER/DROP/sp_rename, DML (INSERT/UPDATE/DELETE/SELECT + WHERE), funciones/variables (@var, AVG/COUNT/SUM/MAX/MIN), DCL (Login vs User, GRANT/REVOKE, WITH GRANT OPTION, CASCADE), 3 triggers (AFTER INSERT/UPDATE/DELETE con inserted/deleted), 4 procedures (CRUD + EXEC + parámetros), 2 vistas (INNER JOIN ≥3 tablas), 7 fases de diseño.
- [x] **60 preguntas resueltas** (1–45 teóricas, 46–55 análisis, 56–60 desarrollo) + asociación final + simulacro de 10 respuestas.
- [x] `Guia_Visual_SQL.html` en `...\Guias terminadas\` (16.9 KB), fondo oscuro `#0F172A`, paleta de 3 capas (azul/rojo/verde/naranja), árbol de decisión, tabla de notación, tabla de prioridades, índice, y simulacro. Imprimible a PDF. Validado: 30/30 `<div>` balanceados, termina en `</html>`.
- [x] Generador reproducible: `gen_visual_sql.py` en el directorio raíz.
- [x] Base de conocimientos: Microsoft Learn (create‑table, alter‑table, insert, select, grant, revoke, create‑trigger, create‑procedure, create‑view, create‑login, inner‑join).

---

# Materia Actual: **Salesforce FSC & Slack** (Estudio de examen)

**Directorio de ingesta:** `...\Matería\Sales Force\` → `1er_MCB (1).pdf` (95 págs., programa de capacitación presencial de 40 h, 10 sesiones / 4 bloques). Sin imágenes de exámenes ni libros.

**Ingesta (02-Sep-2026):**
- [x] PDF analizado (95 páginas → texto extraído en `_extract_salesforce.txt`, 75 KB).
- [x] Estructura mapeada: B1 Fundamentos (S1), B2 FSC+Insurance (S2–S5), B3 Service+Voice (S6–S9), B4 Slack (S10).
- [x] Tabla de frecuencias con términos clave (SLA 100, Asegurado 95, Slack 84, Siniestro 81, Case 73…).

**Entregable — Examen Interactivo (02-Sep-2026):**
- [x] `Examenes_Interactivos_Salesforce.html` en `...\Guias terminadas\` (~92 KB).
- [x] **60 reactivos** de nivel difícil (opción múltiple A–D) con escenarios reales y relación de conceptos, **balanceados 15×A, 15×B, 15×C, 15×D** (rotación automática por nº de reactivo).
- [x] Cobertura total del temario: S1=5, S2=8, S3=8, S4=6, S5=7, S6=7, S7=5, S8=5, S9=4, S10=5.
- [x] Barra inferior con contador y barra de progreso; el botón **"✓ Mostrar resultados" aparece solo al responder los 60**.
- [x] Al calificar: panel con aciertos/60, %, mensaje y listado de reactivos incorrectos; en cada error se resalta la opción correcta (verde) y la elegida (rojo) y se abre la **justificación con código de colores** 🔵 concepto · 🟠 regla de oro · 🟢 ejemplo/solución · ⚠️ trampa.
- [x] Incluye: Árbol de Decisión (qué herramienta usar), Tabla de Notación de objetos, Reglas de Oro, Trampas Comunes y Repaso Activo.
- [x] Estilo visual estricto: fondo `#0F172A`, bloques con 3 capas (background/border/texto), imprimible a PDF.
- [x] Validado (`verify_salesforce.py`): 60 preguntas × 4 opciones = 240 radios OK; 60 soluciones; 383/383 `<div>` balanceados; sin opciones duplicadas; ANS ↔ "Respuesta correcta" 60/60; cierra en `</html>`.
- [x] Generador reproducible: `gen_examenes_salesforce.py` en el directorio raíz.

---

# Evolución v2 — Guía + Examen combinados (26-Sep-2026)

**Decisión del usuario:** No migrar a app/plataforma por ahora. Solo mejorar el agente generador: (1) estándar/base de diseño compartida + validación obligatoria antes de entregar; (2) guía visual mejorada; (3) UN SOLO HTML por materia con alternador 📖 Guía ⇄ 📝 Examen; (4) examen que corrige cada pregunta al momento, guarda en `localStorage`, restaura al reabrir y da resultado global + por tema al finalizar.

**Archivos base creados en el directorio raíz:**
- [x] `estilo_base.py` — CSS único compartido (fondo `#0F172A`, bloques 3 capas 🔵🔴🟢🟠🗺️🧠, alternador, examen v2, barra, panel resultados, `@media print`) + helpers `H2/B/TAB/LI/PRE/RECALL/HERO`.
- [x] `examen_v2.js` — Motor examen v2 (guardado `localStorage` clave `ex_<id>_respuestas`, restauración, feedback por pregunta verde/rojo + justificación inmediata, barra fija, resultado global + dominio por tema + "Temas a repasar" con anclas a la guía, reintentar con confirmación).
- [x] `gen_guia_examen_v2.py` — Generador combinado (contenido Entrevista Técnica, JSON embebido, JS inyectado con ID de materia).
- [x] `verify_v2.py` — Validador obligatorio FASE 4 (balance HTML, vistas guía/examen, alternador, IDs únicos, anclas, radios 4x, feedback, motor JS, JSON parsea, temas existen en guía).

**Entregable piloto (26-Sep-2026, ampliado 01-Oct-2026):** cobertura total del PDF — 12 temas + 38 preguntas (≥2 por tema), validación APROBADO ✔.
- [x] `Guias terminadas/Guia_Examen_Entrevista_Tecnica.html`: 12 temas navegables (soporte, redes, ciberseguridad, IAM, SQL, IA, python-auto, fullstack, iso-gestion, workspace-gcp, m365, hardware) + 38 preguntas examen v2 con guardado y resultado por tema.
- [x] Validación `verify_v2.py`: **APROBADO ✔** (div 184/184, table 9/9, details 17/17, 152 radios = 38×4, feedback 38/38, JSON 38 preguntas, 0 anclas rotas, cierra en `</html>`).

**Reglas del agente actualizadas:**
- [x] `Inicio/agent.md` — Formato v2 (un solo HTML, alternador, guía navegable, examen v2 con guardado/feedback/por-tema), validación obligatoria FASE 4, comandos `/generar_guia_visual` y `/generar_examen` actualizados.
- [x] `Inicio/flujo_trabajo.md` — FASE 2 clasifica Tipo A/B/C; FASE 3 usa base compartida + estructura v2; FASE 4 validación obligatoria con `verify_v2.py`.

# Publicación en GitHub (01-Oct-2026)

**Repo:** `https://github.com/DedSecRisk/Agente_de_estudio_y_examenes.git` (rama `main`, commit `f90554b`, 29 archivos, ~258 KB subidos).
- [x] `git init` + `.gitignore` (excluye `Matería/`, `_extract_*.txt`, `*.pdf/jpg/jpeg/png`, `__pycache__/`) + `README.md` con estructura y uso.
- [x] Commit inicial + `push -u origin main` exitoso.
- [x] **NO versionado (por copyright/privacidad):** libro Probabilidad (30 MB), PDF capacitación Salesforce, PDFs/imágenes de exámenes, guía con datos personales del CV, extracts de texto.

# Reorganización del repo (05-Oct-2026)

- [x] Nueva estructura: `Inicio/` (punto de entrada) · `src/` (código) · `docs/` (especificación + roadmap) · `Guias terminadas/` (entregables) · `Matería/` (fuente local, no versionada).
- [x] `Inicio/LEEME.md` (mapa + protocolo de inicio, orden de lectura 0→6) y `Inicio/estado_actual.md` (resumen vivo: dónde estamos, último entregable, qué sigue).
- [x] Rutas actualizadas a `src/` en `Inicio/agent.md`, `Inicio/flujo_trabajo.md` y `README.md`; comandos verificados (`python src/gen_guia_examen_v2.py` + `python src/verify_v2.py` → APROBADO ✔).
- [x] Nota: `verify_v2.py` requiere consola UTF-8 (`$env:PYTHONUTF8='1'` en PowerShell) por los emojis ✅/✔.

