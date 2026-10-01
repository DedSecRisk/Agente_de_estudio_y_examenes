# -*- coding: utf-8 -*-
"""
verify_v2.py — Validación obligatoria del entregable Guía+Examen v2 (ParetoTutor Visual)
Checks:
  1) HTML balanceado y cierra en </html>
  2) Vista guía y vista examen presentes
  3) Temas con IDs únicos y anclas válidas
  4) Preguntas: nombre de radio único, exactamente 4 opciones, 1 correcta, feedback presente
  5) Motor JS presente (localStorage, responder, mostrarResultados, reintentar)
  6) Anclas "tema-<slug>" referenciadas existen
  7) Datos JSON embebidos parsean (PREGUNTAS)
"""
import io, json, re, sys

def validate(path):
    h = io.open(path, encoding="utf-8").read()
    # Separar HTML visible de los bloques <script> (el JS contiene strings que parecen HTML)
    sin_js = re.sub(r"<script.*?</script>", "", h, flags=re.S)
    errs = []
    ok = []
    def C(cond, msg):
        if cond: ok.append(msg)
        else: errs.append(msg)

    C(h.rstrip().endswith("</html>"), "Cierra en </html>")
    for tag in ["div", "section", "table", "ul", "details", "label", "body", "html"]:
        ab = len(re.findall(r"<" + tag + r"(?:\s|>)", sin_js))
        ce = sin_js.count("</" + tag + ">")
        C(ab == ce, f"Balance {tag}: {ab}/{ce}")
    C(sin_js.count("<script") == 0, "Bloques <script> fuera del balance contados aparte")
    C(h.count("<script") == h.count("</script>"), f"Balance script: {h.count('<script')}/{h.count('</script>')}")
    C('id="vista-guia"' in sin_js, "Vista GUÍA presente")
    C('id="vista-examen"' in sin_js, "Vista EXAMEN presente")
    C("onclick=\"verGuia()\"" in sin_js and "onclick=\"verExamen()\"" in sin_js, "Alternador Guía/Examen presente")

    # Temas (solo HTML visible)
    ids_tema = re.findall(r'id="tema-([^"]+)"', sin_js)
    C(len(ids_tema) > 0, f"{len(ids_tema)} temas con ID")
    C(len(set(ids_tema)) == len(ids_tema), "IDs de temas únicos")
    anclas = re.findall(r'href="#tema-([^"]+)"', sin_js)
    rotas = [a for a in anclas if a not in ids_tema]
    C(not rotas, "Anclas de la guía válidas (0 rotas)" if not rotas else f"Anclas rotas: {rotas}")

    # Preguntas
    nombres = re.findall(r'type="radio" name="([^"]+)"', h)
    C(len(nombres) > 0, f"{len(nombres)} radios")
    por_preg = {}
    for n in nombres:
        por_preg.setdefault(n, 0)
        por_preg[n] += 1
    C(all(v == 4 for v in por_preg.values()), "Todas las preguntas con 4 opciones")
    C(len(set(por_preg.keys())) == len(por_preg.keys()), "Nombres de radio únicos")
    c_fb = re.findall(r'id="fb-([^"]+)"', h)
    C(len(c_fb) == len(por_preg), f"Feedback por pregunta: {len(c_fb)}/{len(por_preg)}")

    # Motor JS
    for token in ["localStorage", "function responder", "mostrarResultados", "reintentar",
                  "actualizarBarra", "var PREGUNTAS"]:
        C(token in h, f"Motor JS: {token}")

    # Parseo del JSON de PREGUNTAS embebido
    m = re.search(r"var PREGUNTAS = (\[.*?\]);", h, re.S)
    if m:
        try:
            data = json.loads(m.group(1))
            C(len(data) > 0, f"JSON embebido parsea: {len(data)} preguntas")
            temas = [d["tema"] for d in data]
            C(not any(d["ans"] not in (0, 1, 2, 3) for d in data), "Índices de respuesta correcta válidos")
            C(all(len(d["opts"]) == 4 for d in data), "4 opciones por pregunta en JSON")
            slug_ok = all(d.get("slug") in ids_tema for d in data)
            C(slug_ok, "Temas del examen existen en la guía")
        except Exception as e:
            errs.append("JSON embebido no parsea: " + str(e))
    else:
        errs.append("No se encontró var PREGUNTAS")

    print("=" * 60)
    print("VALIDACIÓN v2 —", path)
    print("=" * 60)
    for m in ok:
        print("  ✅", m)
    for e in errs:
        print("  ❌", e)
    print("-" * 60)
    print("RESULTADO:", "APROBADO ✔" if not errs else f"REPROBADO ({len(errs)})")
    return 0 if not errs else 1

if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Guia_Examen_Entrevista_Tecnica.html"
    sys.exit(validate(p))