# 📌 Estado actual del proyecto (resumen vivo)

> **Actualizar al cerrar cada sesión de trabajo.** `memoria_sesion.md` guarda el detalle;
> aquí solo el estado necesario para retomar sin leer todo.

## Dónde estamos (05-Oct-2026)

- **Repo:** `https://github.com/DedSecRisk/Agente_de_estudio_y_examenes.git` · rama `main` · limpio y sincronizado.
- **Estructura vigente:** `Inicio/` (reglas+estado) · `src/` (código) · `docs/` (especificación+roadmap) · `Guias terminadas/` (entregables) · `Matería/` (fuente local, no versionada).
- **Sistema vigente:** **v2** — un solo HTML por materia (📖 Guía ⇄ 📝 Examen), base `src/estilo_base.py` + motor `src/examen_v2.js`, validación obligatoria `src/verify_v2.py` (FASE 4).

## Último entregable validado

- `Guias terminadas/Guia_Examen_Entrevista_Tecnica.html` — **12 temas + 38 preguntas**, `verify_v2.py` = **APROBADO ✔** (div 184/184, 152 radios, feedback 38/38, 0 anclas rotas).
- Generador: `src/gen_guia_examen_v2.py`. Uso: `python src/gen_guia_examen_v2.py` → `python src/verify_v2.py`.

## Qué sigue (Fase 5 — migración v2)

1. **SQL** → 2. **Probabilidad** → 3. **Salesforce** (se conservan los legacy hasta revalidar).
- Pendiente del usuario en GitHub web: campo **About** (descripción + topics, sin website).

## Notas operativas

- Comandos se ejecutan desde la raíz del repo; los scripts viven en `src/`.
- `Matería/`, `_extract_*.txt`, `*.pdf/jpg/jpeg/png`, `__pycache__/` **no se versionan** (`.gitignore`).
- Historial completo y decisiones en `memoria_sesion.md`.
