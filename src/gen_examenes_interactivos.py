#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador maestro de Examenes Interactivos de Probabilidad - ParetoTutor Visual.
Calcula valores numericos exactos con Python y genera un HTML interactivo
con opcion multiple, soluciones detalladas y codigo de colores visual.
"""
import os
import math

OUT = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Examenes_Interactivos_Probabilidad.html"

# ===== Funciones de probabilidad precisas =====
def comb(n, k):
    return math.comb(n, k)

def norm_cdf(z):
    """CDF de la normal estandar."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

def binom_pmf(n, p, k):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binom_cdf(n, p, k):
    s = 0.0
    for i in range(0, k + 1):
        s += binom_pmf(n, p, i)
    return s

def poisson_pmf(lam, k):
    return math.exp(-lam) * (lam ** k) / math.factorial(k)

def poisson_cdf(lam, k):
    s = 0.0
    for i in range(0, k + 1):
        s += poisson_pmf(lam, i)
    return s

CSS = """
<style>
body{font-family:Segoe UI;background:#0F172A;color:#e2e8f0;line-height:1.6;margin:0;padding:20px}
h1{color:#bae6fd;text-align:center;border-bottom:3px solid #38bdf8;padding-bottom:10px}
h2{color:#38bdf8;margin-top:40px;border-left:5px solid #38bdf8;padding-left:10px}
h3{color:#fef3c7;margin-top:25px}
.container{max-width:1100px;margin:0 auto;padding:20px;background:rgba(15,23,42,0.8);border-radius:10px;box-shadow:0 0 20px rgba(56,189,248,0.2)}
.question{background:rgba(255,255,255,0.05);border-left:4px solid #38bdf8;padding:15px;margin-bottom:20px;border-radius:5px}
.options{display:flex;flex-direction:column;gap:8px;margin:12px 0}
.option{display:flex;align-items:center;background:rgba(56,189,248,0.1);border:2px solid #38bdf8;color:#bae6fd;padding:8px;border-radius:5px;cursor:pointer}
.option:hover{background:rgba(56,189,248,0.2)}
.solution{background:rgba(34,197,94,0.1);border-left:4px solid #22c55e;padding:12px;margin-top:10px;border-radius:5px;display:none}
.btn-toggle{background:#f59e0b;color:#0f1729;border:none;padding:6px 12px;border-radius:5px;cursor:pointer;font-weight:bold;margin-top:8px}
.formula-box{background:rgba(245,158,11,0.1);border:2px solid #f59e0b;color:#fef3c7;padding:8px;border-radius:5px;font-family:monospace;text-align:center;margin:8px 0}
.tip-box{background:rgba(248,113,113,0.1);border:2px solid #ef4444;color:#fecaca;padding:8px;border-radius:5px;font-size:0.9em;margin-top:6px}
.concept-box{background:rgba(56,189,248,0.1);border:2px solid #38bdf8;color:#bae6fd;padding:8px;border-radius:5px;font-size:0.9em}
.example-box{background:rgba(34,197,94,0.1);border:2px solid #22c55e;color:#bbf7d0;padding:8px;border-radius:5px;font-size:0.9em;margin-top:6px}
table.symb{border-collapse:collapse;margin:10px auto;width:100%}
table.symb th,table.symb td{border:1px solid #475569;padding:6px 10px;text-align:left}
table.symb th{background:rgba(100,116,139,0.2);color:#e0e0ff}
.tree{background:rgba(30,41,59,0.9);border:2px dashed #475569;color:#cbd5e1;padding:12px;border-radius:8px;font-family:monospace;white-space:pre;overflow-x:auto;margin:10px 0;line-height:1.45}
.nav{background:rgba(15,23,42,0.9);padding:12px;border-radius:8px;margin-bottom:20px;text-align:center}
.nav a{color:#38bdf8;text-decoration:none;margin:3px 8px;font-weight:bold}
.nav a:hover{color:#bae6fd;text-decoration:underline}
.footer{text-align:center;margin-top:40px;padding:12px;color:#64748b;font-size:0.9em}
</style>
"""

def q(qn, qid, txt, opts, sol, ans="A"):
    html = f'\n<div class="question"><p><strong>{qn}. {txt}</strong></p>\n<div class="options">\n'
    for i, o in enumerate(opts):
        html += f'<label class="option"><input type="radio" name="{qid}"> {chr(65+i)}) {o}</label>\n'
    sol = f'<div class="example-box">✅ <strong>Respuesta correcta: {ans})</strong></div>' + sol
    html += f"</div>\n<button class='btn-toggle' onclick=\"toggleSolution('{qid}')\">🔍 Ver Solución</button>\n<div id='{qid}' class='solution'>{sol}</div>\n</div>\n"
    return html

# ===== DATOS DE LOS EXÁMENES =====

# ---- Precalculo de valores (Examen 1) ----
pD = 0.5*0.03 + 0.3*0.04 + 0.2*0.05   # 0.037
pL3D = (0.2*0.05) / pD                 # 0.2703
mu2 = 500*0.05                          # 25
sg2 = math.sqrt(500*0.05*0.95)         # 4.873
p2a = norm_cdf((30.5-mu2)/sg2) - norm_cdf((24.5-mu2)/sg2)
p2b = 1 - norm_cdf((22.5-mu2)/sg2)

EX = {}

# --- EXAMEN 1: EXTRAORDINARIO 2019 ---
EX["exam1"] = ("EXAMEN EXTRAORDINARIO (2019)", "Turno Vespertino / 22-Ene-2019", [
    q("1", "q1ab",
      "(Probabilidad Total y Bayes) Una fábrica tiene 3 líneas: L1=50%, L2=30%, L3=20%. Las piezas defectuosas son: L1=3%, L2=4%, L3=5%. (a) ¿Cuál es la probabilidad de que una pieza elegida al azar sea defectuosa? (b) Si salió defectuosa, ¿cuál es la probabilidad de que provenga de L3?",
      [f"(a) {pD:.3f}, (b) {pL3D:.3f}",
       f"(a) {pD:.4f}, (b) {0.5*0.03/pD:.4f}",
       f"(a) {pD+0.005:.3f}, (b) {pL3D:.3f}",
       f"(a) {pD:.3f}, (b) {pL3D-0.05:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Ley de Probabilidad Total y Teorema de Bayes.</div>'
      '<div class="formula-box">(a) P(D) = P(L₁)·P(D|L₁) + P(L₂)·P(D|L₂) + P(L₃)·P(D|L₃)</div>'
      '<div class="example-box">🟢 0.50×0.03 + 0.30×0.04 + 0.20×0.05 = 0.015 + 0.012 + 0.010 = '
      f'<strong>{pD:.3f} ({(pD*100):.1f}%)</strong></div>'
      '<div class="formula-box">(b) P(L₃|D) = [P(L₃)·P(D|L₃)] / P(D)</div>'
      f'<div class="example-box">🟢 (0.20×0.05) / {pD:.3f} = 0.010 / {pD:.3f} = <strong>{pL3D:.3f} ({(pL3D*100):.1f}%)</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> El denominador SIEMPRE es P(D) total = 0.037, no solo una línea.</div>'),
    q("2", "q2ab",
      "(Aproximación Normal a la Binomial) El 5% de los libros prestados son técnicos. De 500 préstamos: (a) ¿P(entre 25 y 30 inclusive sean técnicos)? (b) ¿P(más de 22 sean técnicos)?",
      [f"(a) {p2a:.3f}, (b) {p2b:.3f}",
       f"(a) {p2a+0.03:.3f}, (b) {p2b+0.04:.3f}",
       f"(a) {p2a-0.02:.3f}, (b) {p2b-0.03:.3f}",
       f"(a) {p2a+0.05:.3f}, (b) {p2b-0.05:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Aproximación normal a binomial con corrección de continuidad (±0.5).</div>'
      f'<div class="formula-box">μ = n·p = 500×0.05 = <strong>{mu2:.0f}</strong>; σ = √(n·p·q) = √23.75 ≈ <strong>{sg2:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Aplicar corrección de ±0.5 (continuidad) antes de tipificar.</div>'
      '<div class="example-box">🟢 <strong>(a)</strong> Entre 25 y 30 (incl.) → 24.5 a 30.5<br>'
      f'z₁ ≈ {((24.5-mu2)/sg2):.2f} , z₂ ≈ {((30.5-mu2)/sg2):.2f}<br>'
      f'P ≈ Φ({((30.5-mu2)/sg2):.2f}) − Φ({((24.5-mu2)/sg2):.2f}) = <strong>{p2a:.3f}</strong></div>'
      '<div class="example-box">🟢 <strong>(b)</strong> Más de 22 → X > 22.5<br>'
      f'z ≈ {((22.5-mu2)/sg2):.2f} → P = 1 − Φ({((22.5-mu2)/sg2):.2f}) = <strong>{p2b:.3f}</strong></div>'),
])

# --- EXAMEN 2: SUFICIENCIA 2017 MATUTINO ---
EX["exam2"] = ("EXAMEN SUFICIENCIA 2017 (MATUTINO)", "Turno Matutino / 17-Ene-2017", [
    q("2", "qsuma",
      "(V.A.D. - Dados) Un dado se lanza dos veces. Sea X la suma obtenida. (a) Construye la distribución de probabilidad de X. (b) Calcula E(X) y Var(X).",
      ["E(X)=7, Var≈2.92", "E(X)=7, Var≈5.83", "E(X)=6.5, Var≈6.25", "E(X)=7.5, Var≈2.92"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> 36 resultados equiprobables; sumas 2..12 con frecuencias 1,2,3,4,5,6,5,4,3,2,1.</div>'
      '<div class="formula-box">E(X) = 252/36 = <strong>7</strong></div>'
      '<div class="formula-box">Var(X) = E(X²) − [E(X)]² = 329/36 − 49 = <strong>35/12 ≈ 2.92</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> La suma 7 tiene 6 combinaciones; es la más probable.</div>'),
    q("3", "q3abcd",
      "(Probabilidad Condicional y Bayes) En un grupo, 60% son hombres. El 30% de los hombres y el 20% de las mujeres usan lentes. (a) ¿P(no use lentes)? (b) Si usa lentes, ¿P(hombre)?",
      ["(a) 0.74, (b) ≈ 0.69", "(a) 0.74, (b) ≈ 0.24", "(a) 0.26, (b) ≈ 0.69", "(a) 0.82, (b) ≈ 0.69"],
      '<div class="formula-box">(a) P(No L) = 0.6×0.7 + 0.4×0.8 = 0.42 + 0.32 = <strong>0.74</strong></div>'
      '<div class="formula-box">(b) P(H|L) = (0.6×0.3) / (0.26) = 0.18/0.26 ≈ <strong>0.69</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> El denominador es P(L)=0.26, NO P(no L)=0.74.</div>'),
    q("5", "q5abcd",
      "(Distribución Normal) El tiempo de vuelo CDMX−MTY es 95 min, σ²=9 min². (a) ¿P(X<90)? (b) ¿Tiempo mínimo del 15% de vuelos más lentos?",
      ["(a) ≈ 0.0475, (b) ≈ 98.1 min", "(a) ≈ 0.4522, (b) ≈ 98.1 min", "(a) ≈ 0.0475, (b) ≈ 91.9 min", "(a) ≈ 0.9545, (b) ≈ 98.1 min"],
      '<div class="formula-box">μ = 95; σ = √9 = 3</div>'
      '<div class="example-box">🟢 (a) z = (90−95)/3 = −1.67 → Φ(−1.67) ≈ <strong>0.0475</strong></div>'
      '<div class="example-box">🟢 (b) Percentil 85 → z≈1.036 → x = 95 + 1.036×3 ≈ <strong>98.1 min</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Usar σ=3 al tipificar, no σ²=9.</div>'),
])

# ---- Precalculo de valores (Examen 3) ----
# Q1 VAD f(x)=(x^2-2x)/50 para x=3,4,5,6
px = [3/50, 8/50, 15/50, 24/50]
ex3 = 3*px[0] + 4*px[1] + 5*px[2] + 6*px[3]
ex2_3 = 9*px[0] + 16*px[1] + 25*px[2] + 36*px[3]
sd3 = math.sqrt(ex2_3 - ex3**2)
# Q3 Binomial p=0.8 n=5
p3a = binom_cdf(5, 0.8, 3)
p3b = 1 - binom_cdf(5, 0.8, 1)
# Q4 Poisson lambda=10
p4a = poisson_cdf(10, 5)
p4b = 1 - poisson_cdf(10, 10)
# Q5 Normal mu=25 sigma=5
p5a = norm_cdf((20-25)/5)
p5b = norm_cdf((30-25)/5) - norm_cdf((22-25)/5)

# --- EXAMEN 3: SUFICIENCIA 2012 MATUTINO ---
EX["exam3"] = ("EXAMEN SUFICIENCIA 2012 (MATUTINO)", "Turno Matutino / 13-Ago-2012", [
    q("1", "q3_1ab",
      "(V.A.D.) f(x)=(x²−2x)/50 para x=3,4,5,6 (y 0 en otro caso). ¿Cuál es la desviación estándar?",
      [f"σ ≈ {sd3:.2f}", "σ ≈ 1.17", "σ ≈ 1.25", "σ ≈ 1.08"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> σ = √Var = √(E(X²) − [E(X)]²).</div>'
      '<div class="formula-box">P(3)=3/50; P(4)=8/50; P(5)=15/50; P(6)=24/50 (suma=1 ✔)</div>'
      f'<div class="example-box">🟢 E(X) = {ex3:.2f}<br>E(X²) = {ex2_3:.2f}<br>Var = {ex2_3:.2f} − {ex3:.2f}² = {ex2_3 - ex3**2:.2f} → '
      f'σ = √({ex2_3 - ex3**2:.2f}) = <strong>{sd3:.2f}</strong></div>'),
    q("3", "q3_3ab",
      "(Binomial) Un arquero tiene p=0.80 de acertar; puede hacer a lo más 5 lanzamientos independientes. (a) ¿P(acierte a lo más en 3 lanzamientos)? (b) ¿P(acierte en por lo menos 2)?",
      [f"(a) {p3a:.3f}, (b) {p3b:.3f}",
       f"(a) {1-p3b:.3f}, (b) {p3b:.3f}",
       f"(a) {0.5:.3f}, (b) {p3b:.3f}",
       f"(a) {p3a+0.05:.3f}, (b) {p3b-0.05:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Binomial P(X=k)=C(n,k)·pᵏ·qⁿ⁻ᵏ con n=5, p=0.8, q=0.2.</div>'
      f'<div class="formula-box">P(X≤3) = Σ P(X=k) para k=0..3 = <strong>{p3a:.3f}</strong></div>'
      '<div class="example-box">🟢 O bien: P(X≤3) = 1 − P(X=4) − P(X=5) = 1 − 0.4096 − 0.3277 = '
      f'<strong>{p3a:.3f}</strong></div>'
      f'<div class="formula-box">P(X≥2) = 1 − P(X=0) − P(X=1) = 1 − 0.0003 − 0.0064 = <strong>{p3b:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> "A lo más 3" = P(X≤3); "por lo menos 2" = 1−P(X≤1).</div>'),
    q("4", "q3_4ab",
      "(Poisson) La probabilidad de que una persona tenga una enfermedad infecciosa es 0.01. De 1000 personas examinadas: (a) ¿P(a lo más 5 enfermas)? (b) ¿P(al menos 11 enfermas)?",
      [f"(a) {p4a:.3f}, (b) {p4b:.3f}",
       f"(a) {p4a:.3f}, (b) {0.5:.3f}",
       f"(a) {0.058:.3f}, (b) {0.632:.3f}",
       f"(a) {0.7286:.3f}, (b) {p4b:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> n grande y p pequeño → Poisson con λ = n·p = 1000×0.01 = <strong>10</strong>.</div>'
      '<div class="formula-box">P(X=k) = e^(−λ)·λᵏ/k!</div>'
      f'<div class="example-box">🟢 (a) P(X≤5) = P(0)+P(1)+...+P(5) = <strong>{p4a:.3f}</strong></div>'
      f'<div class="example-box">🟢 (b) P(X≥11) = 1 − P(X≤10) = 1 − {poisson_cdf(10,10):.3f} = <strong>{p4b:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> λ debe ajustarse al tamaño total (n·p), aquí λ=10.</div>'),
    q("5", "q3_5ab",
      "(Normal) El tiempo de un taxista es N(25, 5²) minutos. (a) ¿P(tarde a lo más 20 min)? (b) ¿P(tarde entre 22 y 30 min)?",
      [f"(a) {p5a:.3f}, (b) {p5b:.3f}",
       f"(a) {p5a:.3f}, (b) {p5b+0.02:.3f}",
       f"(a) {0.1587:.3f}, (b) {0.6403:.3f}",
       f"(a) {p5a-0.04:.3f}, (b) {p5b:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Tipificar z=(x−μ)/σ.</div>'
      f'<div class="formula-box">(a) z=(20−25)/5 = −1 → P(Z<−1) = <strong>{p5a:.3f}</strong></div>'
      f'<div class="example-box">🟢 (b) z₁=(22−25)/5=−0.6; z₂=(30−25)/5=1 → P = Φ(1)−Φ(−0.6) = '
      f'<strong>{p5b:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Restar Φ del límite menor: Φ(z₂)−Φ(z₁).</div>'),
])

# ---- Precalculo (Examen 4: Junio 2016 Vespertino - Proba 4/9) ----
lam4 = 1/4.5
pX2 = math.exp(-lam4*2)
pLess2 = 1 - pX2
p4b = sum(binom_pmf(8, pLess2, k) for k in range(4, 9))
pDc = 0.6*0.01 + 0.4*0.02
pM2D = (0.4*0.02)/pDc
E120 = 120*(1/3)
sg120 = math.sqrt(120*(1/3)*(2/3))
pQ4 = 1 - norm_cdf((29.5 - E120)/sg120)

# --- EXAMEN 4: JUNIO 2016 VESPERTINO ---
EX["exam4"] = ("EXAMEN JUNIO 2016 (Vespertino)", "Turno Vespertino / 16-Jun-2016", [
    q("1", "q4_1ab",
      "(Exponencial) La duración de llamadas sigue exponencial con media 4.5 min. (a) ¿Qué porcentaje supera los 2 min? (b) De 8 llamadas, ¿P(por lo menos la mitad duran < 2 min)?",
      [f"(a) {pX2:.0%}, (b) ≈ {p4b:.3f}",
       f"(a) {(pX2+0.05):.0%}, (b) ≈ {(p4b+0.05):.3f}",
       f"(a) {(pX2-0.08):.0%}, (b) ≈ {(1-p4b):.3f}",
       f"(a) {pX2:.0%}, (b) ≈ {(p4b-0.08):.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Exponencial: P(X>t)=e^(−λt) con λ=1/μ.</div>'
      f'<div class="formula-box">λ = 1/4.5 ≈ {lam4:.3f}<br>P(X>2) = e^(−2/4.5) = e^(−0.444) ≈ <strong>{pX2:.2f} ({(100*pX2):.0f}%)</strong></div>'
      f'<div class="example-box">🟢 (b) P(X<2) = 1−e^(−0.444) ≈ {pLess2:.3f}; Y~Bin(8, {pLess2:.3f}):</div>'
      f'<div class="formula-box">P(Y≥4) = <strong>{p4b:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> λ=1/μ (≈0.222), no 4.5. "Al menos la mitad de 8" = 4 o más.</div>'),
    q("2", "q4_2ab",
      "(V.A. Continua - constante k) f(x)=2kx si x<2; f(x)=1−2kx si 2≤x≤4; 0 en otro caso. (a) Halla k para que sea densidad. (b) Halla la varianza.",
      [f"(a) k = {0.125:.3f}, (b) Var = {0.667:.2f}", f"(a) k = {0.125:.3f}, (b) Var = {1.33:.2f}", f"(a) k = {0.25:.2f}, (b) Var = {0.667:.2f}", f"(a) k = {0.25:.2f}, (b) Var = {1.33:.2f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> ∫f = 1 sobre todo el dominio (densidad).</div>'
      '<div class="formula-box">∫₀² 2kx dx + ∫₂⁴ (1−2kx) dx = 1</div>'
      '<div class="example-box">🟢 [kx²]₀² = 4k ; [x−kx²]₂⁴ = 2−12k → total 2−8k = 1 → '
      '<strong>k = 1/8 = 0.125</strong></div>'
      '<div class="example-box">🟢 Con k=1/8: f(x)=x/4 (0≤x<2) y 1−x/4 (2≤x≤4):<br>'
      'E(X) = 0.667 + 2.667 − 1.333 = <strong>2</strong><br>E(X²) = 1 + 5.333 − 1.667 = 14/3<br>′'
      'Var = 14/3 − 2² = 14/3 − 12/3 = <strong>2/3 ≈ 0.67</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Asegurar que la función sea continua y sume 1 en TODO el intervalo.</div>'),
    q("3", "q4_3ab",
      "(Probabilidad Total y Bayes) La máquina M1 empaca el 60% (1% con falla de sellado) y M2 el 40% (2% con falla). (a) ¿P(una bolsa tenga problema de sellado)? (b) Si tuvo falla, ¿P(sea de M2)?",
      [f"(a) {pDc:.3f}, (b) {pM2D:.3f}",
       f"(a) {pDc:.3f}, (b) {(pM2D+0.05):.3f}",
       f"(a) {0.018:.3f}, (b) {pM2D:.3f}",
       f"(a) {pDc:.3f}, (b) {0.4:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Probabilidad total y Bayes con dos máquinas.</div>'
      f'<div class="formula-box">(a) P(F) = 0.6×0.01 + 0.4×0.02 = 0.006 + 0.008 = <strong>{pDc:.3f} (1.4%)</strong></div>'
      f'<div class="formula-box">(b) P(M2|F) = (0.4×0.02)/{pDc:.3f} = 0.008/0.014 ≈ <strong>{pM2D:.2f} ({100*pM2D:.0f}%)</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> El denominador es P(F) total (0.014), no 0.008.</div>'),
    q("4", "q4_4ab",
      "(Binomial - examen aleatorio) Un examen tiene 120 reactivos con 3 opciones cada uno. Al contestar al azar: (a) ¿Cuántas correctas se esperan? (b) ¿P(al menos la cuarta parte correctas)?",
      [f"(a) ≈ {E120:.0f}, (b) ≈ {pQ4:.3f}",
       f"(a) ≈ {E120:.0f}, (b) ≈ {0.017:.3f}",
       f"(a) ≈ {80:.0f}, (b) ≈ {pQ4:.3f}",
       f"(a) ≈ {E120:.0f}, (b) ≈ {0.998:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Binomial n=120, p=1/3. E(X)=n·p.</div>'
      f'<div class="formula-box">E(X) = 120 × 1/3 = <strong>{E120:.0f} correctas</strong></div>'
      '<div class="example-box">🟢 (b) La cuarta parte de 120 = 30. Con aproximación normal (np=40, '
      f'σ≈{sg120:.1f}) y corrección 0.5:</div>'
      f'<div class="formula-box">P(X≥30) ≈ 1 − Φ((29.5−40)/{sg120:.1f}) = 1 − Φ(−{((40-29.5)/sg120):.2f}) ≈ <strong>{pQ4:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> La cuarta parte de 120 es 30, no 40 (la esperanza).</div>'),
    q("5", "q4_5ab",
      "(Normal - tornillos) Los diámetros son N(3.0, 0.0025). Un tornillo es adecuado si su diámetro está en 3.0±0.10 mm. (a) ¿Qué % es desechado? (b) ¿P(el primer desechado antes del tercero que se inspeccione)?",
      [f"(a) {0.0456:.2%}, (b) {0.087:.3f}",
       f"(a) {0.0456:.2%}, (b) {0.912:.3f}",
       f"(a) {0.0038:.2%}, (b) {0.087:.3f}",
       f"(a) {0.9544:.2%}, (b) {0.087:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Normal: σ=√0.0025=0.05. Límites 3.0±0.10 → z=±2.</div>'
      '<div class="formula-box">P(desechado) = 2×P(Z<−2) = 2×0.0228 = <strong>0.0456 (4.56%)</strong></div>'
      '<div class="example-box">🟢 (b) Geométrica con p=0.0456: P(primer desechado en 1º o 2º intento) '
      '= p + (1−p)·p ≈ <strong>0.087</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> "Antes del tercero" = desechado en intento 1 o 2; usa σ=0.05, no la varianza.</div>'),
])

# ---- Precalculo (Examen 5: Primer Departamental 11/Sep/2017) ----
# Q2 eventos mut. excluyentes
pA = 1 - 0.6
pB = 1 - 0.7
pAUB = pA + pB
pAUBc = 1 - pAUB
# Q3 Don Gato bayes
probs_gato = [0.19, 0.35, 0.25, 0.21]
catches = [0.08, 0.075, 0.1, 0.05]
pCat = sum(probs_gato[i]*catches[i] for i in range(4))
pBenitoC = probs_gato[3]*catches[3]/pCat
pNoCat = 1 - pCat
# Q4 cartas sin reemplazo
pSegReina = 4/51
pAlMenosReina = 1 - (48/52)*(47/51)
# Q5 dados divisor de 12 y multiplo de 3 (sumas)
sumas = {i: 0 for i in range(2, 13)}
for d1 in range(1, 7):
    for d2 in range(1, 7):
        sumas[d1+d2] += 1
div12 = [2, 3, 4, 6, 12]
mult3 = [3, 6, 9, 12]
pDiv12 = sum(sumas[s] for s in div12)/36
pMult3 = sum(sumas[s] for s in mult3)/36

# --- EXAMEN 5: PRIMER DEPARTAMENTAL 2017 ---
EX["exam5"] = ("PRIMER DEPARTAMENTAL (2017)", "Turno Matutino / 11-Sep-2017", [
    q("1", "q5_1ab",
      "(Naipes) De una baraja de 52 cartas: A={espada}, B={figura (J,Q,K,As)}, C={Rey}. (a) ¿P(A∩B)? (b) ¿P(Bᶜ∩C)?",
      ["(a) 1/13, (b) 0", "(a) 3/52, (b) 1/13", "(a) 4/13, (b) 1/52", "(a) 1/4, (b) 4/52"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Hay 13 cartas por palo; 4 figuras por palo (J,Q,K,As).</div>'
      '<div class="example-box">🟢 (a) A∩B = espadas que son figura (J♠,Q♠,K♠,A♠) = 4 cartas → <strong>4/52 = 1/13</strong></div>'
      '<div class="example-box">🟢 (b) Bᶜ = no es figura; pero todo Rey (K) ES figura → Bᶜ∩C = ∅ → <strong>0</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> El As (A) también es figura en este contexto.</div>'),
    q("2", "q5_2ab",
      "(Eventos mutuamente excluyentes) A y B mutuamente excluyentes con P(Aᶜ)=0.6 y P(Bᶜ)=0.7. (a) ¿P(A∪B)? (b) ¿P(A∪B)ᶜ?",
      [f"(a) {pAUB:.2f}, (b) {pAUBc:.2f}", f"(a) {0.3:.2f}, (b) {0.7:.2f}", f"(a) {pAUB:.2f}, (b) {0.12:.2f}", f"(a) {0.42:.2f}, (b) {0.58:.2f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> A y B mutuamente excluyentes → P(A∪B)=P(A)+P(B).</div>'
      '<div class="formula-box">P(A) = 1−0.6 = 0.4 ; P(B) = 1−0.7 = 0.3</div>'
      f'<div class="example-box">🟢 (a) P(A∪B) = {pA:.1f} + {pB:.1f} = <strong>{pAUB:.1f}</strong></div>'
      f'<div class="example-box">🟢 (b) P(A∪B)ᶜ = 1 − {pAUB:.1f} = <strong>{pAUBc:.1f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Mutuamente excluyentes NO significa complementarios.</div>'),
    q("3", "q5_3ab",
      "(Bayes - Don Gato) Panzas 19% (atrapado 0.08), Demóstenes 35% (0.075), Cucho 25% (0.10), Benito 21% (0.05). (a) ¿P(ninguno sea atrapado)? (b) Si uno es atrapado, ¿P(sea Benito)?",
      [f"(a) {pNoCat:.3f}, (b) {pBenitoC:.3f}",
       f"(a) {pCat:.3f}, (b) {pBenitoC:.3f}",
       f"(a) {pNoCat:.3f}, (b) {0.377:.3f}",
       f"(a) {0.95:.3f}, (b) {pBenitoC:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Probabilidad total (atrapado) y Bayes (cuál gatito).</div>'
      f'<div class="formula-box">P(Atrapan) = 0.19×0.08 + 0.35×0.075 + 0.25×0.10 + 0.21×0.05 ≈ <strong>{pCat:.3f}</strong></div>'
      f'<div class="formula-box">(a) P(ninguno) = 1 − {pCat:.3f} = <strong>{pNoCat:.3f}</strong></div>'
      f'<div class="formula-box">(b) P(Benito|A) = (0.21×0.05)/({pCat:.3f}) ≈ <strong>{pBenitoC:.2f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> En (b) el denominador es P(atrapan) total.</div>'),
    q("4", "q5_4ab",
      "(Sin reemplazo - reinas) Se extraen 2 cartas sin reemplazo de una baraja. (a) ¿P(la 2ª sea reina si la 1ª no fue reina)? (b) ¿P(al menos una reina)?",
      [f"(a) {pSegReina:.3f}, (b) {pAlMenosReina:.3f}",
       f"(a) {pSegReina:.3f}, (b) {1-pAlMenosReina:.3f}",
       f"(a) {4/52:.3f}, (b) {pAlMenosReina:.3f}",
       f"(a) {3/51:.3f}, (b) {pAlMenosReina:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Extracción sin reemplazo reduce el espacio muestral.</div>'
      '<div class="example-box">🟢 (a) Si la 1ª NO fue reina: quedan 51 cartas, 4 reinas → <strong>4/51 ≈ 0.078</strong></div>'
      '<div class="example-box">🟢 (b) P(≥1 reina) = 1 − P(ninguna) = 1 − (48/52)×(47/51) ≈ '
      f'<strong>{pAlMenosReina:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> En (a) el denominador es 51, no 52 (ya se sacó una carta).</div>'),
    q("5", "q5_5ab",
      "(Dados - suma) Se lanzan 2 dados. X = suma de las caras. (a) ¿P(X sea divisor de 12)? (b) ¿P(X sea múltiplo de 3)?",
      [f"(a) {pDiv12:.3f}, (b) {pMult3:.3f}",
       f"(a) {pDiv12:.3f}, (b) {(pMult3+0.11):.3f}",
       f"(a) {0.5:.3f}, (b) {pMult3:.3f}",
       f"(a) {pDiv12:.3f}, (b) {0.167:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> 36 resultados equiprobables. Contar sumas favorables.</div>'
      '<div class="formula-box">Frecuencias: 2(1) 3(2) 4(3) 5(4) 6(5) 7(6) 8(5) 9(4) 10(3) 11(2) 12(1)</div>'
      f'<div class="example-box">🟢 (a) Divisores de 12: 2,3,4,6,12 → {1+2+3+5+1} casos → <strong>{pDiv12:.3f}</strong></div>'
      f'<div class="example-box">🟢 (b) Múltiplos de 3: 3,6,9,12 → {2+5+4+1} casos → <strong>{pMult3:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> El 1 no es suma posible; 12 solo con (6,6).</div>'),
])

# ---- Precalculo (Examen 6: Junio 2016 Vespertino - Proba 6) ----
# Q1 Normal camioneta mu=40, sigma=5, 75 entregas
z1_6 = (35-40)/5
pLess35 = norm_cdf(z1_6)
nEntregas = 75 * pLess35
# Q2 VAC [1,6]: k=0.25. Hallar varianza numericamente (integracion)
def f6(x):
    if x <= 4: return 0.25
    return -x/8 + 3*0.25
# integracion simple para E(X) y E(X^2)
N = 4000
h = 5.0/N
E1 = 0.0
E2 = 0.0
for i in range(N):
    x = 1 + h*(i+0.5)
    fv = f6(x)
    E1 += x*fv*h
    E2 += x*x*fv*h
var6 = E2 - E1*E1
# Q3 posgrados UPIICSA
pPos = [0.48, 0.07, 0.18, 0.27]
concl = [0.73, 0.85, 0.30, 0.50]
pNoConcl = sum(pPos[i]*(1-concl[i]) for i in range(4))
pConcl = 1 - pNoConcl
pAdmC = pPos[0]*concl[0]/pConcl
# Q4 exponencial colas: P(4<X<7) y P(entre 2 y 5 de 12 <1min)
lam6 = 1/6
pBetween = math.exp(-lam6*4) - math.exp(-lam6*7)
pLess1 = 1 - math.exp(-lam6*1)
p_2_5 = sum(binom_pmf(12, pLess1, k) for k in range(2, 6))
# Q5 binomial reparaciones p=0.1, n=220 approx Poisson(22); muestra 8
pRep = sum(poisson_pmf(22, k) for k in range(0, 16))
p2of8 = binom_pmf(8, 0.1, 2)

# --- EXAMEN 6: JUNIO 2016 VESPERTINO (Proba 6) ---
EX["exam6"] = ("EXAMEN JUNIO 2016 (Vespertino) 2", "Turno Vespertino / 16-Jun-2016", [
    q("1", "q6_1ab",
      "(Normal) La camioneta de reparto tarda N(40, 25) min. En 75 entregas (3 meses): (a) ¿En cuántas el tiempo fue < 35 min? (b) ¿Tiempo mínimo del 15% de recorridos más largos?",
      [f"(a) ≈ {nEntregas:.0f}, (b) ≈ {40 + 1.036*5:.1f} min",
       f"(a) ≈ {nEntregas+5:.0f}, (b) ≈ {40 + 1.036*5:.1f} min",
       f"(a) ≈ {nEntregas:.0f}, (b) ≈ 35 min",
       f"(a) ≈ {15:.0f}, (b) ≈ {40 + 1.036*5:.1f} min"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> z=(x−μ)/σ; P(X<35)=Φ(−1).</div>'
      '<div class="formula-box">σ=√25=5; z=(35−40)/5=−1 → Φ(−1) = '
      f'<strong>{pLess35:.3f}</strong></div>'
      f'<div class="example-box">🟢 (a) 75 × {pLess35:.3f} ≈ <strong>{nEntregas:.0f} entregas</strong></div>'
      '<div class="example-box">🟢 (b) Percentil 85: z≈1.036 → x = 40 + 1.036×5 = '
      f'<strong>{40 + 1.036*5:.1f} min</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Usar σ=5, no σ²=25, al tipificar.</div>'),
    q("2", "q6_2ab",
      "(V.A. Continua) f(x)=k si x≤4; f(x)=−x/8 + 3k si x>4, en [1,6]. (a) Halla k. (b) Halla la varianza.",
      [f"(a) k = 0.25, (b) Var ≈ {var6:.2f}",
       f"(a) k = 0.25, (b) Var ≈ 3.45",
       f"(a) k = 0.5, (b) Var ≈ {var6:.2f}",
       f"(a) k = 0.35, (b) Var ≈ {var6:.2f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> ∫₁⁶ f(x) dx = 1.</div>'
      '<div class="formula-box">∫₁⁴ k dx + ∫₄⁶ (−x/8+3k) dx = 3k + (−2.25+18k+1−12k) = 9k −1.25 = 1 → '
      '<strong>k = 0.25</strong></div>'
      f'<div class="example-box">🟢 f(x)=0.25 (1≤x≤4) y −x/8 + 0.75 (4<x≤6).<br>'
      f'Integrando: E(X) ≈ {E1:.2f} ; E(X²) ≈ {E2:.2f} → Var ≈ {var6:.2f}</div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Verificar que f(x) quede continua y positiva al elegir k.</div>'),
    q("3", "q6_3ab",
      "(Probabilidad Total y Bayes) Matrícula UPIICSA: Adm. 48% (concluye 73%), PYMES 7% (85%), Informática 18% (30%), Ing. Industrial 27% (50%). (a) ¿P(no concluya)? (b) Si concluyó, ¿P(sea Administración)?",
      [f"(a) {pNoConcl:.3f}, (b) {pAdmC:.3f}",
       f"(a) {pConcl:.3f}, (b) {pAdmC:.3f}",
       f"(a) {pNoConcl:.3f}, (b) {0.48:.3f}",
       f"(a) {pNoConcl:.3f}, (b) {0.73:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Probabilidad total (no concluir) y Bayes (qué maestría).</div>'
      '<div class="formula-box">P(No concluye) = 0.48×0.27 + 0.07×0.15 + 0.18×0.70 + 0.27×0.50 ≈ '
      f'<strong>{pNoConcl:.3f} ({100*pNoConcl:.0f}%)</strong></div>'
      f'<div class="formula-box">P(Concluye) = 1 − {pNoConcl:.3f} = {pConcl:.3f}</div>'
      f'<div class="formula-box">(b) P(Adm|Concl.) = (0.48×0.73)/({pConcl:.3f}) ≈ <strong>{pAdmC:.2f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> "No concluye" usa (1−concluye%) y el denominador en (b) es P(Concluye).</div>'),
    q("4", "q6_4ab",
      "(Exponencial) El tiempo en la fila de cajas es Exp(μ=6 min). (a) ¿P(tarde entre 4 y 7 min)? (b) De 12 clientes, ¿P(entre 2 y 5 sean atendidos en el 1er minuto)?",
      [f"(a) {pBetween:.3f}, (b) {p_2_5:.3f}",
       f"(a) {pBetween:.3f}, (b) {p_2_5+0.1:.3f}",
       f"(a) {pLess1:.3f}, (b) {p_2_5:.3f}",
       f"(a) {0.32:.3f}, (b) {p_2_5:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Exponencial: P(a<X<b)=e^(−λa)−e^(−λb), λ=1/6.</div>'
      f'<div class="formula-box">(a) P(4<X<7) = e^(−4/6) − e^(−7/6) = {math.exp(-lam6*4):.3f} − {math.exp(-lam6*7):.3f} = '
      f'<strong>{pBetween:.3f}</strong></div>'
      f'<div class="example-box">🟢 (b) P(<1 min) = 1−e^(−1/6) = {pLess1:.3f}<br>'
      f'Y~Bin(12, {pLess1:.3f}): P(2≤Y≤5) = <strong>{p_2_5:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Ajustar λ al orden correcto: e^(−λa)−e^(−λb) con a<b.</div>'),
    q("5", "q6_5ab",
      "(Binomial/Poisson) 1 de cada 10 equipos reparados vuelve a fallar. En 220 equipos: (a) ¿P(≤15 vuelvan a fallar)? (b) De 8 equipos, ¿P(2 deban reemplazarse)?",
      [f"(a) {pRep:.3f}, (b) {p2of8:.3f}",
       f"(a) {pRep:.3f}, (b) {binom_pmf(8, 0.1, 1):.3f}",
       f"(a) {pRep+0.05:.3f}, (b) {p2of8:.3f}",
       f"(a) {0.5:.3f}, (b) {p2of8:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> n grande, p pequeño → Poisson λ=n·p=22 para (a).</div>'
      '<div class="formula-box">(a) X~Bin(220, 0.1) ≈ Poisson(22): P(X≤15) = '
      f'<strong>{pRep:.3f}</strong></div>'
      '<div class="example-box">🟢 (b) Y~Bin(8, 0.1): P(Y=2) = C(8,2)×0.1²×0.9⁶ = '
      f'<strong>{p2of8:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Para (b) usar binomial directa (muestra pequeña), no Poisson.</div>'),
])

# ---- Precalculo (Examen 7: Enero 2003 - Proba 7) ----
# Q1 aeropuertos Bayes
pDet = 0.5*0.9 + 0.3*0.8 + 0.2*0.5
pAD = 0.5*0.9/pDet
# Q2 monedas disparejo (geometrica, p=0.75)
pDisp = 6/8
pMenos4 = pDisp + (1-pDisp)*pDisp + (1-pDisp)**2*pDisp
eIntentos = 1/pDisp
# Q3 pernos normales mu=10 sigma=0.01 (buenos 9.97 a 10.03)
pPernoDef = 2*(1 - norm_cdf(3))
xp3 = 10 - 1.8808*0.01
# Q4 TV exponencial mu=7
lam7 = 1/7
pTV7 = math.exp(-lam7*7)
pTV12 = math.exp(-lam7*12)
p1of10 = binom_pmf(10, pTV12, 1)
# Q5 examen binomial n=50 p=1/3 (aprox normal)
muB50 = 50/3
sgB50 = math.sqrt(50*(1/3)*(2/3))
pB50a = 1 - norm_cdf((25.5 - muB50)/sgB50)
pB50b = norm_cdf((19.5 - muB50)/sgB50)

# --- EXAMEN 7: ENERO 2003 ---
EX["exam7"] = ("EXAMEN ENERO 2003", "Enero 2003", [
    q("1", "q7_1ab",
      "(Probabilidad Total y Bayes) Aeropuerto A controla 50% del tráfico, B el 30% y C el 20%. Tasas de detección de armas: 0.9, 0.8 y 0.5. (a) ¿P(se detecte un arma)? (b) Si se detectó un arma, ¿P(que haya sido en A)?",
      [f"(a) {pDet:.3f}, (b) {pAD:.3f}",
       f"(a) {pDet:.3f}, (b) {0.5:.3f}",
       f"(a) {0.75:.3f}, (b) {pAD:.3f}",
       f"(a) {pDet:.3f}, (b) {0.9:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Probabilidad total y Bayes con 3 aeropuertos.</div>'
      '<div class="formula-box">(a) P(D) = 0.5×0.9 + 0.3×0.8 + 0.2×0.5 = 0.45 + 0.24 + 0.10 = '
      f'<strong>{pDet:.3f}</strong></div>'
      f'<div class="formula-box">(b) P(A|D) = (0.5×0.9)/({pDet:.2f}) = <strong>{pAD:.3f} ({100*pAD:.0f}%)</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> La tasa de detección NO es la probabilidad de que venga de A.</div>'),
    q("2", "q7_2ab",
      "(Geométrica - monedas) Tres personas lanzan una moneda; el disparejo paga. Si las 3 son iguales, se repite. (a) ¿P(se necesiten menos de 4 intentos)? (b) ¿En cuántos intentos se espera al perdedor?",
      [f"(a) {pMenos4:.3f}, (b) {eIntentos:.2f} intentos",
       f"(a) {pMenos4:.3f}, (b) {eIntentos+0.3:.2f}",
       f"(a) {1-pMenos4:.3f}, (b) {eIntentos:.2f}",
       f"(a) {0.75:.3f}, (b) {eIntentos:.2f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> P(disparejo)=6/8=0.75; el conteo de intentos es geométrico con p=0.75.</div>'
      '<div class="formula-box">P(3 iguales) = 2/8 = 0.25 → P(determinar) = 1−0.25 = <strong>0.75</strong></div>'
      '<div class="example-box">🟢 (a) P(X<4) = 0.75 + 0.25×0.75 + 0.25²×0.75 = '
      f'<strong>{pMenos4:.3f}</strong></div>'
      f'<div class="formula-box">(b) E(X) = 1/0.75 = <strong>{eIntentos:.2f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Geométrica cuenta SOLO los intentos; "menos de 4" = 1, 2 o 3.</div>'),
    q("3", "q7_3ab",
      "(Normal) Los pernos tienen diámetros N(10, 0.01²) mm. Son buenos si 9.97 ≤ d ≤ 10.03. (a) ¿% de pernos defectuosos? (b) Si solo el 3% de los más pequeños se rechaza, ¿cuál es el diámetro de selección?",
      [f"(a) {pPernoDef:.2%}, (b) {xp3:.3f} mm",
       f"(a) {pPernoDef:.2%}, (b) {10+1.8808*0.01:.3f} mm",
       f"(a) {0.001:.2%}, (b) {xp3:.3f} mm",
       f"(a) {pPernoDef:.2%}, (b) 9.970 mm"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> z=(x−μ)/σ; los límites 10±0.03 equivalen a z=±3.</div>'
      '<div class="formula-box">z = ±0.03/0.01 = ±3 → P(dentro) = Φ(3)−Φ(−3) = '
      f'<strong>{(norm_cdf(3)-norm_cdf(-3)):.4f}</strong></div>'
      f'<div class="example-box">🟢 (a) P(defectuoso) = 1 − 0.9973 = <strong>{pPernoDef:.2%} (0.27%)</strong></div>'
      f'<div class="example-box">🟢 (b) Percentil 3 → z=−1.881 → x = 10 − 1.881×0.01 = <strong>{xp3:.3f} mm</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Defectuoso = 2×0.0013 (ambas colas), no solo una.</div>'),
    q("4", "q7_4ab",
      "(Exponencial) La vida media de un televisor es 7 años (distribución exponencial). (a) ¿P(fallezca después del 7º año)? (b) De 10 televisores, ¿P(exactamente 1 dure más de 12 años)?",
      [f"(a) {pTV7:.3f}, (b) {p1of10:.3f}",
       f"(a) {pTV7:.3f}, (b) {1-p1of10:.3f}",
       f"(a) {1-pTV7:.3f}, (b) {p1of10:.3f}",
       f"(a) {pTV7:.3f}, (b) {pTV12:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Exponencial: P(X>t)=e^(−t/μ) con μ=7.</div>'
      f'<div class="formula-box">(a) P(X>7) = e^(−7/7) = e^(−1) = <strong>{pTV7:.3f}</strong></div>'
      f'<div class="example-box">🟢 P(X>12) = e^(−12/7) = {pTV12:.3f}<br>'
      f'(b) Y~Bin(10, {pTV12:.3f}): P(Y=1) = 10×{pTV12:.3f}×(0.8199)⁹ = <strong>{p1of10:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> En (b) es binomial: "exactamente 1", no "≥1".</div>'),
    q("5", "q7_5ab",
      "(Binomial - examen al azar) Examen de 50 preguntas, cada una con 3 opciones (1 correcta). Contesta al azar. (a) ¿P(acierte más de 25)? (b) ¿P(acierte menos de 20)?",
      [f"(a) ≈ {pB50a:.3f}, (b) ≈ {pB50b:.3f}",
       f"(a) ≈ {pB50a:.3f}, (b) ≈ {1-pB50b:.3f}",
       f"(a) ≈ {pB50a+0.05:.3f}, (b) ≈ {pB50b:.3f}",
       f"(a) ≈ {0.05:.3f}, (b) ≈ {pB50b:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> X~Bin(50, 1/3); aproximación normal con corrección ±0.5.</div>'
      f'<div class="formula-box">μ = np = 50/3 = {muB50:.1f} ; σ = √(50×1/3×2/3) = {sgB50:.1f}</div>'
      '<div class="example-box">🟢 (a) P(X>25) → z = (25.5 − 16.67)/3.33 = 2.65 → '
      f'<strong>{pB50a:.3f}</strong></div>'
      '<div class="example-box">🟢 (b) P(X<20) → z = (19.5 − 16.67)/3.33 = 0.85 → '
      f'<strong>{pB50b:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Aplicar ±0.5 de corrección de continuidad en ambos incisos.</div>'),
])

# ---- Precalculo (Examen 8: 19/Oct/2017 - Proba 8) ----
# Q1 binomial reprobacion 80% en 20
q1_8a = binom_pmf(20, 0.8, 8)
q1_8b = 1 - binom_cdf(20, 0.2, 5)       # mas de 5 no reprueban -> Y~Bin(20,0.2)
# Q2 Poisson estacionamiento: 10 lugares/30min -> lambda 5 en 15 min
lam5 = 5
q2_8a = 1 - poisson_cdf(lam5, 1)
q2_8b = poisson_pmf(lam5, 5)
# Q3 Hipergeometrica: 4R,3V,3B; extraer 3 sin reemplazo
q3_8a = comb(3,2)*comb(7,1)/comb(10,3)
q3_8b = 1 - comb(7,3)/comb(10,3)
# Q4 semaforo fiscal p=0.06, novena persona primera
q4_8a = (0.94**8)*0.06
q4_8b = 1/0.06
# Q5 VAD tabla: X=1,x2,5,7 ; p=1/4,1/3,P3,1/4 ; E=23/6
p3_8 = 1 - 1/4 - 1/3 - 1/4
x2_8 = (23/6 - 1*(1/4) - 5*(1/6) - 7*(1/4)) / (1/3)   # -> 3
E2_8 = 1*(1/4) + x2_8**2*(1/3) + 25*(1/6) + 49*(1/4)
var8 = E2_8 - (23/6)**2

# --- EXAMEN 8: SEGUNDO EXAMEN 2017 ---
EX["exam8"] = ("SEGUNDO EXAMEN (2017)", "Turno Vespertino / 19-Oct-2017", [
    q("1", "q8_1ab",
      "(Binomial - reprobación) El 80% de los alumnos reprueba Cálculo Diferencial. De 20 alumnos: (a) ¿P(reprueben exactamente 8)? (b) ¿P(más de 5 no reprueben)?",
      [f"(a) {q1_8a:.5f}, (b) {q1_8b:.3f}",
       f"(a) {q1_8a:.5f}, (b) {1-q1_8b:.3f}",
       f"(a) {q1_8b:.5f}, (b) {q1_8a:.3f}",
       f"(a) {0.5:.3f}, (b) {q1_8a:.5f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Binomial P(X=k)=C(n,k)·pᵏ·qⁿ⁻ᵏ.</div>'
      f'<div class="formula-box">(a) P(X=8) = C(20,8)×0.8⁸×0.2¹² = <strong>{q1_8a:.5f}</strong></div>'
      '<div class="example-box">🟢 (b) "No reprueban" → Y~Bin(20, 0.2): P(Y>5) = 1−P(Y≤5) = '
      f'<strong>{q1_8b:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> En (b) el evento es "no reprobar" → usa p=0.2 directamente.</div>'),
    q("2", "q8_2ab",
      "(Poisson) Se desocupan 10 lugares cada 30 min. En los próximos 15 min: (a) ¿P(por lo menos 2 lugares)? (b) ¿P(exactamente 5 lugares)?",
      [f"(a) {q2_8a:.3f}, (b) {q2_8b:.3f}",
       f"(a) {q2_8a:.3f}, (b) {q2_8b+0.1:.3f}",
       f"(a) {1-q2_8a:.3f}, (b) {q2_8b:.3f}",
       f"(a) {q2_8a:.3f}, (b) {0.067:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Ajustar λ al intervalo: 10/30 min = 5/15 min.</div>'
      '<div class="formula-box">λ = 5 por 15 min</div>'
      '<div class="example-box">🟢 (a) P(X≥2) = 1 − P(0) − P(1) = 1 − 6e⁻⁵ = '
      f'<strong>{q2_8a:.3f}</strong></div>'
      f'<div class="example-box">🟢 (b) P(X=5) = e⁻⁵·5⁵/5! = <strong>{q2_8b:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> λ cambia con el intervalo de tiempo (media proporcional).</div>'),
    q("3", "q8_3ab",
      "(Hipergeométrica - urnas) Hay 4 esferas rojas, 3 verdes y 3 blancas; se extraen 3 sin reemplazo. (a) ¿P(exactamente 2 verdes)? (b) ¿P(por lo menos una blanca)?",
      [f"(a) {q3_8a:.3f}, (b) {q3_8b:.3f}",
       f"(a) {q3_8a:.3f}, (b) {1-q3_8b:.3f}",
       f"(a) {comb(3,1)*comb(7,2)/comb(10,3):.3f}, (b) {q3_8b:.3f}",
       f"(a) {q3_8a:.3f}, (b) {0.5:.3f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Hipergeométrica sin reemplazo: P(k)=C(K,k)·C(N−K,n−k)/C(N,n).</div>'
      '<div class="formula-box">N=10 (4R+3V+3B), n=3.</div>'
      '<div class="example-box">🟢 (a) P(2 verdes) = C(3,2)·C(7,1)/C(10,3) = 3×7/120 = '
      f'<strong>{q3_8a:.3f}</strong></div>'
      '<div class="example-box">🟢 (b) P(≥1 blanca) = 1 − P(0 blancas) = 1 − C(7,3)/C(10,3) = '
      f'<strong>{q3_8b:.3f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> "Por lo menos una" se resuelve con complemento.</div>'),
    q("4", "q8_4ab",
      "(Geométrica - semáforo fiscal) Solo el 6% de las personas recibe inspección minuciosa. (a) ¿P(la 9ª persona de la fila sea la primera en accionar el semáforo)? (b) ¿Cuántas personas se esperan hasta la primera revisión?",
      [f"(a) {q4_8a:.3f}, (b) {q4_8b:.1f} personas",
       f"(a) {0.06:.3f}, (b) {16.7:.1f}",
       f"(a) {q4_8a:.3f}, (b) {0.94/0.06:.1f}",
       f"(a) {(0.94**9)*0.06:.3f}, (b) {q4_8b:.1f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Geométrica: P(X=k)=(1−p)ᵏ⁻¹·p; E(X)=1/p.</div>'
      '<div class="formula-box">p = 0.06 (inspección), q = 0.94</div>'
      f'<div class="example-box">🟢 (a) P(X=9) = 0.94⁸ × 0.06 = <strong>{q4_8a:.3f}</strong></div>'
      f'<div class="formula-box">(b) E(X) = 1/0.06 = <strong>{q4_8b:.1f} personas</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> La 9ª es la PRIMERA → 8 fallos antes: (1−p)⁸·p, no (1−p)⁹·p.</div>'),
    q("5", "q8_5ab",
      "(V.A.D.) Distribución: X={1, x₂, 5, 7} con p={1/4, 1/3, P₃, 1/4} y E(X)=23/6. (a) Halla x₂ y P₃. (b) Halla la varianza.",
      [f"(a) x₂={x2_8:.0f}, P₃=1/6, (b) Var ≈ {var8:.2f}",
       f"(a) x₂={x2_8:.0f}, P₃=1/6, (b) Var ≈ {0.972:.2f}",
       f"(a) x₂=3, P₃=1/3, (b) Var ≈ {var8:.2f}",
       f"(a) x₂=4, P₃=1/6, (b) Var ≈ {var8:.2f}"],
      '<div class="concept-box">🔵 <strong>Concepto:</strong> Σp=1 y Σx·p = E(X) para hallar incógnitas.</div>'
      '<div class="formula-box">1/4 + 1/3 + P₃ + 1/4 = 1 → '
      f'<strong>P₃ = 1/6</strong><br>E(X)=1/4 + x₂/3 + 5/6 + 7/4 = 23/6 → <strong>x₂ = {x2_8:.0f}</strong></div>'
      f'<div class="example-box">🟢 E(X²) = 1/4 + {x2_8:.0f}²/3 + 25/6 + 49/4 = {E2_8:.3f}<br>'
      f'Var = {E2_8:.3f} − (23/6)² = <strong>{var8:.2f}</strong></div>'
      '<div class="tip-box">⚠️ <strong>Trampa:</strong> Varianza con probabilidades que suman 1 y usando E(X²).</div>'),
])

# ===== GENERACIÓN DEL HTML =====
NAV_BLOCK = """
<div class="nav">
""" + "\n".join(f"<a href='#{eid}'>📝{i+1} {info[0].split('(')[0].strip()}</a>"
                for i, (eid, info) in enumerate(EX.items())) + """
</div>
"""

TREE_BLOCK = """
<h2>🌳 Árbol de Decisión: ¿Qué fórmula usar?</h2>
<div class="tree">
¿Cuál es la pregunta del problema?      -> Fórmula
├─ "¿de qué causa proviene lo observado?" -> BAYES: P(A|B)=P(A)·P(B|A)/ΣP(Aᵢ)P(B|Aᵢ)
├─ "¿n intentos fijos con éxito/fracaso?"  -> BINOMIAL: C(n,k)·pᵏ·qⁿ⁻ᵏ
├─ "¿hasta el PRIMER éxito?"               -> GEOMÉTRICA: (1-p)ᵏ⁻¹·p
├─ "¿éxitos en intervalo de tiempo/espacio,"-> POISSON: e⁻λ·λᵏ/k!
│   sucesos raros, λ media?"
├─ "¿sin reemplazo y población finita?"    -> HIPERGEOMÉTRICA: C(K,k)·C(N-K,n-k)/C(N,n)
├─ "¿tiempos de espera / vida útil (μ medio)"-> EXPONENCIAL: P(X>t)=e⁻ᵗ/μ
├─ "¿variable continua en campana (μ,σ)?"   -> NORMAL: z=(x−μ)/σ
└─ "¿se ordenan/escogen elementos?"         -> COMBINATORIA (permutaciones/combinaciones)
</p>
</div>

<h2>🧮 Tabla de Notación de Símbolos</h2>
<table class="symb">
<tr><th>Símbolo</th><th>Significado</th></tr>
<tr><td>P(A|B)</td><td>Probabilidad de A dado B</td></tr>
<tr><td>μ</td><td>Media poblacional / valor esperado</td></tr>
<tr><td>σ, σ²</td><td>Desviación estándar, varianza</td></tr>
<tr><td>λ</td><td>Tasa media (Poisson, Exponencial)</td></tr>
<tr><td>n, p, q</td><td>Nº ensayos, prob. éxito, prob. fracaso (q=1−p)</td></tr>
<tr><td>C(n,r)</td><td>Combinaciones de n tomando r</td></tr>
<tr><td>Φ(z)</td><td>Función de distribución normal estándar</td></tr>
<tr><td>E(X), Var(X)</td><td>Esperanza y varianza de una variable aleatoria</td></tr>
<tr><td>e</td><td>Base del logaritmo natural ≈ 2.71828</td></tr>
</table>
"""

FOOTER_BLOCK = """
<h2>📌 Fórmulas Maestras y Cheat Sheets</h2>
<h3>🔵 Conceptos Fundamentales</h3>
<div class="concept-box">
<p><strong>Prob. Condicional:</strong> P(A|B) = P(A∩B) / P(B)</p>
<p><strong>Bayes:</strong> P(A|B) = P(A)·P(B|A) / Σ P(Aᵢ)·P(B|Aᵢ)</p>
<p><strong>V.A.:</strong> E(X) = Σ x·p(x); Var(X) = E(X²) − [E(X)]²</p>
</div>
<h3>🟠 Fórmulas Esenciales</h3>
<div class="formula-box">
📊 Binomial: C(n,k)·pᵏ·qⁿ⁻ᵏ<br>
📈 Poisson: e⁻λ·λᵏ/k!<br>
🎯 Normal: z = (x−μ)/σ<br>
⏱️ Exponencial: P(X>t) = e⁻ᵗ/μ, λ=1/μ<br>
📐 Hipergeométrica: C(K,k)·C(N−K,n−k)/C(N,n)<br>
🎲 Geométrica: P(X=k)=(1−p)ᵏ⁻¹·p; E(X)=1/p
</div>
<h3>⚠️ Trampas Comunes en Exámenes</h3>
<div class="tip-box">
<p>1. <strong>Bayes:</strong> el denominador SIEMPRE es P(E) total.</p>
<p>2. <strong>Normal−Binomial:</strong> aplicar corrección ±0.5.</p>
<p>3. <strong>Exponencial:</strong> λ = 1/μ, no confundir con μ.</p>
<p>4. <strong>Poisson:</strong> ajustar λ al intervalo.</p>
<p>5. <strong>"Al menos"/"A lo más":</strong> usar complemento: P(X≥k)=1−P(X≤k−1).</p>
<p>6. <strong>Sin reemplazo:</strong> el denominador disminuye en 1.</p>
<p>7. <strong>Normal:</strong> tipificar con σ, nunca con σ².</p>
</div>
<h3>🧠 Repaso Activo (Active Recall)</h3>
<div class="example-box">
<p>1. Sin mirar el documento: escribir de memoria las 4 fórmulas del examen (Bayes, Binomial, Poisson, Normal).</p>
<p>2. Para cada inciso, preguntarse: ¿qué distribución reconozco por las palabras clave del enunciado?</p>
<p>3. Verificar siempre que las probabilidades sumen 1 antes de entregar.</p>
</div>
"""


def build_html():
    parts = [
        "<!DOCTYPE html>\n<html lang='es'>\n<head>\n",
        "<meta charset='UTF-8'>\n",
        "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n",
        "<title>Exámenes Interactivos de Probabilidad - ParetoTutor Visual</title>\n",
        CSS,
        "</head>\n<body>\n<div class='container'>\n",
        "<h1>🎓 Exámenes Interactivos de Probabilidad</h1>\n",
        "<p style='text-align:center; color:#94a3b8;'>Exámenes reales IPN - UPIICSA · Resoluciones explicadas paso a paso · Código de colores (🔵🔴🟢🟠)</p>\n",
        TREE_BLOCK,
        NAV_BLOCK,
    ]
    for eid in sorted(EX.keys()):
        title, subtitle, questions = EX[eid]
        parts.append(f"\n<h2 id='{eid}'>📝 {title}</h2>\n<p>{subtitle}</p>\n")
        for question in questions:
            parts.append(question)
    parts.append(FOOTER_BLOCK)
    parts.append("\n<div class='footer'><p>🎓 Generado por <strong>ParetoTutor Visual</strong> · Método con códigos de color para memoria visual</p></div>\n</div>\n")
    parts.append("<script>\nfunction toggleSolution(id){\nvar e=document.getElementById(id);\nif(e.style.display==='none'||e.style.display===''){e.style.display='block';}else{e.style.display='none';}\n}\n</script>\n")
    parts.append("</body>\n</html>\n")
    return "".join(parts)


def main():
    html = build_html()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Generado: {OUT}")
    print(f"📊 Caracteres: {len(html):,}")


if __name__ == "__main__":
    main()