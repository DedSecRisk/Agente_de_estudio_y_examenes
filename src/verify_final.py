# -*- coding: utf-8 -*-
"""Validacion cruzada: valores de la opcion A deben aparecer en la solucion."""
import re
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

path = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Examenes_Interactivos_Probabilidad.html"
with open(path, encoding="utf-8") as f:
    t = f.read()


def numeros(texto):
    """Extrae valores numericos: fracciones a/b, decimales y enteros."""
    def _div(m):
        den = float(m.group(2))
        return repr(int(m.group(1)) / den) if den else m.group()
    texto = re.sub(r"(\d+)\s*/\s*(\d+(?:\.\d+)?)", _div, texto)
    vals = []
    for m in re.finditer(r"-?\d+\.?\d*", texto):
        vals.append(float(m.group()))
    return vals


def cerca(v, lista):
    """True si v esta en lista con tolerancia de redondeo."""
    for w in lista:
        if abs(v - w) <= max(0.006, abs(w) * 0.01):
            return True
        # opcion en % vs solucion en fraccion (o viceversa)
        if abs(v * 100 - w) <= 0.6 or abs(v / 100 - w) <= 0.00006:
            return True
    return False


blocks = re.split(r'(?=<div class="question")', t)
fallos = 0
for b in blocks:
    m_id = re.search(r'name="(q[^"]+)"', b)
    if not m_id:
        continue
    qid = m_id.group(1)
    opt_a_m = re.search(r'<label class="option"><input type="radio" name="[^"]+"> A\) (.*?)</label>', b, re.S)
    sol_m = re.search(r"<div id='" + qid + r"' class='solution'>(.*?)</div>\s*</div>", b, re.S)
    if not opt_a_m or not sol_m:
        print(f"⚠️ {qid}: no se pudieron extraer partes")
        fallos += 1
        continue
    sol_txt = re.sub(r"<[^>]+>", " ", sol_m.group(1))
    nums_a = numeros(opt_a_m.group(1))
    nums_sol = numeros(sol_txt)
    faltan = [v for v in set(nums_a) if not cerca(v, nums_sol)]
    if faltan:
        fallos += 1
        print(f"⚠️ {qid}: valores de A no hallados en solucion -> {faltan}")
        print(f"   A = {opt_a_m.group(1)[:80]}")

if fallos == 0:
    print("✅ Todas las opciones A son coherentes con sus soluciones")
else:
    print(f"\nTotal con discrepancias: {fallos}")


path = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Examenes_Interactivos_Probabilidad.html"
with open(path, encoding="utf-8") as f:
    t = f.read()

parts = re.split(r"(<h2 id='exam\d'>[^<]+</h2>)", t)
total_q = 0
for i in range(1, len(parts) - 1, 2):
    header = parts[i]
    body = parts[i + 1]
    titulo = re.search(r">([^<]+)<", header).group(1)
    qids = re.findall(r'name="(q[^"]+)"', body)
    uniq = sorted(set(qids))
    n_opts = len(qids)
    n_q = len(re.findall(r'<div class="question">', body))
    total_q += n_q
    estado = "OK" if (n_q == len(uniq) and all(qids.count(u) == 4 for u in uniq)) else "REVISAR"
    print(f"{titulo}")
    print(f"   preguntas={n_q} | grupos_radio={len(uniq)} | radios={n_opts} -> {estado}")
    for u in uniq:
        c = qids.count(u)
        if c != 4:
            print(f"      ⚠️ {u}: {c} opciones")
print(f"\nTOTAL preguntas: {total_q}")

# IDs de solucion vs ids de radio
sol_ids = set(re.findall(r"<div id='(q[^']+)' class='solution'>", t))
rad_ids = set(re.findall(r'name="(q[^"]+)"', t))
print("Solucion sin radio:", sol_ids - rad_ids or "ninguno")
print("Radio sin solucion:", rad_ids - sol_ids or "ninguno")

# Marcador de respuesta correcta en soluciones
n_ans = len(re.findall(r"Respuesta correcta", t))
print(f"Marcas 'Respuesta correcta': {n_ans} (esperadas {total_q}) -> {'OK' if n_ans == total_q else 'REVISAR'}")

# Opciones identicas dentro de la misma pregunta
print("=" * 50)
blocks = re.split(r'(?=<div class="question")', t)
hay_dup = False
for b in blocks:
    m = re.search(r'name="(q[^"]+)"', b)
    if not m:
        continue
    opts = re.findall(r'<label class="option"><input type="radio" name="[^"]+"> [A-E]\) (.*?)</label>', b)
    vistos = {}
    for o in opts:
        vistos[o] = vistos.get(o, 0) + 1
    reps = {k: v for k, v in vistos.items() if v > 1}
    if reps:
        hay_dup = True
        print(f"⚠️ {m.group(1)}: opciones repetidas -> {reps}")
if not hay_dup:
    print("Opciones duplicadas: ninguna")

# Cierre del documento
print("Cierra </html>:", t.strip().endswith("</html>"))

# JavaScript interactivo y navegacion
print("=" * 50)
print("function toggleSolution definida:", "function toggleSolution" in t)
nav = re.findall(r"href=[\"']#(exam\d)[\"']", t)
h2 = re.findall(r"<h2 id=['\"](exam\d)['\"]", t)
print(f"Enlaces nav: {len(set(nav))} | h2: {len(h2)} | coinciden:", sorted(set(nav)) == sorted(h2))
print("divs abiertos:", t.count("<div"), "| cerrados:", t.count("</div>"),
      "->", "OK" if t.count("<div") == t.count("</div>") else "⚠️ desbalance")
print("script cerrado:", "</script>" in t)


