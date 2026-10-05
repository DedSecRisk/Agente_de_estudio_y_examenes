# 🧭 INICIO — Punto de entrada de cada sesión

> **Lee estos archivos en orden al comenzar.** Todo lo necesario para ponerte al día
> está aquí; si falta algo, actualiza esta carpeta antes de trabajar.

| # | Archivo | Qué contiene |
|---|---|---|
| 0 | `LEEME.md` (este archivo) | Mapa de la carpeta + protocolo de inicio de sesión. |
| 1 | `agent.md` | Rol **ParetoTutor Visual**, formato v2, rutas, comandos. |
| 2 | `flujo_trabajo.md` | Fases 1–4 (ingesta → Pareto/Tipo A-B-C → producción → **validación obligatoria**). |
| 3 | `reglas_estilo_visual.md` | Paleta 3 capas (`#0F172A` + 🔵🔴🟢🟠🗺️🧠) y cierres obligatorios por tema. |
| 4 | `plantilla_salida.md` | Plantilla por tema de prioridad alta + simulacro final. |
| 5 | `estado_actual.md` | **Resumen vivo**: dónde estamos, último entregable, qué sigue. |
| 6 | `memoria_sesion.md` | Historial detallado (decisiones, materias, validaciones, publicación). |

## 🗂️ Mapa del proyecto (rutas relativas al repo)

```text
Estudio de examen/
├── Inicio/                  ← ESTÁS AQUÍ (reglas + estado + memoria)
├── src/                     ← código: base visual, motor examen, generadores, validadores
├── docs/                    ← especificación del sistema + roadmap/plataforma
├── Guias terminadas/        ← entregables HTML/Markdown listos
├── Matería/                 ← material fuente LOCAL (no versionado)
├── README.md                ← presentación pública del repo
└── .gitignore
```

## ✅ Protocolo de inicio de sesión (para el agente)

1. Lee `Inicio/` en el orden de la tabla (0→6).
2. Verifica `estado_actual.md`: confirma último entregable y pendiente.
3. Ejecuta `git status --short` y `git log --oneline -3` para situarte.
4. Si `Guias terminadas/` cambió sin registro, actualiza `estado_actual.md`
   y `memoria_sesion.md` **antes** de generar nada nuevo.
5. Recién entonces recibe la instrucción del usuario.
