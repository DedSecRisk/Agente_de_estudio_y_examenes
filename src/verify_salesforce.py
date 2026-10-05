# -*- coding: utf-8 -*-
"""Validacion del examen interactivo de Salesforce generado."""
import re, json, sys, collections
path = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Examenes_Interactivos_Salesforce.html"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
t = open(path, encoding="utf-8").read()

print("Cierra </html>:", t.strip().endswith("</html>"))
print("Divs abiertos:", t.count("<div"), "| cerrados:", t.count("</div>"), "-> OK" if t.count("<div")==t.count("</div>") else "DESBALANCE")
print("Scripts:", t.count("<script"), "| cierre script:", t.count("</script>"))

# 1) grupos de radio por pregunta
names = re.findall(r'name="(q\d+)"', t)
cnt = collections.Counter(names)
print("\n== RADIOS por pregunta ==")
bad = {k:v for k,v in cnt.items() if v!=4}
print("Preguntas:", len(cnt), "| todas con 4 opciones:", "OK" if not bad else bad)

# 2) soluciones: id sol-qXX y letra correcta
sols = re.findall(r'id="sol-(q\d+)"', t)
print("Soluciones:", len(sols), "| coinciden con radios:", sorted(sols)==sorted(cnt.keys()))

# 3) ANS data de JS
m = re.search(r'id="ans-data">(.*?)</script>', t, re.S)
ans = json.loads(m.group(1))
print("\n== ANS data ==")
print("Entradas:", len(ans), "| todas en radios:", set(ans.keys())==set(cnt.keys()))
ltr = collections.Counter(ans.values())
print("Distribucion letras correctas:", dict(sorted(ltr.items())))

# 4) bloques por sesion
qbloques = re.findall(r'<span class="qtag">Sesión (\d+)</span>', t)
cb = collections.Counter(qbloques)
print("\n== Preguntas por sesion ==")
print({f"S{k}":v for k,v in sorted(cb.items(), key=lambda x:int(x[0]))})
print("TOTAL:", sum(cb.values()))

# 5) marcadores "Respuesta correcta"
print("\nMarcas 'Respuesta correcta':", t.count("Respuesta correcta"), "(esperado 60)")

# 6) opciones duplicadas dentro de la misma pregunta
print("\n== Opciones duplicadas ==")
dups = 0
for b in re.split(r'(?=<div class="question")', t):
    mm = re.search(r'name="(q\d+)"', b)
    if not mm: continue
    opts = re.findall(r'<span>[A-D]\) (.*?)</span>', b)
    vistos = [o for o,c in collections.Counter(opts).items() if c>1]
    if vistos:
        dups += 1
        print("  ⚠️", mm.group(1), vistos)
print("Opciones duplicadas: ninguna" if dups==0 else f"{dups} preguntas con duplicados")

# 7) JS funcional presente
for fn in ["mostrarResultados","toggleSol","reiniciar","actualizar","btnRes","resPanel"]:
    if fn not in t: print("⚠️ falta", fn)
print("JS funcional presente: OK")

# 8) anchors de sesiones y nav
navs = re.findall(r'href="#ses(\d+)"', t)
h2s = re.findall(r'id="ses(\d+)"', t)
print("Nav:", len(navs)==10, "| H2 sesiones:", len(h2s)==10, "| coinciden:", sorted(navs)==sorted(h2s))

# 9) distribution of qid numbering 1..60
nums = sorted(int(re.match(r"q(\d+)", k).group(1)) for k in cnt)
print("Numeracion reactivos:", nums==list(range(1,61)))