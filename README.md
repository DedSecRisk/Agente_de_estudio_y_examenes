# Agente de Estudio y Exámenes — ParetoTutor Visual

Generador local de **guías de estudio visuales + exámenes interactivos** en un solo HTML
autocontenido (offline, imprimible a PDF). Sin frameworks, sin backend: Python + HTML/CSS/JS vanilla.

## Estructura

| Ruta | Qué es |
|---|---|
| `Inicio/` | Reglas del agente (`agent.md`, `flujo_trabajo.md`, `plantilla_salida.md`, `reglas_estilo_visual.md`, `memoria_sesion.md`) |
| `estilo_base.py` | CSS único compartido + helpers HTML (base visual v2) |
| `examen_v2.js` | Motor de examen: corrección inmediata, `localStorage`, resultado global + por tema |
| `gen_guia_examen_v2.py` | Generador combinado Guía + Examen (sistema v2 actual) |
| `verify_v2.py` | Validador obligatorio FASE 4 (se ejecuta antes de cada entrega) |
| `gen_visual*.py`, `gen_examenes_*.py` | Generadores legacy (Probabilidad, SQL, Salesforce) |
| `verify_final.py`, `verify_salesforce.py` | Validadores legacy |
| `Guias terminadas/` | Entregables HTML/Markdown listos para abrir en el navegador |
| `Especificacion_Agente_Guias_Examenes.md` | Especificación del sistema guía + examen |
| `Plan_Plataforma_Estudio_TI.md` | Roadmap futuro (plataforma/app) |

> **Nota:** la carpeta `Matería/` (PDFs, libros e imágenes fuente) y los `_extract_*.txt`
> **no se versionan** (ver `.gitignore`): contienen material con copyright y datos
> personales. Cada usuario coloca allí su propio material de estudio en local.

## Uso

```bash
# Generar la guía + examen (sistema v2)
python gen_guia_examen_v2.py

# Validar antes de entregar (obligatorio)
python verify_v2.py
```

Abrir `Guias terminadas/Guia_Examen_Entrevista_Tecnica.html` en el navegador:
alternar 📖 Guía ⇄ 📝 Examen, responder (corrección inmediata), el progreso se guarda
solo y al finalizar se muestra el dominio por tema con enlaces de repaso.
