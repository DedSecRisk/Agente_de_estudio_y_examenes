# -*- coding: utf-8 -*-
"""
estilo_base.py — Base visual única de ParetoTutor Visual (v2)
CSS compartido para TODAS las guías/exámenes generados.
Cumple reglas_estilo_visual.md: fondo #0F172A, bloques 3 capas, paleta 🔵🔴🟢🟠🗺️🧠.
Incluye estilos del modo combinado GUÍA ⇄ EXAMEN (un solo archivo HTML).
"""

CSS = r"""
/* ===== ParetoTutor Visual v2 — estilos base compartidos ===== */
:root{--azul:#38bdf8;--rojo:#ef4444;--verde:#22c55e;--naranja:#f59e0b;--morado:#6366f1;--base:#0F172A}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--base);color:#e2e8f0;font-family:'Segoe UI',Calibri,Arial,sans-serif;margin:0;padding:20px;line-height:1.5}
.wrap{max-width:1060px;margin:0 auto}

/* ---------- Encabezado ---------- */
h1{font-size:1.85em;color:#f8fafc;letter-spacing:.3px;text-align:center;margin:6px 0}
.sub{text-align:center;color:#94a3b8;font-size:.95em}
h2{font-size:1.3em;color:#f1f5f9;border-bottom:2px solid #475569;padding-bottom:4px;margin:24px 0 10px}
h3{font-size:1.1em;color:#e2e8f0;margin:2px 0 6px}
.hero{background:linear-gradient(135deg,#0C4A6E,#0284C7);color:#fff;border-radius:14px;padding:18px 20px;box-shadow:0 2px 12px rgba(0,0,0,.5)}
.hero h1{margin:0;color:#fff}
.hero p{margin:6px 0 0;font-size:1.02em;opacity:.93}

/* ---------- Alternador GUÍA ⇄ EXAMEN ---------- */
.modo{position:sticky;top:0;z-index:60;background:rgba(15,23,42,.96);border:1px solid #334155;border-radius:10px;padding:8px 12px;margin:10px 0;text-align:center}
.modo button{background:transparent;border:2px solid var(--morado);color:#a5b4fc;font-weight:700;font-size:.98em;padding:7px 18px;border-radius:8px;cursor:pointer;margin:0 6px;font-family:inherit}
.modo button.activo{background:var(--morado);color:#e0e0ff;border-color:#818cf8}
#vista-guia,#vista-examen{display:none}

/* ---------- Tabla de contenido / ruta rápida ---------- */
.toc{background:#1e293b;border:2px solid #475569;border-radius:10px;padding:12px 16px;column-count:2;column-gap:26px}
.toc a{color:#7dd3fc;text-decoration:none;display:block;padding:2px 0}
.toc a:hover{text-decoration:underline}
.toc .n{display:inline-block;background:var(--azul);color:#0f1729;border-radius:4px;padding:0 7px;font-size:.75em;font-weight:700;margin-right:5px}

/* ---------- Bloques visuales (3 capas) ---------- */
.bloque{border-radius:10px;margin:9px 0;padding:12px 14px}
.bloque h3{margin:2px 0 6px}
.bloque b{color:inherit}
.bloque code{background:rgba(15,23,42,.55);color:#e2e8f0;border:1px solid #475569;border-radius:4px;padding:0 5px;font-family:Consolas,monospace;font-size:.9em}
.b-azul{background:rgba(56,189,248,.10);border:2px solid #38bdf8;color:#bae6fd}
.b-rojo{background:rgba(248,113,113,.10);border:2px solid #ef4444;color:#fecaca}
.b-verde{background:rgba(34,197,94,.10);border:2px solid #22c55e;color:#bbf7d0}
.b-naranja{background:rgba(245,158,11,.10);border:2px solid #f59e0b;color:#fef3c7}
.b-mapa{background:#1e293b;border:2px dashed #475569;color:#cbd5e1}
.b-recall{background:#0f1729;border:2px solid #6366f1;color:#e0e0ff}

/* ---------- Tablas y código ---------- */
table{border-collapse:collapse;width:100%;font-size:.92em;margin:6px 0}
th,td{border:1px solid #475569;padding:6px 8px;text-align:left}
th{background:#1e293b;color:#cbd5e1}
.cmd{display:block;background:#0d1b2e;border:1px solid #475569;color:#7dd3fc;padding:4px 10px;border-radius:6px;font-family:Consolas,monospace;font-size:.88em;margin:2px 0;white-space:pre-wrap}
blockquote{background:#0f1729;border-left:4px solid var(--naranja);color:#fef3c7;padding:6px 12px;margin:6px 0}
.badge{display:inline-block;background:#1e293b;color:#94a3b8;border:1px solid #475569;border-radius:6px;padding:1px 8px;font-size:.78em;margin:0 3px}
.prio-alta{background:rgba(239,68,68,.15);border:1px solid #ef4444;color:#fecaca}
.prio-media{background:rgba(245,158,11,.15);border:1px solid #f59e0b;color:#fef3c7}
.prio-baja{background:rgba(56,189,248,.12);border:1px solid #38bdf8;color:#bae6fd}

/* ---------- Preguntas de repaso activo ---------- */
details{background:#0f1729;border:1px solid #6366f1;border-radius:8px;margin:5px 0;padding:6px}
summary{color:#a5b4fc;font-weight:bold;cursor:pointer}
/* ===== Estilos del EXAMEN v2 (feedback por pregunta + guardado) ===== */
.ex-intro{background:#0f1729;border:2px solid #38bdf8;border-radius:10px;padding:12px 14px;color:#bae6fd;margin-bottom:12px}
.ex-stats{display:inline-block;background:rgba(99,102,241,.15);color:#a5b4fc;border:1px solid #6366f1;border-radius:6px;padding:2px 10px;font-size:.85em}
.pregunta{background:rgba(255,255,255,.045);border:1px solid #334155;border-left:4px solid #38bdf8;padding:14px 16px;margin-bottom:18px;border-radius:8px}
.pregunta.respondida{border-left-color:#22c55e}
.pregunta.ok{border-color:#22c55e;border-left-color:#22c55e}
.pregunta.bad{border-color:#ef4444;border-left-color:#ef4444}
.pnum{display:inline-block;background:#38bdf8;color:#0f1729;font-weight:700;border-radius:4px;padding:1px 9px;margin-right:8px}
.ptema{display:inline-block;background:rgba(245,158,11,.15);color:#fef3c7;border:1px solid #f59e0b;border-radius:4px;padding:1px 8px;font-size:.75em}
.opciones{display:flex;flex-direction:column;gap:8px;margin:10px 0 12px}
.opcion{display:flex;align-items:flex-start;gap:10px;background:rgba(56,189,248,.07);border:2px solid #38bdf8;color:#bae6fd;padding:9px 12px;border-radius:6px;cursor:pointer;transition:.15s}
.opcion:hover{background:rgba(56,189,248,.18);border-color:#7dd3fc}
.opcion input{margin-top:3px;flex:none}
.opcion.bloqueada{pointer-events:none;opacity:.72}
.opcion.correcta{background:rgba(34,197,94,.16);border-color:#22c55e;color:#bbf7d0}
.opcion.incorrecta{background:rgba(248,113,113,.16);border-color:#ef4444;color:#fecaca}
.ex-feedback{display:none;margin-top:10px;padding:12px;background:rgba(30,41,59,.6);border:2px dashed #475569;border-radius:8px}
.ex-feedback .caja-verde{background:rgba(34,197,94,.10);border:2px solid #22c55e;color:#bbf7d0;padding:8px 12px;border-radius:6px;margin:6px 0;font-size:.95em}
.ex-feedback .caja-azul{background:rgba(56,189,248,.10);border:2px solid #38bdf8;color:#bae6fd;padding:8px 12px;border-radius:6px;margin:6px 0;font-size:.95em}
.ex-feedback .caja-naranja{background:rgba(245,158,11,.10);border:2px solid #f59e0b;color:#fef3c7;padding:8px 12px;border-radius:6px;margin:6px 0;font-size:.95em}
.ex-feedback .caja-roja{background:rgba(248,113,113,.10);border:2px solid #ef4444;color:#fecaca;padding:8px 12px;border-radius:6px;margin:6px 0;font-size:.95em}

/* Barra de progreso flotante */
.ex-bar{position:sticky;bottom:0;z-index:55;background:rgba(15,23,42,.97);border:1px solid #334155;border-radius:10px;padding:8px 12px;margin:6px 0;display:flex;gap:12px;align-items:center;justify-content:center}
.ex-bar span{color:#4ade80;font-weight:700;font-size:.95em}
.bar-wrap{width:260px;height:14px;background:#1e293b;border:1px solid #475569;border-radius:7px;overflow:hidden}
.bar-fill{height:100%;background:linear-gradient(90deg,#6366f1,#38bdf8,#22c55e);width:0%;transition:width .25s}
.ex-bar button.ver-resultados{background:#22c55e;color:#0f1729;border:none;padding:6px 16px;border-radius:8px;cursor:pointer;font-weight:700;display:none}

/* Panel de resultados */
.res-panel{display:none;background:#0f1729;border:2px solid #6366f1;border-radius:12px;padding:16px 18px;margin-top:16px}
.res-panel h3{color:#a5b4fc;font-size:1.2em;margin:0 0 6px}
.res-global{font-size:2.6em;font-weight:800;color:#a5b4fc;text-align:center}
.res-detalle{font-size:1.15em;color:#e2e8f0;text-align:center}
.res-msg{background:rgba(34,197,94,.10);border:1px solid #22c55e;color:#bbf7d0;padding:8px 12px;border-radius:8px;text-align:center;margin:8px 0;font-weight:700}
.res-tema{display:flex;justify-content:space-between;align-items:center;margin:6px 0}
.res-tema .rt-nombre{color:#cbd5e1;min-width:180px}
.res-tema .rt-bar{height:12px;background:#1e293b;border:1px solid #475569;border-radius:6px;overflow:hidden;flex:1}
.res-tema .rt-fill{height:100%;background:#22c55e;width:0%}
.res-tema .rt-pct{color:#e2e8f0;min-width:52px;font-weight:700}
.res-repasar{background:rgba(248,113,113,.10);border:2px solid #ef4444;color:#fecaca;padding:8px 12px;border-radius:8px;margin:8px 0}
.res-repasar a{color:#fecaca;text-decoration:underline;cursor:pointer}
.res-botones{text-align:center;margin-top:10px}
.res-botones button{background:#6366f1;color:#e0e0ff;border:none;padding:9px 18px;border-radius:8px;cursor:pointer;font-weight:700;margin:4px 6px}
.res-botones button.reintentar{background:#ef4444;color:#fff}

/* Pie y reglas de impresión */
.foot{text-align:center;color:#64748b;font-size:.8em;margin-top:18px}
@media print{
  body{zoom:.9}
  #vista-guia,#vista-examen{display:block}
  .modo,.ex-bar{display:none}
  .opcion{box-shadow:inset 0 0 0 1000px #fff;color:#000}
}
"""
# ---FIN-CSS---
# ================= Helpers HTML reutilizables =================

def H2(uid, icono, titulo):
    """Encabezado de sección con ID para anclas."""
    return f'<h2 id="{uid}">{icono} {titulo}</h2>'

def B(estilo, emoji, titulo, cuerpo):
    """Bloque visual de 3 capas: estilo en {azul,rojo,verde,naranja,mapa,recall}."""
    return (f'<div class="bloque b-{estilo}"><h3>{emoji} {titulo}</h3>{cuerpo}</div>')

def TAB(cab, filas, cls=""):
    """Tabla HTML a partir de encabezados y filas."""
    ths = "".join(f"<th>{c}</th>" for c in cab)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas)
    return f'<table class="{cls}"><tr>{ths}</tr>{trs}</table>'

def LI(items):
    """Lista con viñetas."""
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def PRE(txt):
    """Bloque de código/consola."""
    return f'<div class="cmd">{txt}</div>'

def RECALL(pares):
    """Repaso activo: lista de preguntas/respuestas en details."""
    out = ['<div class="bloque b-recall"><h3>🧠 Repasa antes de continuar</h3>']
    for i, (p, r) in enumerate(pares, 1):
        out.append(f'<details><summary>Q{i}. {p}</summary><p>{r}</p></details>')
    out.append('</div>')
    return "".join(out)

def HERO(titulo, subtitulo):
    """Encabezado hero del documento."""
    return f'<div class="hero"><h1>{titulo}</h1><p>{subtitulo}</p></div>'