# Flujo de Trabajo Local para Sesiones Visuales

## FASE 1: Ingesta y Análisis (Comando `/analizar [Nombre de la Materia]`)
1. Construye la ruta de búsqueda: `C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Materia\[Nombre de la Materia]\`
2. Escanea `\imagenes de examenes\` y `\libros\`.
3. Extrae temas y evalúa visualmente qué tipo de gráficos/diagramas ayudarán a explicar mejor cada tema.
4. Responde con tabla de frecuencias.

## FASE 2: Consolidación (Comando `/estado`)
1. Calcula el "Top 20% de temas clave".
2. Clasifica la materia: **Tipo A (cuantitativa)**, **Tipo B (herramienta/tecnológica)** o **Tipo C (conceptual/puesto)** para elegir la plantilla adecuada.

## FASE 3: Producción Visual y Guardado (Comando `/generar_guia_visual [Nombre de la Materia]`)
1. Selecciona los temas de Prioridad Alta.
2. Utiliza Python para generar un **HTML autocontenido** con estilos CSS (colores de fondo, bordes, tipografía). El CSS base compartido está en `src/estilo_base.py`; el motor de exámenes v2 en `src/examen_v2.js` y `src/gen_guia_examen_v2.py`.
3. **Estructura Visual:** Aplica estrictamente la paleta de colores (Azul, Rojo, Verde, Naranja) con la regla de 3 capas de `reglas_estilo_visual.md`.
4. **Guía + Examen combinados (formato v2):** El entregable es UN SOLO archivo HTML con:
   - Alternador superior **📖 Guía ⇄ 📝 Examen** (botones que muestran/ocultan cada vista).
   - Guía dividida en temas navegables: `<h2 id="tema-slug">` + índice "Ruta rápida" con anclas internas.
   - Examen interactivo que **corrige cada pregunta al momento**, guarda el progreso en `localStorage` (clave `ex_<materia>_respuestas`), restaura al reabrir, muestra barra de progreso fija y al final da resultado global + **dominio por tema** + **"Temas a repasar"** con enlaces que regresan a la sección de la guía.
5. **ACCIÓN CRÍTICA DE GUARDADO:** Guarda el archivo EXACTAMENTE en: `C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\`

## FASE 4: Validación OBLIGATORIA antes de confirmar (NUEVA — no omitir)
1. Ejecuta `python src/verify_v2.py <archivo_generado>` (o el verificador de la materia).
2. Corrige TODO fallo hasta `RESULTADO: APROBADO`.
3. Solo entonces confirma al usuario que el documento está listo en su carpeta.
