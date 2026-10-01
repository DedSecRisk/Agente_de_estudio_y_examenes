#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador maestro: Examen Interactivo de Salesforce FSC & Slack - ParetoTutor Visual.
60 reactivos de nivel dificil (opcion multiple A-D) con escenarios reales y
relacion de conceptos, basados en la presentacion '1er_MCB (1).pdf'.
Al completar los 60 reactivos aparece 'Mostrar resultados': en las preguntas
malas se resalta la opcion correcta y se muestra la justificacion codificada
por colores (azul concepto, rojo trampa, verde ejemplo, naranja regla de oro).
"""
import os

OUT = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Examenes_Interactivos_Salesforce.html"

SES = [
    (1, "Sesión 1 — Introducción al Ecosistema Salesforce"),
    (2, "Sesión 2 — FSC: Fundamentos y Modelo de Datos"),
    (3, "Sesión 3 — Insurance Cloud: Pólizas y Beneficios"),
    (4, "Sesión 4 — Procesos Comerciales: Cotización y Pipeline"),
    (5, "Sesión 5 — Gestión de Siniestros (Claims)"),
    (6, "Sesión 6 — Service Cloud: Casos, Colas y SLAs"),
    (7, "Sesión 7 — Omnichannel: Canales de Atención"),
    (8, "Sesión 8 — Service Cloud Voice"),
    (9, "Sesión 9 — Reportes y Dashboards"),
    (10, "Sesión 10 — Slack + Cierre Integrador"),
]

CSS = """<style>
body{font-family:'Segoe UI',Arial,sans-serif;background:#0F172A;color:#e2e8f0;line-height:1.6;margin:0;padding:0 14px 90px}
.container{max-width:1000px;margin:0 auto;padding:14px}
h1{color:#bae6fd;text-align:center;border-bottom:3px solid #38bdf8;padding-bottom:12px}
h2{color:#38bdf8;border-left:5px solid #38bdf8;padding-left:10px;margin-top:46px}
h3{color:#fef3c7}
.nav{position:sticky;top:0;background:rgba(15,23,42,.96);padding:10px;border-radius:8px;margin:18px 0;text-align:center;z-index:40;border:1px solid #334155}
.nav a{color:#38bdf8;text-decoration:none;margin:2px 6px;font-weight:600;font-size:.9em}
.nav a:hover{color:#bae6fd;text-decoration:underline}
.question{background:rgba(255,255,255,.04);border:1px solid #334155;border-left:4px solid #38bdf8;padding:14px 16px;margin-bottom:18px;border-radius:6px}
.question.ok{border-left-color:#22c55e;border-color:#22c55e}
.question.bad{border-left-color:#ef4444;border-color:#ef4444}
.qnum{display:inline-block;background:#38bdf8;color:#0f1729;font-weight:700;border-radius:4px;padding:1px 9px;margin-right:8px}
.qtag{display:inline-block;background:rgba(245,158,11,.15);color:#fef3c7;border:1px solid #f59e0b;border-radius:4px;padding:1px 8px;font-size:.75em}
.qtext{margin:10px 0 12px}
.options{display:flex;flex-direction:column;gap:8px;margin:0 0 12px}
.option{display:flex;align-items:flex-start;gap:10px;background:rgba(56,189,248,.07);border:2px solid #38bdf8;color:#bae6fd;padding:9px 12px;border-radius:6px;cursor:pointer;transition:.15s}
.option:hover{background:rgba(56,189,248,.18);border-color:#7dd3fc}
.option input{margin-top:3px;flex:none}
.option.opt-correct{background:rgba(34,197,94,.16);border-color:#22c55e;color:#bbf7d0}
.option.opt-wrong{background:rgba(248,113,113,.16);border-color:#ef4444;color:#fecaca}
.btn-sol{background:#f59e0b;color:#0f1729;border:none;padding:6px 14px;border-radius:6px;cursor:pointer;font-weight:700}
.btn-sol:hover{background:#fbbf24}
.sol-box{display:none;margin-top:12px;padding:12px;background:rgba(30,41,59,.6);border:2px dashed #475569;border-radius:8px}
.concept-box{background:rgba(56,189,248,.1);border:2px solid #38bdf8;color:#bae6fd;padding:9px 12px;border-radius:6px;margin:8px 0;font-size:.95em}
.tip-box{background:rgba(248,113,113,.1);border:2px solid #ef4444;color:#fecaca;padding:9px 12px;border-radius:6px;margin:8px 0;font-size:.95em}
.example-box{background:rgba(34,197,94,.1);border:2px solid #22c55e;color:#bbf7d0;padding:9px 12px;border-radius:6px;margin:8px 0;font-size:.95em}
.formula-box{background:rgba(245,158,11,.1);border:2px solid #f59e0b;color:#fef3c7;padding:9px 12px;border-radius:6px;margin:8px 0;font-size:.95em}
.tree{background:rgba(30,41,59,.9);border:2px dashed #475569;color:#cbd5e1;padding:12px;border-radius:8px;font-family:Consolas,monospace;white-space:pre;overflow-x:auto;margin:10px 0;line-height:1.5}
table.symb{border-collapse:collapse;margin:10px 0;width:100%}
table.symb th,table.symb td{border:1px solid #475569;padding:6px 10px;text-align:left}
table.symb th{background:rgba(100,116,139,.2);color:#e0e0ff}
.resultbar{position:fixed;bottom:0;left:0;right:0;background:rgba(15,23,42,.98);border-top:2px solid #38bdf8;padding:10px 18px;display:flex;justify-content:center;gap:16px;align-items:center;z-index:60;flex-wrap:wrap}
.bar-wrap{width:200px;height:12px;background:#1e293b;border-radius:6px;overflow:hidden}
#progbar{height:100%;width:0;background:linear-gradient(90deg,#38bdf8,#22c55e);transition:width .3s}
#btnRes{display:none;background:#22c55e;color:#0f1729;font-weight:800;border:2px solid #4ade80;padding:10px 24px;border-radius:8px;cursor:pointer;font-size:1.05em;animation:pulse 1s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(74,222,128,.45)}70%{box-shadow:0 0 0 12px rgba(74,222,128,0)}100%{box-shadow:0 0 0 0 rgba(74,222,128,0)}}
.score-panel{display:none;background:rgba(30,41,59,.85);border:2px solid #38bdf8;border-radius:10px;padding:20px;margin:30px 0;text-align:center}
.score-panel .big{font-size:2.4em;font-weight:800;color:#bae6fd}
.score-panel .pct{font-size:1.4em;color:#4ade80;font-weight:700}
#resLista a{color:#fecaca;font-weight:700;margin:0 3px}
.footer{text-align:center;margin-top:40px;padding:12px;color:#64748b;font-size:.9em}
</style>"""

TREE = """<h2>🌳 Árbol de Decisión: ¿Qué herramienta usar según el caso?</h2>
<div class="tree">
Situación en el Broker                          -> Solución
├─ "¿Unificar canales y asignar al agente libre?"  -> OMNICHANNEL (Work Items + Presence + Capacity)
├─ "¿Registrar toda solicitud/consulta con SLA?"    -> CASE (Service Cloud) + COLAS
├─ "¿Gestionar el expediente del siniestro?"        -> CLAIM (Insurance Cloud)
├─ "¿Llamadas integradas al CRM con contexto?"      -> SERVICE CLOUD VOICE (Screen Pop, ACW, Wrap-Up)
├─ "¿Lista exacta de registros para trabajar?"      -> REPORTE (exportable a Excel/CSV/PDF)
├─ "¿Ver el negocio de un vistazo?"                 -> DASHBOARD (gráficas, contadores, semáforos)
├─ "¿Automatizar tareas al cambiar un registro?"    -> FLOW BUILDER (Record-Triggered)
├─ "¿Persona física / empresa / familia en FSC?"    -> ACCOUNT Person | Business | HOUSEHOLD
├─ "¿Modificar una póliza vigente?"                 -> ENDORSEMENT (endoso)
├─ "¿Coordinar y decidir en equipo?"                -> SLACK (canales, hilos, Huddle)
└─ "¿Colaborar con la aseguradora (externa)?"       -> SLACK CONNECT
</div>"""

NOTATION = """<h2>📋 Tabla de Notación — Objetos y Términos Salesforce</h2>
<table class="symb">
<tr><th>Término</th><th>Significado en el negocio</th></tr>
<tr><td>Account (Business/Person)</td><td>Empresa contratante / persona física asegurada</td></tr>
<tr><td>Household</td><td>Agrupa miembros de familia o colectivo (rollup AUM, net worth)</td></tr>
<tr><td>Insurance Policy</td><td>Póliza (objeto central de Insurance Cloud, id POL-xxxx)</td></tr>
<tr><td>Coverage / Participant</td><td>Cobertura específica / asegurado incluido en la póliza</td></tr>
<tr><td>Carrier / Producer</td><td>Aseguradora que suscribe / agente responsable del Broker</td></tr>
<tr><td>Endorsement / Renewal</td><td>Endoso (modificación vigente) / proceso de renovación</td></tr>
<tr><td>Claim</td><td>Siniestro (Reportado → En Proceso → En Revisión → Resuelto → Cerrado)</td></tr>
<tr><td>Case</td><td>Solicitud/consulta con SLA (Nuevo → … → Pendiente Cliente → … → Cerrado)</td></tr>
<tr><td>Opportunity / Stage</td><td>Cotización/venta activa / etapa del pipeline</td></tr>
<tr><td>Work Item</td><td>Unidad de trabajo de Omnichannel (chat, WhatsApp, email, voz)</td></tr>
<tr><td>Presence / Capacity</td><td>Estado del agente / máx. Work Items simultáneos</td></tr>
<tr><td>Screen Pop / ACW / Wrap-Up</td><td>Ficha al contestar / trabajo post-llamada / código de cierre</td></tr>
<tr><td>SLA / Queue</td><td>Tiempo comprometido / cola de casos por área</td></tr>
<tr><td>Flow / Workflow Builder</td><td>Automatización en Salesforce / automatización en Slack</td></tr>
</table>"""

NAV = """<div class="nav">
<a href="#ses1">S1</a><a href="#ses2">S2</a><a href="#ses3">S3</a><a href="#ses4">S4</a><a href="#ses5">S5</a><a href="#ses6">S6</a><a href="#ses7">S7</a><a href="#ses8">S8</a><a href="#ses9">S9</a><a href="#ses10">S10</a>
</div>"""

FOOTER = """<h2>📌 Reglas de Oro y Trampas Comunes del Temario</h2>
<h3>🟠 Reglas de Oro</h3>
<div class="formula-box">
• Lo que se decide en Slack, se registra en Salesforce (Slack = conversación · SF = fuente de verdad)<br>
• Nadie asigna manualmente: el sistema resuelve quién atiende (Colas y Omnichannel)<br>
• Cada llamada = un Case con historial + grabación + resumen Einstein<br>
• El Broker administra, NO suscribe ni liquida siniestros<br>
• Lo que no está en el Action Plan puede olvidarse; lo que está, se hace y queda registrado
</div>
<h3>⚠️ Trampas Comunes en Examen</h3>
<div class="tip-box">
1. El SLA de respuesta al asegurado aplica al CASE, no al Claim.<br>
2. Account(Business) es para empresas; las personas se registran con Account(Person).<br>
3. El endoso modifica la póliza vigente; no se crea una póliza nueva.<br>
4. El Claim se abre DESPUÉS del Case (FNOL); no al revés.<br>
5. Dashboard no exporta registros individuales; el Reporte sí.<br>
6. Flow Builder = Salesforce; Workflow Builder = Slack.<br>
7. Atención usa Service+Omni+Voice; Siniestros usa Insurance+Service+Voice.
</div>
<h3>🧠 Repaso Activo (Active Recall)</h3>
<div class="example-box">
1. Sin mirar: dibuja el flujo end-to-end de un siniestro (6 pasos) con su objeto Salesforce en cada paso.<br>
2. Explica con tus palabras la diferencia entre Case y Claim; y entre Reporte y Dashboard.<br>
3. Antes de dormir: repite de memoria las 7 reglas de oro y las 7 trampas comunes.
</div>"""

SCORE_PANEL = """<div class="score-panel" id="resPanel">
<p class="big" id="resNum">0 / 0</p>
<p class="pct" id="resPct">0%</p>
<p id="resMsg" style="font-size:1.15em"></p>
<p id="resLista"></p>
<button class="btn-sol" onclick="reiniciar()">🔄 Reintentar examen</button>
</div>"""

ANSWER_DATA = """<script type="application/json" id="ans-data">%s</script>"""

JS = """<script>
var ANS = JSON.parse(document.getElementById('ans-data').textContent);
function totalQ(){return Object.keys(ANS).length;}
function actualizar(){
  var names={};
  var radios=document.querySelectorAll('input[type=radio]:checked');
  for(var i=0;i<radios.length;i++){names[radios[i].name]=1;}
  var n=Object.keys(names).length;
  document.getElementById('prog').textContent=n;
  document.getElementById('progbar').style.width=Math.round(n/totalQ()*100)+'%';
  document.getElementById('btnRes').style.display=(n>=totalQ())?'inline-block':'none';
}
document.querySelectorAll('input[type=radio]').forEach(function(r){r.addEventListener('change',actualizar);});
function mostrarResultados(){
  var aci=0,err=[],total=totalQ();
  Object.keys(ANS).forEach(function(qid){
    var sel=document.querySelector('input[name="'+qid+'"]:checked');
    var cont=document.getElementById('cont-'+qid);
    if(!sel)return;
    if(sel.value===ANS[qid]){
      aci++;
      sel.closest('.option').classList.add('opt-correct');
      cont.classList.add('ok');
    }else{
      sel.closest('.option').classList.add('opt-wrong');
      var radios=document.querySelectorAll('input[name="'+qid+'"]');
      for(var i=0;i<radios.length;i++){if(radios[i].value===ANS[qid]){radios[i].closest('.option').classList.add('opt-correct');}}
      document.getElementById('sol-'+qid).style.display='block';
      cont.classList.add('bad');
      err.push(qid);
    }
  });
  var pct=Math.round(aci/total*100);
  var msg = pct===100?'🏆 ¡Perfecto! Dominas todo el temario.'
           : pct>=90?'🥇 Nivel experto: listo para el examen.'
           : pct>=75?'✅ Buen nivel: refuerza tus fallos.'
           : pct>=60?'⚠️ Revisa las secciones donde fallaste.'
           : '📚 Te conviene repasar el temario y reintentar.';
  var lista=err.map(function(q){return '<a href="#'+q+'">'+q.replace('q','')+'</a>';}).join(' ');
  document.getElementById('resPanel').style.display='block';
  document.getElementById('resNum').textContent=aci+' / '+total;
  document.getElementById('resPct').textContent=pct+'%';
  document.getElementById('resMsg').textContent=msg;
  document.getElementById('resLista').innerHTML=err.length?'🔴 Reactivos incorrectos (opción correcta resaltada y justificada): '+lista:'🎯 Todos correctos';
  document.getElementById('resPanel').scrollIntoView({behavior:'smooth'});
}
function toggleSol(qid){
  var e=document.getElementById('sol-'+qid);
  e.style.display=(e.style.display==='block')?'none':'block';
}
function reiniciar(){
  document.querySelectorAll('input[type=radio]').forEach(function(r){r.checked=false;});
  document.querySelectorAll('.opt-correct,.opt-wrong').forEach(function(e){e.classList.remove('opt-correct','opt-wrong');});
  document.querySelectorAll('.question.ok,.question.bad').forEach(function(e){e.classList.remove('ok','bad');});
  document.querySelectorAll('.sol-box').forEach(function(e){e.style.display='none';});
  document.getElementById('resPanel').style.display='none';
  actualizar();window.scrollTo(0,0);
}
</script>"""

def render_q(q):
    """Renderiza un reactivo. Rota opciones segun el numero para variar la letra correcta."""
    k = q['num'] % 4
    opts = list(q['opt'])
    ans = q['ans']
    if k:
        opts = opts[k:] + opts[:k]
        ans = (ans - k) % 4
    letter = 'ABCD'[ans]
    L = [f'<div class="question" id="cont-{q["qid"]}">',
         f'<p><span class="qnum">{q["num"]}</span><span class="qtag">Sesión {q["s"]}</span></p>',
         f'<p class="qtext">{q["txt"]}</p>',
         '<div class="options">']
    for i, o in enumerate(opts):
        L.append(f'<label class="option"><input type="radio" name="{q["qid"]}" value="{chr(65+i)}"> <span>{chr(65+i)}) {o}</span></label>')
    L.append('</div>')
    L.append(f'<button class="btn-sol" onclick="toggleSol(\'{q["qid"]}\')">🔍 Ver solución</button>')
    L.append(f'<div class="sol-box" id="sol-{q["qid"]}">')
    L.append(f'<div class="example-box">✅ <strong>Respuesta correcta: {letter})</strong></div>')
    L.append(q['just'])
    L.append('</div></div>')
    return '\n'.join(L)


def build_html():
    ans_map = {}
    for q in QUESTIONS:
        k = q['num'] % 4
        ans = (q['ans'] - k) % 4
        ans_map[q['qid']] = 'ABCD'[ans]
    parts = ["<!DOCTYPE html>\n<html lang='es'>\n<head>\n<meta charset='UTF-8'>\n",
             "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n",
             "<title>Examen Interactivo Salesforce FSC &amp; Slack — 60 reactivos (Nivel Difícil)</title>\n",
             CSS, "</head>\n<body>\n<div class='container'>\n",
             "<h1>🎓 Examen Interactivo — Salesforce FSC &amp; Slack</h1>\n",
             "<p style='text-align:center;color:#94a3b8;'>Broker de Seguros y Beneficios Empresariales · 60 reactivos de nivel difícil (opción múltiple) · Escenarios reales y relación de conceptos · Método visual 🔵🔴🟢🟠</p>\n",
             "<p style='text-align:center;color:#94a3b8;'>Responde los 60 reactivos y al finalizar aparecerá el botón <strong style='color:#4ade80'>✓ Mostrar resultados</strong>; en tus errores verás la opción correcta resaltada y justificada.</p>",
             TREE, NOTATION, NAV]
    for sid, title in SES:
        parts.append(f'<h2 id="ses{sid}">📘 {title}</h2>\n')
        for q in QUESTIONS:
            if q['s'] == sid:
                parts.append(render_q(q))
    parts.append(FOOTER)
    parts.append(SCORE_PANEL)
    parts.append('<div class="resultbar">')
    parts.append('<span>Reactivos respondidos: <strong id="prog" style="color:#4ade80">0</strong>/60</span>')
    parts.append('<div class="bar-wrap"><div id="progbar"></div></div>')
    parts.append('<button id="btnRes" onclick="mostrarResultados()">✓ Mostrar resultados</button>')
    parts.append('</div>')
    parts.append(ANSWER_DATA % ("{" + ",".join(f'"{qid}":"{letter}"' for qid, letter in ans_map.items()) + "}"))
    parts.append(JS)
    parts.append("<div class='footer'><p>🎓 Generado por <strong>ParetoTutor Visual</strong> · Basado en la presentación del programa de capacitación Salesforce FSC &amp; Slack (MC Brokers)</p></div>")
    parts.append("</div>\n</body>\n</html>\n")
    return '\n'.join(parts)


QUESTIONS = []

QUESTIONS.append(dict(
    num=1, s=1, qid='q01',
    txt="En el diagnóstico inicial de MC Brokers se detectaron: solicitudes funcionales sin análisis previo suficiente, uso parcial de las funcionalidades estándar y alta dependencia del equipo técnico. ¿Cuál es el impacto más grave que busca contener el programa de capacitación?",
    opt=[
        "La sobreconfiguración innecesaria que incrementa la deuda técnica y el retrabajo funcional",
        "La baja del SLA de la mesa de servicio del call center",
        "La pérdida de grabaciones de llamadas por falta de almacenamiento",
        "El aumento del costo de las licencias de las nubes contratadas"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Concepto:</strong> El diagnóstico documenta "riesgo de sobreconfiguración innecesaria" derivado de customizar por falta de conocimiento.</div>'
         '<div class="example-box">🟢 <strong>Impacto actual:</strong> retrabajo funcional, ineficiencias operativas e incremento en deuda técnica.</div>'
         '<div class="tip-box">⚠️ <strong>Trampa:</strong> Las otras opciones mezclan síntomas operativos (SLA, grabaciones, licencias) que no derivan del dolor detectado.</div>'))

QUESTIONS.append(dict(
    num=2, s=1, qid='q02',
    txt="De acuerdo con el mapa del ecosistema, el área de Siniestros del Broker combina tres nubes en su operación diaria. ¿Cuáles son?",
    opt=[
        "Insurance Cloud + Service Cloud + Voice",
        "FSC + Insurance Cloud + Slack",
        "Service Cloud + Omnichannel + Voice",
        "FSC + Reportes + Campañas"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Quién usa qué:</strong> Siniestros = Insurance + Service + Voice.</div>'
         '<div class="example-box">🟢 El asegurado reporta el siniestro (Service), se gestiona el Claim (Insurance) y se coordina por llamadas integradas (Voice).</div>'
         '<div class="tip-box">⚠️ <strong>Trampa:</strong> Atención = Service+Omni+Voice; Comercial = FSC+Insurance+Slack; Cobranza = FSC+Reportes.</div>'))

QUESTIONS.append(dict(
    num=3, s=1, qid='q03',
    txt="¿Qué elemento distingue a Financial Services Cloud (FSC) de la plataforma Salesforce estándar para el caso de un Broker de seguros?",
    opt=[
        "Un modelo de datos especializado, consolas preconfiguradas por rol y funcionalidades regulatorias",
        "Un sistema contable que reemplaza al ERP de la aseguradora",
        "Una red privada que aísla la información del sector financiero",
        "Un módulo de facturación electrónica exclusivo de México"],
    ans=0,
    just='<div class="concept-box">🔵 FSC extiende Salesforce con modelo de datos especializado, consolas (Banker, Advisor, Insurance Producer) y funcionalidades regulatorias.</div>'
         '<div class="tip-box">⚠️ <strong>Trampa:</strong> FSC no sustituye un ERP ni factura: vive SOBRE la plataforma Salesforce y se integra con ella.</div>'))

QUESTIONS.append(dict(
    num=4, s=1, qid='q04',
    txt="Un cliente corporativo comunica que su empresa tendrá una expansión (abrirá operaciones en otra ciudad). ¿Qué pilar de FSC registra este hito y dispara oportunidades comerciales proactivas?",
    opt=[
        "Life Events & Business Milestones",
        "Referral Management",
        "Households & Relaciones",
        "Perfil Financiero del Cliente"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Life Events & Business Milestones:</strong> registra matrimonio, nacimiento, jubilación, expansión, IPO — dispara oportunidades proactivas.</div>'
         '<div class="tip-box">⚠️ <strong>Trampa:</strong> Referral Management rastrea referidos entre áreas (origen, estado, conversión); no gestiona hitos de vida.</div>'))

QUESTIONS.append(dict(
    num=5, s=1, qid='q05',
    txt="En el mapa del ecosistema, ¿qué combinación de nubes corresponde al área de Atención del Broker?",
    opt=[
        "Service Cloud + Omnichannel + Voice",
        "Insurance Cloud + Service Cloud + Voice",
        "FSC + Insurance Cloud + Slack",
        "FSC + Reportes"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Atención:</strong> Service (Casos) + Omni (canales: email, chat, WhatsApp, voz) + Voice (llamadas).</div>'
         '<div class="tip-box">⚠️ <strong>Trampa:</strong> Siniestros comparte Service y Voice pero suma Insurance; el distintivo de Atención es Omnichannel (multi-canal).</div>'))

QUESTIONS.append(dict(
    num=6, s=2, qid='q06',
    txt="ACME Corp. contrata un seguro colectivo y tú debes registrar a Juan Pérez, empleado de ACME, como asegurado individual en el modelo de datos FSC. ¿Qué objeto usas?",
    opt=[
        "Account (Person)",
        "Account (Business)",
        "Financial Account",
        "Household"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Account (Business)</strong> = empresa contratante; <strong>Account (Person)</strong> = persona física asegurada.</div>'
         '<div class="tip-box">⚠️ <strong>Trampa:</strong> Financial Account representa la cuenta de beneficios o la póliza maestra del colectivo, no a la persona.</div>'))

QUESTIONS.append(dict(
    num=7, s=2, qid='q07',
    txt="¿Qué objeto del modelo FSC agrupa a los miembros de una familia o colectivo (cónyuge, dependientes, beneficiarios) y permite cálculos como el rollup de AUM y net worth?",
    opt=[
        "Household",
        "Relationship",
        "Contact",
        "Activity / Task"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Household:</strong> agrupa Person Accounts en hogares, modela cónyuges/dependientes/beneficiarios y calcula AUM y net worth.</div>'
         '<div class="tip-box">⚠️ <strong>Trampa:</strong> Relationship conecta registros entre sí (vínculos), pero no agrupa familias ni calcula métricas financieras.</div>'))

QUESTIONS.append(dict(
    num=8, s=2, qid='q08',
    txt="En la operación diaria del Broker, ¿para qué se utiliza el objeto Relationship de FSC?",
    opt=[
        "Para conectar personas, empresas y cuentas entre sí dentro del modelo FSC (ej. empleado–empresa)",
        "Para guardar una copia de la póliza en PDF",
        "Para registrar el RFC y CURP del asegurado",
        "Para activar un Action Plan de renovación"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Relationship</strong> conecta personas, empresas y cuentas (vínculo empleado, cónyuge, dependiente).</div>'
         '<div class="tip-box">⚠️ <strong>Trampa:</strong> Registrar vínculos solo en notas de Chatter es un error común; el vínculo estructural se modela con Relationship.</div>'))

QUESTIONS.append(dict(
    num=9, s=2, qid='q09',
    txt="Un ejecutivo debe dar la vista 360° de ACME Corp: ver empresa, asegurados, pólizas, siniestros, oportunidades y actividades. ¿Qué práctica garantiza que la vista sea confiable y sin registros duplicados?",
    opt=[
        "Buscar duplicados antes de crear y vincular cada asegurado al Account Business mediante Relationships",
        "Crear un Account Business nuevo por cada empleado asegurado",
        "Mantener el historial en una hoja de cálculo sincronizada manualmente",
        "Registrar los vínculos únicamente como notas internas"],
    ans=0,
    just='<div class="concept-box">🔵 El <strong>360°</strong> consolida Account, pólizas, Claims, Opportunities y Activities del cliente.</div>'
         '<div class="example-box">🟢 Buenas prácticas: buscar antes de crear, vincular asegurados con Relationship y actualizar RFC/CURP.</div>'
         '<div class="tip-box">⚠️ Crear cuentas duplicadas o planillas externas rompe la vista única del cliente.</div>'))

QUESTIONS.append(dict(
    num=10, s=2, qid='q10',
    txt="¿Cuál de las siguientes acciones es un ERROR común identificado en la gestión de clientes y asegurados con FSC?",
    opt=[
        "Usar Account (Business) para registrar personas físicas aseguradas",
        "Vincular a cada asegurado con una Relationship a su empresa empleadora",
        "Buscar duplicados antes de crear un registro",
        "Documentar en Chatter las decisiones relevantes del cliente"],
    ans=0,
    just='<div class="concept-box">🔵 Errores comunes: duplicados por no buscar, Account(Business) para personas, campos obligatorios en blanco, relaciones en notas, no actualizar bajas.</div>'
         '<div class="tip-box">⚠️ Las otras opciones son buenas prácticas; la pregunta pide el ERROR.</div>'))

QUESTIONS.append(dict(
    num=11, s=2, qid='q11',
    txt="¿Qué representan la Banker Console, Advisor Console e Insurance Producer Console dentro de FSC?",
    opt=[
        "Consolas (layouts) preconfiguradas por rol para acelerar el trabajo de cada perfil",
        "Objetos de datos donde se almacenan las pólizas",
        "Reportes financieros obligatorios del regulador",
        "Colas de atención del área de Siniestros"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Consolas Especializadas:</strong> Banker, Advisor e Insurance Producer — layouts preconfigurados por rol.</div>'
         '<div class="tip-box">⚠️ Son vistas de trabajo por perfil, no tablas de datos ni reportes regulatorios.</div>'))

QUESTIONS.append(dict(
    num=12, s=2, qid='q12',
    txt="El área de riesgos recibe una recomendación de un ejecutivo comercial para ofrecer un seguro de Vida a un cliente existente. La trazabilidad del referido se gestiona con...",
    opt=[
        "Referral Management",
        "Life Events & Business Milestones",
        "Perfil Financiero del Cliente",
        "Modelo de Datos Especializado"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Referral Management:</strong> flujo de referidos con tracking de origen, estado, conversión y asignación automática por producto.</div>'
         '<div class="tip-box">⚠️ Distingue "hito de vida" (matrimonio, IPO) de "referido entre áreas" (recomendación de un ejecutivo).</div>'))

QUESTIONS.append(dict(
    num=13, s=2, qid='q13',
    txt="¿Qué muestra la vista de Perfil Financiero del Cliente en FSC?",
    opt=[
        "Cuentas, activos, pasivos, inversiones, pólizas y metas consolidadas del cliente en una sola pantalla",
        "Únicamente la prima de la póliza más reciente del asegurado",
        "El estado de las colas de Omnichannel",
        "El catálogo de productos de la aseguradora"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Perfil Financiero:</strong> vista consolidada 360° con cuentas, activos, pasivos, inversiones, pólizas y metas.</div>'
         '<div class="tip-box">⚠️ No es un reporte de una sola póliza ni del estado de colas/atención.</div>'))

QUESTIONS.append(dict(
    num=14, s=3, qid='q14',
    txt="En el modelo de operación del Broker, ¿cuál es la diferencia funcional clave frente a la Aseguradora?",
    opt=[
        "El Broker administra pólizas de múltiples aseguradoras, pero no suscribe ni liquida siniestros",
        "El Broker suscribe pólizas y la aseguradora solo administra las renovaciones",
        "El Broker liquida los siniestros y cobra la prima directamente al asegurado",
        "No hay diferencia: el Broker y la aseguradora ejecutan el mismo proceso"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Diferencia vs. Aseguradora:</strong> el Broker administra, no suscribe ni liquida.</div>'
         '<div class="example-box">🟢 El Broker recibe, registra, documenta y da seguimiento (primer punto de contacto); la aseguradora resuelve el siniestro.</div>'))

QUESTIONS.append(dict(
    num=15, s=3, qid='q15',
    txt="El objeto central de Insurance Cloud que representa la póliza y posee un identificador único (ej. POL-2024-001234) es...",
    opt=[
        "Insurance Policy",
        "Coverage",
        "Policy Participant",
        "Producer"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Insurance Policy:</strong> póliza de seguro — objeto central del módulo Insurance.</div>'
         '<div class="tip-box">⚠️ Coverage es la cobertura específica; Policy Participant es el asegurado incluido; Producer es el agente responsable.</div>'))

QUESTIONS.append(dict(
    num=16, s=3, qid='q16',
    txt="Dentro de una póliza colectiva GMM se incluyen Hospitalización, Dental y Óptica. ¿Cómo se modelan estos beneficios en Insurance Cloud?",
    opt=[
        "Como registros de Coverage vinculados a la Insurance Policy",
        "Como Opportunities de venta adicional",
        "Como Cases de la cola de servicios",
        "Como campos de texto libre del Account Business"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Coverage:</strong> cobertura o beneficio específico de la póliza (Hospitalización, Auto, etc.).</div>'
         '<div class="tip-box">⚠️ Una cobertura no es una venta (Opportunity), ni una solicitud (Case) ni texto del cliente.</div>'))

QUESTIONS.append(dict(
    num=17, s=3, qid='q17',
    txt="A mitad de la vigencia, ACME solicita agregar a tres empleados nuevos a la póliza GMM vigente. ¿Qué registro de Insurance Cloud refleja correctamente esa modificación?",
    opt=[
        "Un Endorsement (endoso) sobre la póliza vigente",
        "Una nueva Insurance Policy independiente",
        "Una Opportunity de cotización",
        "Un Case de la cola de siniestros"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Endorsement</strong> = endoso: modificación a una póliza vigente (cobertura, asegurado, prima).</div>'
         '<div class="example-box">🟢 Altas/bajas de asegurados y cambios de cobertura se registran como endosos, no como pólizas nuevas.</div>'
         '<div class="tip-box">⚠️ Una póliza nueva implicaría un contrato distinto; agregar asegurados es un movimiento de la misma póliza.</div>'))

QUESTIONS.append(dict(
    num=18, s=3, qid='q18',
    txt="¿Cuál es el punto de partida del proceso de renovación en el Broker?",
    opt=[
        "Identificación mediante el reporte de pólizas a vencer en 90/60/30 días",
        "La creación inmediata de la Opportunity de renovación",
        "La llamada al cliente para ofrecer un producto nuevo",
        "El envío de la póliza renovada al asegurado"],
    ans=0,
    just='<div class="example-box">🟢 Flujo: Identificación (reporte 90/60/30) → Asignación (tarea al ejecutivo) → Contacto → Cotización (Opportunity vinculada) → Negociación → Emisión.</div>'
         '<div class="tip-box">⚠️ La Opportunity de renovación se crea DESPUÉS de identificar y contactar; el reporte dispara el proceso.</div>'))

QUESTIONS.append(dict(
    num=19, s=3, qid='q19',
    txt="Se requiere que, cuando el estado de una póliza cambie a 'Vencida', Salesforce cree automáticamente una tarea de renovación para el ejecutivo. ¿Qué herramienta de automatización debes configurar?",
    opt=[
        "Flow Builder (Record-Triggered Flow)",
        "Approval Process",
        "Un dashboard de renovaciones",
        "Una cola de Omnichannel"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Flow Builder:</strong> automatización por eventos disparadores (fechas, cambios de estado, checklist).</div>'
         '<div class="tip-box">⚠️ Approval Process sirve para aprobaciones en cadena, no para disparar tareas por cambio de estado.</div>'))

QUESTIONS.append(dict(
    num=20, s=3, qid='q20',
    txt="Una póliza vigente inicia su gestión de renovación: se creó la Opportunity y el ejecutivo está negociando condiciones. Mientras tanto, ¿qué estado del ciclo de vida refleja la póliza en Salesforce?",
    opt=[
        "En Renovación",
        "Activa",
        "Vencida",
        "Cancelada"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Policy Status:</strong> Activa, En Renovación, Vencida, Cancelada — controla el ciclo de vida.</div>'
         '<div class="example-box">🟢 Solo hasta que se emite la renovación (nueva vigencia y prima) el estado vuelve a "Activa".</div>'))

QUESTIONS.append(dict(
    num=21, s=3, qid='q21',
    txt="Los campos Fecha de Inicio / Fecha de Fin (Vigencia) de la Insurance Policy son estratégicos porque...",
    opt=[
        "Activan las alertas de renovación (90/60/30 días) y delimitan el período de cobertura",
        "Definen el porcentaje de probabilidad de cierre de la Opportunity",
        "Determinan el ramo o tipo de seguro (GMM, Vida, Auto)",
        "Indican qué ejecutivo es el Producer responsable de la póliza"],
    ans=0,
    just='<div class="concept-box">🔵 La <strong>vigencia</strong> es clave para alertas de renovación y control del período de cobertura.</div>'
         '<div class="tip-box">⚠️ El ramo lo define "Tipo de Seguro"; el responsable lo define Producer; la vigencia gobierna renovaciones.</div>'))

QUESTIONS.append(dict(
    num=22, s=4, qid='q22',
    txt="Un ejecutivo envió la cotización formal y queda a la espera de la decisión del cliente. ¿Qué etapa del pipeline refleja este momento?",
    opt=[
        "Propuesta enviada",
        "Negociación",
        "Cierre ganado",
        "Calificando"],
    ans=0,
    just='<div class="example-box">🟢 Pipeline: Prospecto → Account → Opportunity abierta → Propuesta enviada → Negociación → Cierre ganado → Renovación (a los 90 días).</div>'
         '<div class="tip-box">⚠️ Negociación es cuando hay ajustes de cobertura/prima en curso; el envío del documento es Propuesta enviada.</div>'))

QUESTIONS.append(dict(
    num=23, s=4, qid='q23',
    txt="¿Qué campo es obligatorio en toda Opportunity y corresponde a la fecha estimada de cierre?",
    opt=[
        "Close Date",
        "Amount",
        "Probability",
        "Stage"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Close Date:</strong> fecha estimada de cierre — obligatoria en toda Opportunity.</div>'
         '<div class="tip-box">⚠️ Amount = prima estimada; Probability = % de cierre; Stage = estado del proceso. No confundir.</div>'))

QUESTIONS.append(dict(
    num=24, s=4, qid='q24',
    txt="¿Cómo se calcula el Win Rate (tasa de éxito) de un ejecutivo comercial?",
    opt=[
        "Oportunidades ganadas ÷ total de oportunidades",
        "Primas cobradas ÷ primas emitidas",
        "Casos resueltos ÷ casos recibidos",
        "Siniestros cerrados ÷ siniestros reportados"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Win Rate</strong> = oportunidades ganadas / total — métrica clave del ejecutivo.</div>'
         '<div class="tip-box">⚠️ Las otras fórmulas pertenecen a Cobranza, Servicio y Siniestros respectivamente.</div>'))

QUESTIONS.append(dict(
    num=25, s=4, qid='q25',
    txt="El Pipeline total del Broker se define como...",
    opt=[
        "El total de oportunidades abiertas ponderadas por su probabilidad",
        "La suma de las primas de todas las pólizas activas",
        "El total de casos abiertos en las colas de atención",
        "El número de leads generados en la última campaña"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Pipeline:</strong> total de oportunidades abiertas ponderadas por probabilidad.</div>'
         '<div class="tip-box">⚠️ Mezclar primas de pólizas o casos de servicio rompe el concepto comercial del pipeline.</div>'))

QUESTIONS.append(dict(
    num=26, s=4, qid='q26',
    txt="En un Action Plan de onboarding, la tarea 'Entregar documentos' solo debe aparecer después de completar 'Verificar identidad'. ¿Qué característica de Action Plans garantiza ese orden?",
    opt=[
        "Tareas con dependencias (la tarea siguiente solo aparece al completar la anterior)",
        "Asignación automática al responsable",
        "Fechas y plazos relativos desde el inicio del plan",
        "Plantillas reutilizables por proceso"],
    ans=0,
    just='<div class="concept-box">🔵 Tareas con <strong>dependencias</strong> encadenan el proceso y evitan saltarse pasos.</div>'
         '<div class="tip-box">⚠️ La asignación automática define QUIÉN hace; las dependencias definen CUÁNDO aparece cada tarea.</div>'))

QUESTIONS.append(dict(
    num=27, s=4, qid='q27',
    txt="Según las buenas prácticas de seguimiento comercial, ¿qué debe hacer el ejecutivo tras una reunión importante con el cliente?",
    opt=[
        "Actualizar la etapa de la Opportunity y registrar la actividad en el timeline",
        "Esperar a que el cliente confirme por email para registrar algo",
        "Marcar la Opportunity como cerrada perdida si no firmó en la reunión",
        "Crear una póliza provisional para no perder el registro"],
    ans=0,
    just='<div class="example-box">🟢 Buenas prácticas: registrar TODA interacción, actualizar etapa tras cada reunión, usar Path y evitar oportunidades sin actividad +15 días.</div>'
         '<div class="tip-box">⚠️ No mezclar venta nueva con renovaciones y registrar el motivo al cerrar perdida.</div>'))

QUESTIONS.append(dict(
    num=28, s=5, qid='q28',
    txt="Durante un siniestro de GMM, ¿cuál de las siguientes corresponde EXACTAMENTE al rol del Broker?",
    opt=[
        "Recibir, registrar, documentar y dar seguimiento ante la aseguradora",
        "Liquidar el siniestro y ordenar el pago al hospital",
        "Determinar si la póliza cubre o no el evento",
        "Emitir un endoso en el momento del siniestro"],
    ans=0,
    just='<div class="concept-box">🔵 El Broker <strong>NO liquida</strong>: la aseguradora resuelve. El Broker es el primer punto de contacto y da acompañamiento.</div>'
         '<div class="tip-box">⚠️ La decisión de cobertura y el pago son de la aseguradora; el Broker administra y da seguimiento.</div>'))

QUESTIONS.append(dict(
    num=29, s=5, qid='q29',
    txt="Un asegurado llama para reportar un siniestro de auto. Según el flujo end-to-end, ¿qué ocurre en el primer momento?",
    opt=[
        "Se crea automáticamente el Case (FNOL) en Service Cloud",
        "Se abre directamente el Claim en Insurance Cloud",
        "Se adjunta la documentación al expediente",
        "Se notifica el cierre a la aseguradora por Slack"],
    ans=0,
    just='<div class="example-box">🟢 Flujo: 1) FNOL → Case (Service) · 2) apertura del Claim (Insurance) · 3) documentación (Files) · 4) gestión con aseguradora · 5) comunicación · 6) cierre.</div>'
         '<div class="tip-box">⚠️ El Claim se crea DESPUÉS del Case; la documentación llega en el paso 3.</div>'))

QUESTIONS.append(dict(
    num=30, s=5, qid='q30',
    txt="¿Cómo se complementan el Case y el Claim en un siniestro?",
    opt=[
        "El Case gestiona la atención al asegurado (con SLA) y el Claim registra el avance del expediente con la aseguradora",
        "Son registros idénticos: se duplica la información para auditoría",
        "El Case es solo para quejas y el Claim para cobranza",
        "El Claim reemplaza al Case cuando la aseguradora acepta el siniestro"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Case</strong> = atención (SLA de respuesta); <strong>Claim</strong> = gestión del siniestro con la aseguradora. Son complementarios.</div>'
         '<div class="tip-box">⚠️ Los SLAs de atención aplican al Case; el Claim registra el avance del expediente.</div>'))

QUESTIONS.append(dict(
    num=31, s=5, qid='q31',
    txt="Al registrar un siniestro de la póliza colectiva GMM de ACME, ¿qué campo indica qué asegurado(s) resultaron afectados?",
    opt=[
        "Claim Participant",
        "Carrier",
        "Policy Status",
        "Claim Number"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Claim Participant:</strong> asegurado(s) afectado(s) por el siniestro.</div>'
         '<div class="tip-box">⚠️ Carrier es la aseguradora que debe resolver; Policy Status es el ciclo de vida de la póliza; Claim Number es el identificador.</div>'))

QUESTIONS.append(dict(
    num=32, s=5, qid='q32',
    txt="Un siniestro fue reportado, ya está 'En Proceso' y la aseguradora está evaluando la documentación. Antes de confirmar la resolución, el estado correcto es...",
    opt=[
        "En Revisión",
        "Resuelto",
        "Reportado",
        "Cerrado"],
    ans=0,
    just='<div class="concept-box">🔵 Estados del Claim: Reportado → En Proceso → En Revisión → Resuelto → Cerrado.</div>'
         '<div class="example-box">🟢 "En Revisión" es la etapa de evaluación por la aseguradora antes de Resuelto.</div>'
         '<div class="tip-box">⚠️ "Cerrado" solo llega tras resolver y documentar; "Reportado" es el inicio.</div>'))

QUESTIONS.append(dict(
    num=33, s=5, qid='q33',
    txt="Los SLAs de atención (tiempo máximo de respuesta al asegurado) en el ecosistema del Broker se aplican a...",
    opt=[
        "El Case de Service Cloud",
        "El Claim de Insurance Cloud",
        "La Opportunity de renovación",
        "El Action Plan de onboarding"],
    ans=0,
    just='<div class="concept-box">🔵 El <strong>SLA de respuesta al asegurado</strong> aplica al Case; el Claim registra el avance del expediente.</div>'
         '<div class="tip-box">⚠️ Aunque el Claim ES el siniestro, la promesa de tiempo al cliente se mide en el Case.</div>'))

QUESTIONS.append(dict(
    num=34, s=5, qid='q34',
    txt="En un siniestro complejo, el equipo decide en Slack #siniestros-complejos quién gestiona con la aseguradora. Según la regla de oro, ¿qué debe ocurrir después?",
    opt=[
        "Registrar la decisión en el Claim/Case de Salesforce (fuente de verdad)",
        "Dejar el acuerdo solo en el hilo de Slack para no duplicar",
        "Enviar el acuerdo por email a todo el equipo",
        "Cerrar el Case sin documentar porque ya se decidió"],
    ans=0,
    just='<div class="formula-box">🟠 Regla de oro: <strong>lo que se decide en Slack, se registra en Salesforce.</strong> Slack = conversación · Salesforce = fuente de verdad.</div>'
         '<div class="tip-box">⚠️ El escalamiento llega a Slack con link al Claim, pero la trazabilidad vive en Salesforce.</div>'))

QUESTIONS.append(dict(
    num=35, s=6, qid='q35',
    txt="En Service Cloud, un asegurado escribe por WhatsApp solicitando su certificado de cobertura. ¿Qué representación recibe esa solicitud en Salesforce?",
    opt=[
        "Un Case con número único, responsable e historial",
        "Una Insurance Policy nueva",
        "Una Opportunity de venta",
        "Un Work Item asignado a una agencia externa"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Case:</strong> registro central de solicitud/consulta/siniestro con número único, responsable e historial completo.</div>'
         '<div class="tip-box">⚠️ El Work Item es el concepto de Omnichannel (distribución por canal); en Service Cloud el registro de la solicitud es el Case.</div>'))

QUESTIONS.append(dict(
    num=36, s=6, qid='q36',
    txt="¿Qué campo del Case determina el SLA y el orden de atención?",
    opt=[
        "Prioridad (Alta / Media / Baja)",
        "Origen (Email/Teléfono/Web)",
        "Tipo de Caso",
        "Queue"],
    ans=0,
    just='<div class="concept-box">🔵 La <strong>Prioridad</strong> (Alta / Media / Baja) determina el orden de atención y el SLA.</div>'
         '<div class="example-box">🟢 Ej: siniestro urgente = Alta; consulta de cobertura = Media; certificado = Baja.</div>'
         '<div class="tip-box">⚠️ El Origen registra el canal; la Queue agrupa por área; el orden lo manda la Prioridad.</div>'))

QUESTIONS.append(dict(
    num=37, s=6, qid='q37',
    txt="Si un Case está cerca de incumplir su SLA sin respuesta, ¿qué hace Salesforce automáticamente?",
    opt=[
        "Escala el caso para que sea atendido antes del vencimiento",
        "Cierra el caso y notifica al asegurado",
        "Convierte el caso en un Claim",
        "Borra el caso de la cola"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>SLA:</strong> Salesforce mide el tiempo comprometido y <strong>escala automáticamente</strong> si se acerca al límite.</div>'
         '<div class="tip-box">⚠️ Nunca cierra ni elimina: el objetivo es salvarlo escalando.</div>'))

QUESTIONS.append(dict(
    num=38, s=6, qid='q38',
    txt="Con las colas de Service Cloud, ¿quién decide qué agente toma cada Case?",
    opt=[
        "El sistema: asigna a la cola correcta por regla y el agente toma el siguiente según prioridad",
        "El supervisor asigna manualmente cada caso uno a uno",
        "El asegurado elige al ejecutivo de su preferencia",
        "El caso se asigna al primer agente que inicie sesión"],
    ans=0,
    just='<div class="formula-box">🟠 Regla de oro de las Colas: <strong>"Nadie asigna manualmente... el sistema lo resuelve solo."</strong></div>'
         '<div class="concept-box">🔵 Visibilidad compartida de la cola + escalamiento + capacidad configurable.</div>'
         '<div class="tip-box">⚠️ El supervisor puede reasignar, pero la operación normal es automática.</div>'))

QUESTIONS.append(dict(
    num=39, s=6, qid='q39',
    txt="Un agente recibe muchas consultas idénticas sobre cobertura dental. ¿Qué componente de Service Cloud le permite responder con una respuesta estándar sin redactar desde cero?",
    opt=[
        "Knowledge Articles",
        "Macros",
        "Entitlements",
        "Service Console"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Knowledge Article:</strong> respuesta estándar a preguntas frecuentes.</div>'
         '<div class="tip-box">⚠️ Macro ejecuta acciones rápidas (email, cambio de estado, cierre); Entitlement define el SLA; Knowledge resuelve "qué responder".</div>'))

QUESTIONS.append(dict(
    num=40, s=6, qid='q40',
    txt="¿Cuál es la ventaja funcional de la Service Console para el agente?",
    opt=[
        "Ver el Case, el cliente y el historial en una sola pantalla",
        "Generar reportes de primas sin permisos",
        "Editar directamente la vigencia de las pólizas",
        "Sustituir a los dashboards de gerencia"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Service Console:</strong> interfaz del agente = vista de caso + cliente + historial en una pantalla.</div>'
         '<div class="tip-box">⚠️ Es una vista de trabajo, no un editor de pólizas ni un sustituto de reportes.</div>'))

QUESTIONS.append(dict(
    num=41, s=6, qid='q41',
    txt="Un agente atendió la solicitud del asegurado y envió una aclaración, pero necesita que el cliente confirme los datos para continuar. ¿Qué estado refleja correctamente esta situación?",
    opt=[
        "Pendiente Cliente",
        "En Proceso",
        "Resuelto",
        "Cerrado"],
    ans=0,
    just='<div class="concept-box">🔵 Estados: Nuevo → Asignado → En Proceso → <strong>Pendiente Cliente</strong> → Resuelto → Cerrado.</div>'
         '<div class="example-box">🟢 "Pendiente Cliente" indica que la pelota está del lado del asegurado.</div>'))

QUESTIONS.append(dict(
    num=42, s=7, qid='q42',
    txt="¿Qué es Omnichannel en el ecosistema del Broker?",
    opt=[
        "El motor que recibe solicitudes de todos los canales y las asigna automáticamente al agente disponible con menor carga",
        "Una consola de reportes para medir tiempos de llamada",
        "Un módulo para administrar pólizas de múltiples aseguradoras",
        "Una red telefónica externa de la aseguradora"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Omnichannel:</strong> recibe email, teléfono, chat, WhatsApp y portal; distribuye al agente correcto según disponibilidad, carga y habilidades.</div>'
         '<div class="tip-box">⚠️ No es Reportes, no es Insurance ni telefonía externa: es el orquestador de canales.</div>'))

QUESTIONS.append(dict(
    num=43, s=7, qid='q43',
    txt="Cuando un asegurado escribe por WhatsApp y otro llama por teléfono, ¿en qué se convierten esas solicitudes dentro de Omnichannel?",
    opt=[
        "Work Items (unidades de trabajo) asignadas a los agentes",
        "Casos manuales que cada agente debe crear",
        "Oportunidades de servicio",
        "Registros de Knowledge"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Work Item:</strong> unidad de trabajo; su contexto viaja con él (historial completo del cliente).</div>'
         '<div class="tip-box">⚠️ El caso se crea a partir del Work Item, pero el concepto del canal es Work Item, no un Case manual.</div>'))

QUESTIONS.append(dict(
    num=44, s=7, qid='q44',
    txt="¿Qué condición determina que Omnichannel envíe un nuevo Work Item a un agente?",
    opt=[
        "Su estado (Presence) está en 'Disponible' y no supera su capacidad",
        "Tener la consola abierta aunque esté en pausa",
        "Haber atendido el último ítem de la cola",
        "Estar conectado por videollamada"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Presence:</strong> Disponible, Ocupado, En Pausa o Fuera de Línea. El sistema solo envía trabajo cuando está Disponible.</div>'
         '<div class="example-box">🟢 <strong>Capacity</strong> limita cuántos Work Items simultáneos puede atender.</div>'
         '<div class="tip-box">⚠️ Estar "conectado" pero "En Pausa" NO recibe trabajo.</div>'))

QUESTIONS.append(dict(
    num=45, s=7, qid='q45',
    txt="El Capacity (capacidad) de un agente en Omnichannel representa...",
    opt=[
        "El número máximo de Work Items simultáneos que puede atender",
        "El número de canales a los que está suscrito",
        "El tiempo máximo que puede estar en pausa",
        "La cantidad de hilos de Slack que puede abrir"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Capacity:</strong> máximo de Work Items simultáneos de un agente.</div>'
         '<div class="tip-box">⚠️ No confundir con canales suscritos ni con tiempos de pausa.</div>'))

QUESTIONS.append(dict(
    num=46, s=7, qid='q46',
    txt="¿Qué acción forma parte del control en tiempo real del supervisor en Omnichannel?",
    opt=[
        "Redistribuir ítems entre agentes con un clic y ver colas acumuladas antes de que impacten",
        "Cambiar la moneda de las primas de las pólizas",
        "Eliminar el SLA de los casos de la cola",
        "Editar la estructura organizacional del Workspace de Slack"],
    ans=0,
    just='<div class="concept-box">🔵 El supervisor ve agentes activos, carga, colas y SLAs en riesgo, y <strong>reasigna con un clic</strong>.</div>'
         '<div class="tip-box">⚠️ Las demás opciones no pertenecen a la vista de supervisión de Omnichannel.</div>'))

QUESTIONS.append(dict(
    num=47, s=8, qid='q47',
    txt="Cuando un asegurado llama y Salesforce identifica su número, ¿qué sucede antes de que el agente conteste?",
    opt=[
        "Screen Pop: aparece el registro del cliente con pólizas, Cases y siniestros",
        "Se abre una Opportunity de venta automática",
        "El sistema envía un email de confirmación",
        "Se crea una tarea para el supervisor"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Screen Pop:</strong> identifica al asegurado y muestra su registro completo antes de contestar.</div>'
         '<div class="tip-box">⚠️ Con Voice el agente ya sabe quién es y su contexto; no hay búsqueda manual.</div>'))

QUESTIONS.append(dict(
    num=48, s=8, qid='q48',
    txt="¿Qué permite Click-to-Dial en Service Cloud Voice?",
    opt=[
        "Llamar al cliente desde un clic en cualquier registro; la llamada sale del softphone y queda registrada en el Timeline",
        "Grabar la pantalla del cliente",
        "Transferir llamadas directo a Slack",
        "Enviar la póliza por SMS"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Click-to-Dial:</strong> llamada con un clic desde Account/Case/Póliza; queda automáticamente en el Timeline.</div>'
         '<div class="tip-box">⚠️ La llamada sale del softphone integrado, sin hardware adicional.</div>'))

QUESTIONS.append(dict(
    num=49, s=8, qid='q49',
    txt="Al colgar una llamada, el agente documenta el Case y clasifica el resultado con códigos como 'Consulta Atendida' o 'Siniestro Reportado'. ¿Qué nombre reciben esos códigos?",
    opt=[
        "Wrap-Up Codes",
        "Screen Pops",
        "Entitlements",
        "Presence States"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Wrap-Up Code:</strong> clasifica el resultado de la llamada y alimenta reportes (mix real de consultas).</div>'
         '<div class="example-box">🟢 El <strong>ACW</strong> (After Call Work) es el tiempo para documentar antes de recibir la siguiente llamada.</div>'
         '<div class="tip-box">⚠️ Screen Pop es la ficha al entrar; Presence es el estado del agente.</div>'))

QUESTIONS.append(dict(
    num=50, s=8, qid='q50',
    txt="Durante la llamada, Einstein Conversation Intelligence transcribe el audio en tiempo real y detecta que el asegurado menciona 'cancelar'. ¿Qué más puede hacer la IA en ese momento?",
    opt=[
        "Sugerir un artículo de Knowledge relacionado y alertar sobre el tema clave",
        "Reasignar la llamada a otro agente sin avisar",
        "Cerrar el Case automáticamente con prioridad Baja",
        "Enviar la cotización de renovación directo al asegurado"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Einstein:</strong> transcripción, análisis de sentimiento, alertas de temas clave (siniestro, cancelar, queja, urgente), sugerencias de Knowledge y resumen automático.</div>'
         '<div class="tip-box">⚠️ Einstein asiste al agente; no cierra Cases ni gestiona cobranza por sí mismo.</div>'))

QUESTIONS.append(dict(
    num=51, s=8, qid='q51',
    txt="¿Cuál es el beneficio directo del IVR para el asegurado que llama?",
    opt=[
        "Enruta la llamada al área correcta antes del agente → menor tiempo de espera y contexto correcto",
        "Elimina la necesidad de grabar la llamada",
        "Sustituye por completo al agente",
        "Solo aplica a llamadas de cobranza"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>IVR</strong> (menú de voz): enruta la llamada al área correcta antes de llegar al agente.</div>'
         '<div class="example-box">🟢 Menor tiempo de espera y resolución más rápida: el agente recibe con contexto (Screen Pop).</div>'))

QUESTIONS.append(dict(
    num=52, s=9, qid='q52',
    txt="El área de Cobranza necesita una lista exacta de pólizas con prima vencida para gestionar cada cuenta y exportarla a Excel. ¿Qué herramienta debe usar?",
    opt=[
        "Un Reporte (tabla de registros exportable a Excel/CSV/PDF)",
        "Un Dashboard (gráficas de un vistazo)",
        "Una alerta de SLA",
        "Un Workflow de Slack"],
    ans=0,
    just='<div class="example-box">🟢 <strong>Reporte:</strong> lista/tabla de registros, agrupable y exportable; ideal para trabajar los datos.</div>'
         '<div class="concept-box">🔵 <strong>Dashboard:</strong> pantalla visual con gráficas y semáforos; no exporta registros individuales.</div>'
         '<div class="tip-box">⚠️ Para "trabajar la lista" se usa Reporte; el Dashboard es para el estado general.</div>'))

QUESTIONS.append(dict(
    num=53, s=9, qid='q53',
    txt="El equipo comercial quiere recibir el reporte de Pipeline todos los lunes a las 8:00 a. m. sin tener que ejecutarlo manualmente. ¿Qué funcionalidad debes configurar?",
    opt=[
        "La suscripción/programación del reporte por email",
        "Un dashboard compartido estático",
        "Una cola de Omnichannel",
        "Un Approval Process"],
    ans=0,
    just='<div class="concept-box">🔵 Los reportes se pueden <strong>programar</strong>: envío automático por email (ej. cada lunes).</div>'
         '<div class="tip-box">⚠️ El dashboard se refresca al abrirlo, pero el envío programado es funcionalidad de los reportes.</div>'))

QUESTIONS.append(dict(
    num=54, s=9, qid='q54',
    txt="Las alertas automáticas por vencimiento de póliza se disparan...",
    opt=[
        "90/60/30 días antes del vencimiento: tarea al ejecutivo + aviso en Slack #renovaciones-urgentes",
        "El mismo día del vencimiento para no molestar antes",
        "15 días después del vencimiento, ya con la póliza vencida",
        "Solo cuando el cliente pregunta por su renovación"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Vencimiento de póliza:</strong> 90/60/30 días antes → tarea automática y aviso en Slack.</div>'
         '<div class="example-box">🟢 La identificación temprana activa todo el flujo de renovación (reporte → tarea → contacto).</div>'))

QUESTIONS.append(dict(
    num=55, s=9, qid='q55',
    txt="El gerente quiere ver en un vistazo siniestros abiertos vs. cerrados, el pipeline por etapa y primas por cobrar. ¿Cuál es la mejor herramienta?",
    opt=[
        "Un Dashboard con gráficas, contadores y semáforos que se refresca al abrirlo",
        "Un Reporte tabular de cada dato por separado",
        "Una suscripción semanal de un reporte",
        "Un Work Item de la cola de cobranza"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Dashboard:</strong> semáforos, donas, barras y números grandes → decisiones rápidas de un vistazo.</div>'
         '<div class="tip-box">⚠️ Si se necesitara exactitud registro por registro y exportación, sería Reporte; para visión general, Dashboard.</div>'))

QUESTIONS.append(dict(
    num=56, s=10, qid='q56',
    txt="El canal #siniestros-complejos se llena de respuestas cruzadas sobre varios casos. ¿Qué práctica mantiene limpio el canal y organiza el contexto por caso?",
    opt=[
        "Responder en un Hilo (thread) al mensaje original de cada caso",
        "Crear un nuevo canal público para cada mensaje",
        "Enviar las respuestas por mensaje directo al jefe",
        "Usar una única cadena de menciones @channel sin estructura"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Hilo (thread):</strong> respuesta anidada a un mensaje; mantiene limpio el canal y organizado el contexto.</div>'
         '<div class="example-box">🟢 Buenas prácticas: si la conversación supera 5 mensajes, mover a Huddle o reunión.</div>'))

QUESTIONS.append(dict(
    num=57, s=10, qid='q57',
    txt="El Broker necesita coordinar la documentación de un siniestro directamente con la aseguradora (empresa externa). ¿Qué funcionalidad de Slack lo permite?",
    opt=[
        "Slack Connect (canal compartido con una organización externa)",
        "Huddle dentro del canal interno",
        "Workflow Builder de aprobaciones internas",
        "Canvas del equipo"],
    ans=0,
    just='<div class="concept-box">🔵 <strong>Slack Connect:</strong> canal compartido con un cliente o partner externo (la aseguradora).</div>'
         '<div class="tip-box">⚠️ Huddle = llamada interna; Canvas = documento colaborativo; Workflow = automatización sin código.</div>'))

QUESTIONS.append(dict(
    num=58, s=10, qid='q58',
    txt="Se desea que un formulario de escalamiento de casos cree automáticamente una alerta en el canal #escalamientos. ¿Qué herramienta de bajo código usas y en qué plataforma?",
    opt=[
        "Workflow Builder, en Slack",
        "Flow Builder, en Salesforce (Record-Triggered Flow)",
        "Macro de la Service Console",
        "Approval Process de Financial Cloud"],
    ans=0,
    just='<div class="formula-box">🟠 Regla: <strong>Flow Builder</strong> automatiza datos/registros en Salesforce; <strong>Workflow Builder</strong> automatiza conversaciones/formularios dentro de Slack.</div>'
         '<div class="tip-box">⚠️ Trampa clásica: "Flow" está en Salesforce; para alertas en Slack desde un formulario, es Workflow Builder.</div>'))

QUESTIONS.append(dict(
    num=59, s=10, qid='q59',
    txt="¿Qué permite la integración 'App de Salesforce en Slack'?",
    opt=[
        "Ver y actualizar registros de Salesforce desde Slack: estado del Case, etapa de Opportunity, notas del Claim, crear Tareas",
        "Reemplazar por completo a la consola de Salesforce",
        "Grabar llamadas desde el canal",
        "Enviar pólizas impresas al asegurado"],
    ans=0,
    just='<div class="example-box">🟢 Acciones desde el chat: actualizar Case, cambiar etapa de Opportunity, agregar nota al Claim y crear Tarea — sin salir de la conversación.</div>'
         '<div class="concept-box">🔵 Las alertas Salesforce→Slack llegan automáticas (Claim prioridad Alta → #siniestros-complejos).</div>'
         '<div class="tip-box">⚠️ Salesforce sigue siendo la fuente de verdad; Slack es la conversación.</div>'))

QUESTIONS.append(dict(
    num=60, s=10, qid='q60',
    txt="En el ejercicio final se cerró un siniestro que se coordinó en Slack. Según el flujo integrado, ¿cuál es el cierre correcto del proceso?",
    opt=[
        "Actualizar el Claim a 'Resuelto', documentar la solución, cerrar el Case vinculado y publicar el cierre en Slack",
        "Borrar el hilo de Slack para eliminar evidencia",
        "Solo escribir 'cerrado' en Slack y no tocar Salesforce",
        "Convertir el Claim en una Opportunity de renovación"],
    ans=0,
    just='<div class="formula-box">🟠 Regla de oro: <strong>lo que se coordina en Slack se registra en Salesforce.</strong></div>'
         '<div class="example-box">🟢 Caso final: Voice → Case → Claim → coordinación Slack → reporte/dashboard → Claim "Resuelto" → Case cerrado → publicación en Slack.</div>'
         '<div class="tip-box">⚠️ Slack documenta la conversación; Salesforce registra el resultado del negocio.</div>'))


def main():
    html = build_html()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    n_radios = html.count('type="radio"')
    n_q = len(QUESTIONS)
    print(f"✅ Generado: {OUT}")
    print(f"📊 Preguntas: {n_q} | Radio inputs: {n_radios} (esperado {n_q*4}) | HTML chars: {len(html):,}")


if __name__ == "__main__":
    main()