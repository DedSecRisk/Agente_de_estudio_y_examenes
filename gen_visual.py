# -*- coding: utf-8 -*-
"""Genera Guia_Visual_Probabilidad.html en modo OSCURO.
(fondo oscuro #0F172A con paleta de 3 capas por bloque, colores semánticos
azul/rojo/verde/naranja + arbol de decision, notacion, repaso activo)."""
import base64, io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import comb, sqrt

Salida_dir = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas"
HTML_OUT = Salida_dir + r"\Guia_Visual_Probabilidad.html"

def fig_to_b64(fig):
    buf = io.BytesIO(); fig.savefig(buf, format="png", dpi=130, bbox_inches="tight")
    plt.close(fig); return base64.b64encode(buf.getvalue()).decode("ascii")

def diagrama_bayes():
    fig, ax = plt.subplots(figsize=(8, 4.4))
    fig.patch.set_facecolor("#0F172A")
    ax.set_facecolor("#1e293b")
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    for cy, c in zip([7.5, 5, 2.5], ["B1 (rama 1)", "B2 (rama 2)", "B3 (rama 3)"]):
        ax.text(1.4, cy, c, fontsize=10, ha="center", va="center", color="#bae6fd",
                bbox=dict(boxstyle="round,pad=0.4", fc="#0f1729", ec="#38bdf8"))
    ax.text(8.4, 5, "A (resultado)\nP(A)=p1+p2+p3", fontsize=10, ha="center", va="center", color="#bbf7d0",
            bbox=dict(boxstyle="round,pad=0.5", fc="#0f1f10", ec="#22c55e"))
    for cy in [7.5, 5, 2.5]:
        ax.annotate("", xy=(7.9, 5), xytext=(2.6, cy), arrowprops=dict(arrowstyle="->", lw=1.6, color="#94a3b8"))
    ax.text(5, 9.4, "BAYES:  P(Bk|A) = P(Bk)*P(A|Bk) / P(A)", fontsize=11, ha="center", color="#0f1729",
            bbox=dict(fc="#fef3c7", ec="#f59e0b", boxstyle="round,pad=0.4"))
    return fig_to_b64(fig)

def diagrama_binomial():
    fig, ax = plt.subplots(figsize=(8, 4.2))
    fig.patch.set_facecolor("#0F172A")
    ax.set_facecolor("#1e293b")
    ax.tick_params(colors="#cbd5e1")
    n, p = 15, 0.3
    k = list(range(0, n+1))
    probs = [comb(n, r)*(p**r)*((1-p)**(n-r)) for r in k]
    ax.bar(k, probs, color="#38bdf8", edgecolor="#0284C7")
    mu = n*p; sd = sqrt(n*p*(1-p))
    ax.axvline(mu, color="#EF4444", ls="--", lw=2)
    ax.text(mu+0.3, max(probs)*0.9, f"media={mu:.1f}", color="#fecaca")
    ax.text(mu+0.3, max(probs)*0.7, f"sigma={sd:.2f}", color="#fecaca")
    ax.set_title("Distribucion Binomial (ejemplo visual)", color="#f8faf4")
    ax.set_xlabel("Num. de exitos", color="#f8faf4"); ax.set_ylabel("P(X=r)", color="#f8faf4"); ax.grid(True, alpha=0.25, color="#475569")
    return fig_to_b64(fig)

IMG = {"bayes": diagrama_bayes(), "binomial": diagrama_binomial()}
print("Diagramas OK")

# ---------- CSS según reglas_estilo_visual.md ----------
CSS = """
body{font-family:'Segoe UI',Arial,sans-serif;max-width:920px;margin:20px auto;padding:0 16px;
     color:#E2E8F0;line-height:1.55;background:#0F172A;}
header{background:linear-gradient(135deg,#0C4A6E,#0284C7);color:#fff;border-radius:14px;
     padding:22px;margin-bottom:12px;box-shadow:0 2px 10px rgba(0,0,0,.45);}
header h1{margin:0;font-size:1.9em;} header p{margin:6px 0 0;font-size:1.05em;opacity:.92;}
h2.tema{background:#0284C7;color:#fff;padding:10px 14px;border-radius:8px;margin:30px 0 6px;
     font-size:1.3em;}
h2.seccion{color:#60A5FA;margin-top:24px;border-bottom:3px solid #0284C7;padding-bottom:4px;}
/* Paleta de 3 capas (regla 1) — Tema OSCURO: fondo oscuro + texto claro, colores semánticos */
.bloque{border-radius:10px;padding:12px 16px;margin:10px 0;}
.azul{background:rgba(56,189,248,.10);border:2px solid #38bdf8;color:#bae6fd;}
.rojo{background:rgba(248,113,113,.10);border:2px solid #ef4444;color:#fecaca;}
.verde{background:rgba(34,197,94,.10);border:2px solid #22c55e;color:#bbf7d0;}
.naranja{background:rgba(245,158,11,.10);border:2px solid #f59e0b;color:#fef3c7;}
.mapa{background:#1e293b;border:2px dashed #475569;color:#cbd5e1;}
.recall{background:#0f1729;border:2px solid #6366f1;color:#e0e0ff;border-radius:10px;
     padding:12px 16px;margin:10px 0;}
h4{color:#f8faf4;padding:4px 12px;border-radius:6px;display:inline-block;font-size:1em;margin:0 0 8px;}
.azul h4{background:#0284C7;} .rojo h4{background:#ef4444;} .verde h4{background:#22c55e;}
.naranja h4{background:#f59e0b;} .mapa h4{background:#475569;} .recall h4{background:#6366f1;}
.bloque a, .bloque b, .bloque li{color:inherit;}
table.flujo{border-collapse:collapse;width:100%;margin:6px 0;color:#cbd5e1;}
table.flujo td,table.flujo th{border:1px solid #475569;padding:8px;text-align:center;background:#0f1729;}
table.flujo th{background:#1e293b;color:#f8faf4;}
img.diagrama{max-width:100%;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.45);background:#1e293b;}
.simulacro{background:rgba(245,158,11,.08);border:2px solid #f59e0b;color:#fef3c7;border-radius:10px;
     padding:14px 18px;margin-top:30px;}
.simulacro ol li{font-size:1.05em;margin:9px 0;color:#fef3c7;}
.badge{display:inline-block;background:#1e293b;color:#fbbf24;border-radius:20px;padding:2px 12px;
     font-weight:bold;font-size:.85em;border:1px solid #475569;}
.resp{background:rgba(34,197,94,.10);border:2px dashed #22c55e;color:#bbf7d0;border-radius:8px;
     padding:10px 14px;margin-top:10px;}
.indexol{color:#cbd5e1;} .indexol li{color:#cbd5e1;margin:4px 0;}
"""

def bloque(color, icono, titulo, contenido):
    return (f'<div class="bloque {color}"><h4>{icono} {titulo}</h4>{contenido}</div>')

def tema(t, d):
    h = [f'<h2 class="tema">📌 Tema: {t}</h2>']
    h.append(bloque("azul", "🧠", "1. Concepto Visual", d["concepto"]))
    h.append(bloque("rojo", "⚠️", "2. Trampas del Examen", d["trampas"]))
    h.append(bloque("mapa", "🗺️", "3. Mapa Mental / Flujo", d["mapa"]))
    if d.get("diagrama") in IMG:
        h.append(f'<img class="diagrama" src="data:image/png;base64,{IMG[d["diagrama"]]}" alt="diagrama"/>')
    h.append(bloque("verde", "💡", "4. Ejemplo y Practica", d["ejemplo"]))
    h.append(bloque("naranja", "🛠️", "5. Cheat Sheet / Formulas", d["cheat"]))
    h.append(bloque("recall", "🧠", "6. Repaso Activo", d["recall"]))
    h.append("<hr/>")
    return "\n".join(h)

print("Helpers OK")

# ============ CONTENIDO (con Repaso Activo) ============
def _t(titulo, concepto, trampas, mapa, ejemplo, cheat, recall, diagrama):
    return dict(titulo=titulo, concepto=concepto, trampas=trampas, mapa=mapa,
                ejemplo=ejemplo, cheat=cheat, recall=recall, diagrama=diagrama)

TEMAS = [
 _t("Teorema de Probabilidad Total y Bayes",
    "<p><b>Probabilidad total:</b> P(A) se forma <b>sumando</b> las ramas que llevan al resultado A desde causas excluyentes B1..Bn.</p>"
    "<p><b>Bayes:</b> invierte la pregunta: si ocurrió A, ¿qué tan probable es que venga de la causa Bk?</p>",
    "<p><b>Ojo:</b> confundir P(B|A) con P(A|B). &quot;De qué causa proviene&quot; divide la rama buscada entre P(A) total.</p>"
    "<p><b>Caza-bobos:</b> &quot;el 90% de las piezas buenas salen de M1&quot; NO es P(M1|buena).</p>",
    ("<table class='flujo'><tr><th>Causa</th><th>Rama</th><th>Resultado</th></tr>"
     "<tr><td>B1</td><td>P(B1)·P(A|B1)</td><td rowspan='3'>A</td></tr>"
     "<tr><td>B2</td><td>P(B2)·P(A|B2)</td></tr>"
     "<tr><td>B3</td><td>P(B3)·P(A|B3)</td></tr>"
     "<tr><td colspan='2'><b>P(A) total</b></td><td>Bayes: P(Bk|A)=rama/P(A)</td></tr></table>"),
    "<p><b>Ejemplo:</b> L1=50%, L2=30%, L3=20%; defectos 3%,4%,5%.</p>"
    "<ul><li><i>Paso 1:</i> P(D)=0.5·0.03+0.3·0.04+0.2·0.05=<b>0.037</b></li>"
    "<li><i>Paso 2:</i> P(L3|D)=0.2·0.05/0.037=<b>0.2703</b></li></ul>",
    "<ul><li>◾ P(A)=Σ P(Bi)·P(A|Bi)</li><li>◾ P(Bk|A)=P(Bk)·P(A|Bk)/P(A)</li>"
    "<li>◾ Denominador de Bayes = P(A) total del árbol</li></ul>",
    "<p><i>1)</i> Enuncia la fórmula del Teorema de Bayes y di qué representa el denominador.</p>"
    "<p><b>R:</b> P(Bk|A)=P(Bk)·P(A|Bk)/P(A); el denominador es la probabilidad total P(A).</p>"
    "<p><i>2)</i> Con 3 máquinas (50/30/20%, defectos 3/4/5%): ¿cuánto vale P(defectuosa) y P(L3|defectuosa)?</p>"
    "<p><b>R:</b> P(D)=0.037; P(L3|D)=0.010/0.037≈0.2703.</p>",
    "bayes"),

 _t("Distribución Binomial",
    "<p>Modela el <b>nº de éxitos</b> X en <b>n ensayos independientes</b> con probabilidad fija p. Interesan: exactamente, a lo más o al menos.</p>",
    "<p><b>Ojo:</b> &quot;al menos 2&quot; = 1 − P(0) − P(1). Si p pequeña y n grande → <b>Poisson λ=np</b>; si np y nq&gt;5 → <b>Normal</b>.</p>"
    "<p><b>Caza-bobos:</b> no confundir P(≥k) con P(&gt;k).</p>",
    ("<table class='flujo'><tr><th>Suceso</th><th>Fórmula</th><th>Resultado</th></tr>"
     "<tr><td>exactamente r</td><td>C(n,r)p^r q^(n−r)</td><td>probabilidad</td></tr>"
     "<tr><td>al menos k</td><td>1 − Σ menores</td><td>complemento</td></tr></table>"),
    "<p><b>Ejemplo:</b> tirador p=0.6, 5 disparos.</p>"
    "<ul><li><i>Paso 1:</i> P(X=3)=C(5,3)·0.6³·0.4²=<b>0.3456</b></li>"
    "<li><i>Paso 2:</i> P(≥2)=1−[0.4⁵+5·0.6·0.4⁴]=<b>0.91296</b></li></ul>",
    "<ul><li>◾ P(X=r)=C(n,r)p^r(1−p)^(n−r)</li><li>◾ μ=n·p; σ=√(n·p·q)</li>"
    "<li>◾ np,nq&gt;5 → Normal; p pequeña → Poisson λ=np</li></ul>",
    "<p><i>1)</i> Escribe P(X=r) de la binomial y su media y desvío.</p>"
    "<p><b>R:</b> P(X=r)=C(n,r)p^r q^(n−r); μ=n·p; σ=√(n·p·q).</p>"
    "<p><i>2)</i> Un tirador p=0.6 hace 5 disparos: ¿P(X=3) y P(X≥2)?</p>"
    "<p><b>R:</b> 0.3456 y 0.91296.</p>",
    "binomial"),

 _t("Distribución Normal",
    "<p>Distribución continua en <b>campana</b> (gaussiana), con media μ y desvío σ. Para resolver se <b>tipifica</b> z=(x−μ)/σ y se busca en la tabla N(0,1).</p>",
    "<p><b>Ojo:</b> tipificar SIEMPRE antes de leer la tabla; si z sale negativo usar simetría Φ(−z)=1−Φ(z).</p>"
    "<p><b>Caza-bobos:</b> invertir μ y x al tipificar.</p>",
    ("<table class='flujo'><tr><th>Quiero</th><th>Fórmula</th><th>Tabla</th></tr>"
     "<tr><td>P(X&lt;x)</td><td>z=(x−μ)/σ</td><td>Φ(z)</td></tr>"
     "<tr><td>P(X&gt;x)</td><td>z=(x−μ)/σ</td><td>1−Φ(z)</td></tr>"
     "<tr><td>percentil k</td><td>x=μ+z_k·σ</td><td>despejar z</td></tr></table>"),
    "<p><b>Ejemplo:</b> peso N(25, σ=4).</p>"
    "<ul><li><i>Paso 1:</i> P(X&lt;30): z=1.25 → <b>0.8944</b></li>"
    "<li><i>Paso 2:</i> percentil 90: z=1.28 → x=25+1.28·4=<b>30.12 kg</b></li></ul>",
    "<ul><li>◾ z=(x−μ)/σ</li><li>◾ P(X&gt;x)=1−Φ(z)</li>"
    "<li>◾ Simetría: Φ(−z)=1−Φ(z)</li></ul>",
    "<p><i>1)</i> Da la fórmula de la variable tipificada z y para qué sirve.</p>"
    "<p><b>R:</b> z=(x−μ)/σ; convierte X en una normal estándar N(0,1) para usar la tabla.</p>"
    "<p><i>2)</i> Peso N(25, σ=4): ¿P(X&lt;30) y el peso del percentil 90?</p>"
    "<p><b>R:</b> 0.8944 y 30.12 kg.</p>",
    None),
 _t("Distribución Exponencial",
    "<p>Modela <b>tiempos de espera</b> o <b>vida útil</b>. Con media μ, el parámetro es λ=1/μ; supervivencia P(X&gt;t)=e^(−λt).</p>",
    "<p><b>Ojo:</b> no confundir media con λ; primero λ=1/μ. P(X&gt;t) usa e^(−λt); P(X&lt;t) usa 1−e^(−λt).</p>"
    "<p><b>Caza-bobos:</b> usar λ directamente donde va la media.</p>",
    ("<table class='flujo'><tr><th>Piden</th><th>Usar</th></tr>"
     "<tr><td>P(X&gt;t) durar más</td><td>e^(−λt)</td></tr>"
     "<tr><td>P(X&lt;t) fallar antes</td><td>1−e^(−λt)</td></tr>"
     "<tr><td>λ a partir de media μ</td><td>λ=1/μ</td></tr></table>"),
    "<p><b>Ejemplo:</b> vida media 8 años.</p>"
    "<ul><li><i>Paso 1:</i> λ=1/8</li>"
    "<li><i>Paso 2:</i> P(X&gt;10)=e^(−1.25)=<b>0.2865</b></li>"
    "<li><i>Paso 3:</i> P(X&lt;4)=1−e^(−0.5)=<b>0.3935</b></li></ul>",
    "<ul><li>◾ λ=1/μ (nunca usar μ como λ)</li><li>◾ P(X&gt;t)=e^(−λt)</li>"
    "<li>◾ Media=1/λ; varianza=1/λ²</li></ul>",
    "<p><i>1)</i> Si la vida media es 8 años, ¿qué valor toma λ y P(X&gt;10)?</p>"
    "<p><b>R:</b> λ=1/8; P(X&gt;10)=e^(−1.25)≈0.2865.</p>"
    "<p><i>2)</i> ¿Qué fórmula usas para el tiempo de espera &quot;mayor que t&quot; y para &quot;menor que t&quot;?</p>"
    "<p><b>R:</b> e^(−λt) y 1−e^(−λt).</p>",
    None),

 _t("Variable Aleatoria Continua (cálculo de k)",
    "<p>En densidad continua el área bajo la curva da la probabilidad. Primero se calcula <b>k</b> con ∫ f(x)dx=1, luego se integra para P(a&lt;X&lt;b) y E(X)=∫ x·f(x)dx.</p>",
    "<p><b>Ojo:</b> el área total DEBE valer 1 antes de calcular cualquier probabilidad. No olvides integrar entre los extremos correctos del dominio.</p>"
    "<p><b>Caza-bobos:</b> usar el valor de f(x) sin integrar.</p>",
    ("<table class='flujo'><tr><th>Quiero</th><th>Fórmula</th></tr>"
     "<tr><td>constante k</td><td>∫ f(x)dx = 1</td></tr>"
     "<tr><td>P(a&lt;X&lt;b)</td><td>∫ₐ f(x)dx</td></tr>"
     "<tr><td>E(X)</td><td>∫ x·f(x)dx</td></tr></table>"),
    "<p><b>Ejemplo:</b> f(x)=k·x en [0,2].</p>"
    "<ul><li><i>Paso 1:</i> k·[x²/2]₀²=2k=1 → <b>k=1/2</b></li>"
    "<li><i>Paso 2:</i> P(0.5&lt;X&lt;1.5)=<b>0.5</b></li>"
    "<li><i>Paso 3:</i> E(X)=<b>4/3</b></li></ul>",
    "<ul><li>◾ k: ∫ f(x)dx = 1</li><li>◾ P(a&lt;X&lt;b)=∫ₐ f(x)dx</li>"
    "<li>◾ E(X)=∫ x·f(x)dx</li></ul>",
    "<p><i>1)</i> ¿Qué condición debe cumplir una función de densidad f(x)?</p>"
    "<p><b>R:</b> f(x)≥0 y el área total ∫f(x)dx=1.</p>"
    "<p><i>2)</i> Para f(x)=k·x en [0,2]: ¿cuánto vale k y P(0.5&lt;X&lt;1.5)?</p>"
        "<p><b>R:</b> k=1/2 y P=0.5.</p>",
    None),

 _t("Variable Aleatoria Discreta (tabla, E, Var)",
    "<p>X toma valores enteros con probabilidades p(x). Siempre Σp(x)=1. E(X)=Σ x·p(x); Var(X)=Σ x²·p(x) − [E(X)]².</p>",
    "<p><b>Ojo:</b> la suma de probabilidades debe dar 1; para la varianza restar E al cuadrado al FINAL.</p>"
    "<p><b>Caza-bobos:</b> calcular E(X²) como [E(X)]².</p>",
    ("<table class='flujo'><tr><th>Valor x</th><td>x1</td><td>x2</td><td>...</td></tr>"
     "<tr><th>p(x)</th><td>p1</td><td>p2</td><td>...</td></tr>"
     "<tr><td colspan='4'>E(X)=Σx·p; Var=Σx²p − E²</td></tr></table>"),
    "<p><b>Ejemplo:</b> diferencia de dos dados (0..5): p=(6,10,8,6,4,2)/36.</p>"
    "<ul><li><i>Paso 1:</i> E(X)=(0+10+16+18+16+10)/36=<b>35/18≈1.944</b></li>"
    "<li><i>Paso 2:</i> E(X²)=210/36=35/6</li>"
    "<li><i>Paso 3:</i> Var=35/6−(35/18)²=<b>≈2.05</b></li></ul>",
    "<ul><li>◾ Σ p(x)=1 (verificar)</li><li>◾ E(X)=Σ x·p(x)</li>"
    "<li>◾ Var(X)=Σ x²·p(x) − (E(X))²</li></ul>",
    "<p><i>1)</i> Escribe E(X) y Var(X) para una variable aleatoria discreta.</p>"
    "<p><b>R:</b> E(X)=Σx·p(x); Var(X)=Σx²·p(x)−[E(X)]².</p>"
    "<p><i>2)</i> Para la diferencia de dos dados (p=(6,10,8,6,4,2)/36): ¿E(X) y Var(X)?</p>"
    "<p><b>R:</b> E=35/18≈1.944; Var≈2.05.</p>",
    None),

 _t("Probabilidad Condicional e Independencia",
    "<p>P(B|A) es la probabilidad de B dado que ocurrió A; el espacio muestral se <b>reduce a A</b>. Si P(A∩B)=P(A)·P(B), A y B son independientes.</p>",
    "<p><b>Ojo:</b> con &quot;sin reemplazo&quot; el denominador baja en 1 en cada extracción; con reemplazo es constante.</p>"
    "<p><b>Caza-bobos:</b> confundir con Bayes (aquí no hay causas previas).</p>",
    ("<table class='flujo'><tr><th>Con reemplazo</th><th>Sin reemplazo</th></tr>"
     "<tr><td>independientes P(A∩B)=P(A)P(B)</td><td>P(A∩B)=P(A)P(B|A)</td></tr>"
     "<tr><td>denominador constante</td><td>denominador cambia</td></tr></table>"),
    "<p><b>Ejemplo:</b> cartas sin reemplazo.</p>"
    "<ul><li><i>Paso 1:</i> 2º as si 1º no fue: <b>4/51≈0.0784</b></li>"
    "<li><i>Paso 2:</i> ambos ases: (4/52)·(3/51)=<b>1/221</b></li></ul>",
    "<ul><li>◾ P(B|A)=P(A∩B)/P(A)</li><li>◾ P(A∩B)=P(A)·P(B|A)</li>"
    "<li>◾ Independencia ⟺ P(A∩B)=P(A)P(B)</li></ul>",
    "<p><i>1)</i> ¿Cuándo dos sucesos A y B son independientes?</p>"
    "<p><b>R:</b> cuando P(A∩B)=P(A)·P(B) (la ocurrencia de uno no afecta al otro).</p>"
    "<p><i>2)</i> De una baraja, si la 1ª carta NO fue un as, ¿P(2ª sea as) sin reemplazo?</p>"
    "<p><b>R:</b> 4/51≈0.0784.</p>",
    None),
 _t("Distribución Geométrica",
    "<p>Cuenta <b>hasta cuántos ensayos hay que esperar para el primer éxito</b>. P(X=r)=q^(r−1)·p; media=1/p.</p>",
    "<p><b>Ojo:</b> es de &quot;hasta que aparece&quot;. No confundir con binomial (n fijo) ni con binomial negativa (hasta el r-ésimo éxito).</p>"
    "<p><b>Caza-bobos:</b> olvidar que la primera vez puede ser r=1 con probabilidad p.</p>",
    ("<table class='flujo'><tr><th>Intento r</th><th>1</th><th>2</th><th>3</th></tr>"
     "<tr><th>P(X=r)</th><td>p</td><td>q·p</td><td>q²·p</td></tr></table>"),
    "<p><b>Ejemplo:</b> acierto con p=0.2.</p>"
    "<ul><li><i>Paso 1:</i> primer éxito en el 4º: (0.8)³·0.2=<b>0.1024</b></li>"
    "<li><i>Paso 2:</i> esperado 1/p=<b>5</b></li></ul>",
    "<ul><li>◾ P(X=r)=q^(r−1)·p</li><li>◾ E(X)=1/p; Var=q/p²</li>"
    "<li>◾ &quot;primer éxito&quot; → geométrica</li></ul>",
    "<p><i>1)</i> Si la probabilidad de éxito es p, ¿cuál es la probabilidad de que el primer éxito ocurra en el ensayo r?</p>"
    "<p><b>R:</b> P(X=r)=q^(r−1)·p, con q=1−p.</p>"
    "<p><i>2)</i> Con p=0.2: ¿P(primer éxito en el 4º intento) y el número esperado?</p>"
    "<p><b>R:</b> 0.1024 y 5.</p>",
    None),

 _t("Distribución de Poisson",
    "<p>Modela <b>sucesos raros</b> en un intervalo fijo (llamadas/min, errores/página). P(X=r)=e^(−λ)·λ^r/r!; λ es la tasa media; E=Var=λ.</p>",
    "<p><b>Ojo:</b> aproxima la binomial cuando n grande y p pequeña con λ=np (np&lt;5). No confundir λ (media) con r (lo que se pregunta).</p>"
    "<p><b>Caza-bobos:</b> olvidar el factorial en el denominador.</p>",
    ("<table class='flujo'><tr><th>Quiero</th><th>Fórmula</th></tr>"
     "<tr><td>P(X=r)</td><td>e^(−λ)·λ^r/r!</td></tr>"
     "<tr><td>al menos 2</td><td>1−[P(0)+P(1)]</td></tr></table>"),
    "<p><b>Ejemplo:</b> 6 llamadas/min.</p>"
    "<ul><li><i>Paso 1:</i> P(X=4)=e^(−6)·6⁴/4!=<b>0.1339</b></li>"
    "<li><i>Paso 2:</i> P(≥2)=1−e^(−6)(1+6)=<b>0.9826</b></li></ul>",
    "<ul><li>◾ P(X=r)=e^(−λ)λ^r/r!</li><li>◾ E(X)=Var(X)=λ</li>"
    "<li>◾ Binomial→Poisson con λ=np</li></ul>",
    "<p><i>1)</i> Escribe la fórmula de P(X=r) en Poisson y su media/varianza.</p>"
    "<p><b>R:</b> P(X=r)=e^(−λ)λ^r/r!; E(X)=Var(X)=λ.</p>"
    "<p><i>2)</i> Con 6 llamadas/min: ¿P(X=4) y P(X≥2)?</p>"
    "<p><b>R:</b> 0.1339 y 0.9826.</p>",
    None),

 _t("Distribución Hipergeométrica",
    "<p>Modela el <b>nº de éxitos con muestreo SIN reemplazo</b> en población finita. P(X=r)=[C(b,r)·C(s,n−r)]/C(b+s,n).</p>",
    "<p><b>Ojo:</b> &quot;sin reemplazo&quot; en población pequeña → hipergeométrica; con reemplazo o población grande → binomial.</p>"
    "<p><b>Caza-bobos:</b> usar C(b,r) sin el C(s,n−r).</p>",
    ("<table class='flujo'><tr><th>Componente</th><th>Valor</th></tr>"
     "<tr><td>3 rojas, 2 azules; saco 2</td><td>P(1 roja)=[C(3,1)C(2,1)]/C(5,2)=0.6</td></tr></table>"),
    "<p><b>Ejemplo:</b> 10 piezas, 4 defectuosas; tomo 3 sin reemplazo.</p>"
    "<ul><li><i>Paso 1:</i> P(1 def.)=[C(4,1)·C(6,2)]/C(10,3)</li>"
    "<li><i>Paso 2:</i> (4·15)/120=<b>0.5</b></li></ul>",
    "<ul><li>◾ P=[C(b,r)·C(s,n−r)]/C(b+s,n)</li><li>◾ sin reemplazo, población finita</li>"
    "<li>◾ Media=n·b/(b+s)</li></ul>",
    "<p><i>1)</i> ¿Cuándo se usa la hipergeométrica en lugar de la binomial?</p>"
    "<p><b>R:</b> cuando el muestreo es SIN reemplazo en una población finita.</p>"
    "<p><i>2)</i> De 10 piezas (4 defectuosas) tomas 3 sin reemplazo: ¿P(exactamente 1 defectuosa)?</p>"
    "<p><b>R:</b> [C(4,1)C(6,2)]/C(10,3)=0.5.</p>",
    None),

 _t("Análisis Combinatorio y Permutaciones",
    "<p>Técnicas de <b>conteo</b> para espacios equiprobables. Permutación: importa el orden P(n,r)=n!/(n−r)!. Combinación: no importa C(n,r)=n!/[r!(n−r)!]. P(A)=favorables/posibles.</p>",
    "<p><b>Ojo:</b> decidir si el orden importa: importa → permutación; no importa → combinación. Con repetición se multiplican potencias; sin repetición se usa factorial.</p>"
    "<p><b>Caza-bobos:</b> usar combinación cuando es permutación (y viceversa).</p>",
    ("<table class='flujo'><tr><th>Operación</th><th>Fórmula</th><th>Ejemplo</th></tr>"
     "<tr><td>Permutación</td><td>P(5,2)=20</td><td>AB ≠ BA</td></tr>"
     "<tr><td>Combinación</td><td>C(5,2)=10</td><td>AB = BA</td></tr></table>"),
    "<p><b>Ejemplo:</b> 5 bolas numeradas, saco 2.</p>"
    "<ul><li><i>Paso 1:</i> ordenados P(5,2)=<b>20</b></li>"
    "<li><i>Paso 2:</i> sin orden C(5,2)=<b>10</b></li>"
    "<li><i>Paso 3:</i> sacar '1' y '2' en algún orden: 2/20=<b>0.1</b></li></ul>",
    "<ul><li>◾ P(n,r)=n!/(n−r)!</li><li>◾ C(n,r)=n!/[r!(n−r)!]</li>"
    "<li>◾ P(A)=favorables/posibles</li></ul>",
    "<p><i>1)</i> ¿Cuándo usas permutación y cuándo combinación? Da sus fórmulas.</p>"
    "<p><b>R:</b> permutación si importa el orden P(n,r)=n!/(n−r)!; combinación si no C(n,r)=n!/[r!(n−r)!].</p>"
    "<p><i>2)</i> Con 5 bolas sacas 2: ¿cuántos ordenados y cuántos sin orden?</p>"
    "<p><b>R:</b> 20 (permutación) y 10 (combinación).</p>",
    None),

]
print("Temas lote2 OK:", len(TEMAS))

print("Temas OK total:", len(TEMAS))

# ============ ÁRBOL DE DECISIÓN (elegir fórmula) ============
arbol_html = ("<div class='bloque mapa'><h4>🌳 Árbol de Decisión: elige la fórmula según el enunciado</h4>"
 "<table class='flujo'><tr><th>Pregunta clave del enunciado</th><th>Si es SÍ → usa</th></tr>"
 "<tr><td>¿&quot;De qué causa proviene el resultado&quot;?</td><td>Bayes / Probabilidad total</td></tr>"
 "<tr><td>¿Tiempo de espera o vida útil?</td><td>Exponencial (λ=1/μ)</td></tr>"
 "<tr><td>¿Variable continua &quot;en campana&quot; (media y desvío)?</td><td>Normal (z=(x−μ)/σ)</td></tr>"
 "<tr><td>¿Sucesos raros en un intervalo (tasa λ)?</td><td>Poisson (P=e^(−λ)λ^r/r!)</td></tr>"
 "<tr><td>¿&quot;Hasta que ocurre el primer éxito&quot;?</td><td>Geométrica (q^(r−1)·p)</td></tr>"
 "<tr><td>¿Muestreo SIN reemplazo en población finita?</td><td>Hipergeométrica [C(b,r)C(s,n−r)]/C(total,n)</td></tr>"
 "<tr><td>¿n ensayos independientes con prob. fija p?</td><td>Binomial (C(n,r)p^r q^(n−r))</td></tr>"
 "<tr><td>¿Contar casos (¿importa el orden?).</td><td>Permutación o Combinación</td></tr>"
 "</table></div>")

# ============ TABLA DE NOTACIÓN DE SÍMBOLOS ============
notacion_html = ("<div class='bloque mapa'><h4>🔣 Tabla de Notación de Símbolos</h4>"
 "<table class='flujo'><tr><th>Símbolo</th><th>Significado</th></tr>"
 "<tr><td>P(A)</td><td>Probabilidad del suceso A</td></tr>"
 "<tr><td>P(A|B)</td><td>Probabilidad de A dado que ocurrió B (condicional)</td></tr>"
 "<tr><td>P(A∩B)</td><td>Probabilidad de que ocurran A y B a la vez</td></tr>"
 "<tr><td>n</td><td>Número de ensayos / tamaño de muestra</td></tr>"
 "<tr><td>p / q</td><td>Probabilidad de éxito / de fracaso (q=1−p)</td></tr>"
 "<tr><td>μ (media) / σ / σ²</td><td>Media / desvío estándar / varianza</td></tr>"
 "<tr><td>λ</td><td>Tasa media (Poisson y exponencial)</td></tr>"
 "<tr><td>X ~ N(μ,σ)</td><td>Variable normal con media μ y desvío σ</td></tr>"
 "<tr><td>z</td><td>Valor tipificado z=(x−μ)/σ</td></tr>"
 "<tr><td>Φ(z)</td><td>Función de distribución de la normal estándar</td></tr>"
 "<tr><td>C(n,r)</td><td>Combinaciones de n en r (sin orden)</td></tr>"
 "<tr><td>E(X) / Var(X)</td><td>Esperanza (media) / varianza de X</td></tr>"
 "<tr><td>∫</td><td>Integral (área bajo densidad continua)</td></tr>"
 "<tr><td>e^(−λt)</td><td>Factor de supervivencia exponencial</td></tr>"
 "</table></div>")

# ============ SIMULACRO (problemas reales de examen) ============
simulacro_q = [
 "1) Una fábrica produce piezas en 3 máquinas: L1=50%, L2=30%, L3=20%; defectos 3%, 4%, 5%. Se elige una pieza. a) ¿P(defectuosa)? b) Si fue defectuosa, ¿P(proviene de L1)?",
 "2) En un examen de 5 preguntas de opción múltiple, p=0.25 de acertar cada una. a) ¿P(aclarar exactamente 2)? b) ¿P(al menos 1)?",
 "3) El 40% de una colonia usa autobús. Muestra de 100. ¿P(más de 45 usen)? ¿P(entre 35 y 50 inclusive)? (aprox. normal con corrección de continuidad)",
 "4) El peso de un paquete es N(25, σ=4). a) ¿P(pese < 30)? b) ¿Qué peso deja debajo al 90%?",
 "5) Vida media de 8 años (exponencial). a) ¿P(dure > 10)? b) ¿P(falle antes de 4)?",
 "6) Densidad f(x)=k·x en [0,2]. a) k. b) P(0.5<X<1.5). c) E(X).",
 "7) Dos dados, X=|d1−d2|. a) Tabla. b) E(X). c) Var(X).",
 "8) Baraja de 52, sacas 2 sin reposición. a) ¿P(2ª sea as si 1ª no fue as)? b) ¿P(ambas ases)?",
 "9) 6 llamadas/min (Poisson). a) ¿P(exactamente 4)? b) ¿P(al menos 2)?",
 "10) 10 piezas, 4 defectuosas; tomas 3 SIN reemplazo. ¿P(exactamente 1 defectuosa)?",
]
simulacro_r = [
 "<b>1)</b> P(D)=0.5·0.03+0.3·0.04+0.2·0.05=<b>0.037</b>; P(L1|D)=0.015/0.037=<b>≈0.4054</b>.",
 "<b>2)</b> P(X=2)=C(5,2)·0.25²·0.75³=<b>0.2637</b>; P(≥1)=1−0.75⁵=<b>0.7627</b>.",
 "<b>3)</b> μ=40, σ≈4.899. P(&gt;45)=1−Φ(1.122)=<b>≈0.131</b>; P(35≤X≤50)=Φ(2.143)−Φ(−1.122)=<b>≈0.853</b>.",
 "<b>4)</b> P(X&lt;30): z=1.25 → <b>0.8944</b>; percentil 90: z=1.28 → <b>30.12 kg</b>.",
 "<b>5)</b> λ=1/8. P(X&gt;10)=e^(−1.25)=<b>0.2865</b>; P(X&lt;4)=1−e^(−0.5)=<b>0.3935</b>.",
 "<b>6)</b> k=1/2; P(0.5&lt;X&lt;1.5)=<b>0.5</b>; E(X)=<b>4/3</b>.",
 "<b>7)</b> p=(6,10,8,6,4,2)/36; E(X)=<b>35/18≈1.944</b>; Var=<b>≈2.05</b>.",
 "<b>8)</b> P=4/51=<b>0.0784</b>; P(ambas)=(4/52)(3/51)=<b>1/221</b>.",
 "<b>9)</b> P(X=4)=e^(−6)·6⁴/4!=<b>0.1339</b>; P(≥2)=1−e^(−6)(1+6)=<b>0.9826</b>.",
 "<b>10)</b> P=[C(4,1)C(6,2)]/C(10,3)=(4·15)/120=<b>0.5</b>.",
]
sim_html = ['<div class="simulacro"><h3 style="color:#78350F">🚨 Simulacro de Emergencia (problemas de examen)</h3>']
sim_html.append("<ol>")
for item in simulacro_q:
    sim_html.append(f"<li>{item}</li>")
sim_html.append("</ol>")
sim_html.append('<div class="resp"><h4 style="background:#22C55E;color:#fff;display:inline-block;padding:2px 10px;border-radius:6px">RESPUESTAS EXPLICADAS</h4>')
for item in simulacro_r:
    sim_html.append(f"<p>{item}</p>")
sim_html.append("</div></div>")

# ============ CONSTRUCCIÓN DE LA PÁGINA ============
tabla_freq = ("<table class='flujo'><tr><th>Tema</th><th>Frecuencia</th><th>Prioridad</th></tr>"
 "<tr><td>Bayes / Prob. Total</td><td>6/8</td><td>🔵 Alta</td></tr>"
 "<tr><td>Normal</td><td>6/8</td><td>🔵 Alta</td></tr>"
 "<tr><td>Binomial</td><td>6/8</td><td>🔵 Alta</td></tr>"
 "<tr><td>V.A. Continua / Discreta</td><td>4/8</td><td>🔵 Alta</td></tr>"
 "<tr><td>Exponencial</td><td>4/8</td><td>🔵 Alta</td></tr>"
 "<tr><td>Condicional / Geométrica / Poisson / Hipergeom. / Combinatoria</td><td>1–3/8</td><td>🟡 Media/Baja</td></tr></table>")

body = [f"<header><h1>🎓 GUÍA VISUAL DE ESTUDIO: PROBABILIDAD</h1>"
        f"<p>Metodología visual ParetoTutor · 🔵 conceptos · 🔴 trampas · 🗺️ mapas · 🟢 ejemplos · 🟠 fórmulas · 🧠 repaso activo</p>"
        f"<p><span class='badge'>8 exámenes únicos analizados</span> "
        f"<span class='badge'>40 reactivos</span> "
        f"<span class='badge'>Libro de 388 pp.</span></p></header>"]

body.append("<h2 class='seccion'>🌳 Decide la fórmula</h2>")
body.append(arbol_html)

body.append("<h2 class='seccion'>🔣 Notación de símbolos</h2>")
body.append(notacion_html)

body.append("<h2 class='seccion'>📊 Análisis de frecuencia (Top 20%)</h2>")
body.append(bloque("azul", "📈", "Frecuencia de temas", tabla_freq))

body.append("<h2 class='seccion'>🗂️ Índice de temas</h2>")
body.append("<ol class='indexol'>")
for t in TEMAS:
    body.append(f"<li>{t['titulo']}</li>")
body.append("</ol>")

for t in TEMAS:
    body.append(tema(t["titulo"], t))

body.append("".join(sim_html))

html = ("<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
        "<title>Guía Visual de Probabilidad</title><style>" + CSS + "</style></head><body>"
        + "\n".join(body) + "</body></html>")

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("GUARDADO:", HTML_OUT)
print("Temas:", len(TEMAS), "| Bytes HTML:", len(html))

