# -*- coding: utf-8 -*-
"""
gen_guia_examen_v2.py — Generador COMBINADO v2 (ParetoTutor Visual)
Guía navegable por temas + Examen interactivo con guardado y feedback por pregunta,
en UN SOLO archivo HTML autocontenido (offline, imprimible a PDF).
"""
import json, os
import estilo_base as EB

OUT = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Guia_Examen_Entrevista_Tecnica.html"
EXAMEN_ID = "entrevista_tecnica"

# ============ CONTENIDO: TEMAS DE LA GUIA ============
TEMAS = [
("soporte", "🛠️ Soporte TI y Troubleshooting", "alta",
 EB.B("azul","🧠","Metodología de 7 pasos", EB.TAB(["Paso","Qué haces"], [
   ["1 Identificar","Síntomas + alcance + usuarios afectados"],
   ["2 Reproducir","Replica el error en entorno controlado"],
   ["3 Aislar","Hardware vs software · red vs local"],
   ["4 Diagnosticar","Event Viewer, logs, pruebas"],
   ["5 Solucionar","Aplica el fix documentado"],
   ["6 Validar","Confirma con el usuario + monitoreo"],
   ["7 Documentar","Ticket + base de conocimiento"],
 ])) +
 EB.B("naranja","🛠️","Windows 10/11: herramientas", EB.LI([
   "<b>Event Viewer:</b> causa raíz en <code>System / Application</code>.",
   "<b>Task Manager:</b> disco o CPU al 100%, procesos colgados.",
   "<b>Administrador de dispositivos:</b> drivers con alerta amarilla.",
   "<b>Servicios (services.msc):</b> servicios detenidos o en manual.",
   "<b>Perfiles y permisos:</b> perfil corrupto vs falla del equipo.",
 ])) +
 EB.B("rojo","⚠️","Priorización y conceptos", EB.LI([
   "<b>Prioridad = impacto + urgencia + usuarios + criticidad + SLA.</b>",
   "<b>Incidente</b> = interrupción · <b>Solicitud</b> = petición · <b>Problema</b> = causa raíz.",
   "<b>Escala</b> cuando: sin acceso, sin avance, o SLA en riesgo.",
   "<b>SLA</b> = tiempo comprometido de respuesta y resolución.",
 ])) +
 EB.RECALL([
   ("¿Cuál es tu metodología ante un incidente?", "Identificar, reproducir, aislar, diagnosticar, solucionar, validar y documentar."),
   ("¿Cuándo escalas un incidente?", "Sin permisos o acceso, sin avance tras aislar, o con SLA en riesgo."),
 ])),
("redes", "🌐 Redes TCP/IP", "alta",
 EB.B("azul","🧠","Conceptos que SIEMPRE preguntan", EB.LI([
   "<b>IP vs MAC:</b> IP lógica; MAC física única.",
   "<b>IPv4 vs IPv6:</b> 32 vs 128 bits; IPv6 sin NAT.",
   "<b>Privadas:</b> <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>.",
   "<b>Gateway:</b> ruta por defecto. <b>NAT:</b> privada→pública.",
   "<b>DHCP:</b> asigna IP (DORA). <b>DNS:</b> nombre→IP.",
   "<b>VLAN:</b> segmentación lógica de la red física.",
 ])) +
 EB.B("naranja","🛠️","Comandos", EB.PRE("ipconfig /all   → IP, MAC, DNS\nping 8.8.8.8    → conectividad\nnslookup nombre → resolución DNS\ntracert destino → salto que falla")) +
 EB.B("mapa","🗺️","Cadena de diagnóstico", EB.TAB(["#","Prueba","Si falla →"], [
   ["1","<code>ipconfig</code> ¿IP válida?","Red / DHCP"],
   ["2","<code>ping gateway</code>","LAN / switch"],
   ["3","<code>ping 8.8.8.8</code>","ISP / NAT"],
   ["4","<code>nslookup</code>","DNS"],
 ])) +
 EB.RECALL([
   ("¿IP vs MAC?", "IP = lógica (cambia); MAC = física única del adaptador."),
   ("Sin Internet, ¿cómo diagnosticas?", "ipconfig → ping gateway → ping 8.8.8.8 → nslookup."),
 ])),
("ciberseguridad", "🔐 Ciberseguridad", "alta",
 EB.B("azul","🧠","Tríada CIA", EB.TAB(["Concepto","Significado","Ejemplo"], [
   ["<b>Confidencialidad</b>","Solo quien debe accede","Cifrado, permisos"],
   ["<b>Integridad</b>","Los datos no se alteran","Hashes, firmas"],
   ["<b>Disponibilidad</b>","Disponible cuando se necesita","Backups, HA"],
 ]) + "<p><b>Riesgo = Amenaza × Vulnerabilidad × Impacto</b></p>") +
 EB.B("rojo","⚠️","Ataques", EB.LI([
   "<b>Phishing:</b> robar credenciales con páginas falsas.",
   "<b>Ransomware:</b> cifra archivos; defensa = backups 3-2-1.",
   "<b>Brute force / credential stuffing:</b> MFA.",
   "<b>Ingeniería social:</b> manipular personas.",
 ])) +
 EB.B("verde","🟢","¿Qué es EDR?",
   "<p><b>“Monitorea endpoints buscando comportamiento malicioso (no solo firmas), detecta, alerta y responde aislando el equipo.”</b></p>") +
 EB.RECALL([
   ("¿Amenaza vs vulnerabilidad?", "Amenaza = lo que puede dañar; vulnerabilidad = la debilidad que lo permite."),
 ])),
("iam", "🪪 IAM — Identidades y accesos", "alta",
 EB.B("azul","🧠","La frase que te salva",
   "<blockquote><b>Autenticación</b> = quién eres · <b>Autorización</b> = qué puedes hacer · <b>Auditoría</b> = registro.</blockquote>") +
 EB.B("naranja","🛠️","Modelos", EB.TAB(["Modelo","Base","Cuándo"], [
   ["<b>RBAC</b>","Rol del usuario","Puestos definidos"],
   ["<b>ABAC</b>","Atributos (usuario+recurso+contexto)","Acceso dinámico y fino"],
 ]) + "<p><b>MFA:</b> saber+tener+ser · <b>SSO:</b> 1 login para todas las apps</p>") +
 EB.B("rojo","⚠️","Trampa",
   "<p>«Contraseña correcta pero acceso denegado» → <b>NO falló la autenticación</b>: no está <b>autorizado</b>.</p>") +
 EB.RECALL([
   ("¿Autenticación vs autorización?", "Autenticación = quién eres; autorización = qué puedes hacer."),
 ])),
("sql", "🗃️ SQL", "media-alta",
 EB.B("azul","🧠","Cláusulas esenciales", EB.PRE("SELECT ... FROM ... WHERE ...\nGROUP BY ... HAVING ... ORDER BY ...")) +
 EB.B("naranja","🛠️","JOINs", EB.TAB(["JOIN","Qué devuelve","Cuándo"], [
   ["<b>INNER JOIN</b>","Solo coincidencias en ambas","Clientes CON pedidos"],
   ["<b>LEFT JOIN</b>","Todo de la izquierda + NULLs","TODOS los clientes"],
 ])) +
 EB.B("verde","🟢","Ejemplo", EB.PRE("SELECT u.nombre, i.codigo\nFROM usuarios u\nLEFT JOIN inventario i ON u.id = i.usuario_id") +
   "<p>Usuarios siempre; inventario donde exista (si no → <code>NULL</code>).</p>") +
 EB.RECALL([
   ("¿INNER vs LEFT JOIN?", "INNER solo coincidencias; LEFT todo lo de la izquierda + NULLs."),
 ])),
("ia", "🤖 IA y agentes", "media",
 EB.B("azul","🧠","Conceptos base", EB.LI([
   "<b>LLM:</b> modelo de lenguaje masivo.",
   "<b>Prompt:</b> instrucción · <b>tokens:</b> unidades de texto.",
   "<b>Embedding:</b> vector numérico del significado.",
 ])) +
 EB.B("mapa","🗺️","Chatbot vs Agente", EB.TAB(["Chatbot","Agente"], [
   ["Responde con su conocimiento","EJECUTA acciones (tool calling, APIs)"],
 ]) + '<p class="sub"><b>“El agente es un chatbot con manos y herramientas.”</b></p>') +
 EB.B("naranja","🛠️","RAG", EB.LI([
   "Recupera documentos relevantes y genera con esa base.",
   "Reduce <b>alucinaciones</b> sin reentrenar.",
 ])) +
 EB.RECALL([
   ("¿Qué es RAG?", "Retrieval-Augmented Generation: recupera docs (embeddings) y responde con base en ellos."),
 ])),
("python-auto", "🐍 Python y automatización", "media",
 EB.B("azul","🧠","Por qué Python en soporte", EB.LI([
   "Automatiza altas y bajas, reportes de tickets, lectura de logs y respaldos.",
   "Bibliotecas típicas: <code>os</code>, <code>csv</code>, <code>requests</code>, <code>pandas</code>.",
 ])) +
 EB.B("verde","🟢","Script mínimo defendible",
   EB.PRE("import csv\nwith open('usuarios.csv', encoding='utf-8') as f:\n    for row in csv.DictReader(f):\n        print(row['nombre'], row['area'])")) +
 EB.B("rojo","⚠️","C++: qué decir",
   "<p>Nivel formativo: POO, estructuras y compilación. Úsalo solo si el puesto lo pide; tu fortaleza práctica es <b>Python + Full-Stack</b>.</p>") +
 EB.RECALL([
   ("¿Ejemplo de automatización?", "Script que lee un CSV de usuarios y genera altas o un reporte automáticamente."),
 ])),
("fullstack", "🌐 Full-Stack: API, REST, Git y Docker", "media",
 EB.B("azul","🧠","Definiciones que siempre preguntan", EB.TAB(["Término","Respuesta de 1 línea"], [
   ["<b>API</b>","Contrato para que dos programas se comuniquen"],
   ["<b>REST</b>","Estilo con verbos HTTP sobre recursos (GET/POST/PUT/DELETE)"],
   ["<b>CRUD</b>","Create/Read/Update/Delete = POST/GET/PUT/DELETE"],
   ["<b>JSON</b>","Formato ligero de intercambio"],
   ["<b>Frontend vs backend</b>","Lo que ve el usuario vs lógica + datos"],
 ])) +
 EB.B("verde","🟢","Git y Docker", EB.LI([
   "<b>Git:</b> <code>clone, add, commit, push y pull</code>; ramas para no romper main.",
   "<b>Docker:</b> imagen = plantilla; contenedor = instancia corriendo.",
   "<b>Comandos:</b> <code>docker build</code>, <code>docker run</code>, <code>docker ps</code>.",
 ])) +
 EB.B("naranja","🛠️","Tu proyecto defendible",
   "<p>Sistema de inventario y usuarios (Full-Stack, arquitectura relacional): altas y bajas, CRUD contra API, base SQL.</p>") +
 EB.RECALL([
   ("¿Imagen vs contenedor?", "Imagen = plantilla inmutable; contenedor = proceso corriendo desde esa imagen."),
   ("¿REST en 1 línea?", "Exponer recursos con verbos HTTP y respuestas JSON."),
 ])),
("iso-gestion", "📋 ISO 27001, Jira y guion PAR-hT", "media",
 EB.B("azul","🧠","ISO 27001 en 3 frases", EB.LI([
   "Norma de <b>SGSI</b>: proteger confidencialidad, integridad y disponibilidad.",
   "Anexo A: controles de acceso, cifrado, respaldo y registro.",
   "Regla de honestidad: habla de <b>práctica documental alineada a ISO 27001</b>, sin afirmar que implementaste toda la norma.",
 ])) +
 EB.B("verde","🟢","Jira y Monday + SLA", EB.LI([
   "Ticket: incidente, request, prioridad, severidad, SLA, escalamiento, asignación, estado y resolución.",
   "278 tickets con 98.6% de efectividad = volumen + resultado medible.",
 ])) +
 EB.B("naranja","🛠️","Guion PAR-hT (60-90 seg)",
   "<p><b>Problema, Acción, Resultado, Herramientas y Aprendizaje.</b> Ten listos 3 incidentes: soporte, accesos o seguridad, e infraestructura o redes; más 1 ejemplo de automatización y 1 de Full-Stack.</p>") +
 EB.RECALL([
   ("¿Qué es PAR-hT?", "Estructura tu respuesta: Problema, Acción, Resultado, Herramientas y Aprendizaje."),
 ])),
("workspace-gcp", "☁️ Google Workspace y GCP", "media-alta",
 EB.B("azul","🧠","Workspace: administración", EB.LI([
   "<b>Usuarios, grupos y roles:</b> altas, bajas, suspensión y licencias.",
   "<b>Drive y Shared Drives:</b> propiedad del equipo, no del usuario.",
   "<b>MFA y políticas:</b> verificación en 2 pasos + políticas de contraseña.",
 ])) +
 EB.B("verde","🟢","GCP: Projects + IAM + recursos", EB.LI([
   "<b>Project:</b> contenedor de recursos con facturación propia.",
   "<b>IAM:</b> quién puede hacer qué (rol = permiso agrupado).",
   "<b>Service Account:</b> identidad para APPS y servicios, NO personas.",
   "<b>VPC:</b> red privada · <b>Compute Engine:</b> VMs · <b>Cloud Storage:</b> objetos.",
   "<b>Logs y APIs:</b> Cloud Logging + habilitar APIs por proyecto.",
 ])) +
 EB.B("rojo","⚠️","Trampa típica",
   "<p><b>Usuario vs Service Account:</b> usuario = persona; SA = app o servicio. Nunca des llaves de SA a un humano.</p>") +
 EB.RECALL([
   ("¿Usuario vs Service Account?", "Usuario = persona; Service Account = identidad para apps y servicios."),
   ("¿Qué contiene un Project?", "Recursos, IAM, facturación, APIs habilitadas y logs."),
 ])),
("m365", "📧 Microsoft 365 y Entra ID", "media-alta",
 EB.B("azul","🧠","M365: servicios", EB.LI([
   "<b>Usuarios, licencias y grupos</b> en el centro de administración.",
   "<b>Exchange Online:</b> buzones · <b>OneDrive:</b> personal · <b>SharePoint:</b> equipo · <b>Teams:</b> colaboración.",
 ])) +
 EB.B("verde","🟢","Entra ID (antes Azure AD)", EB.LI([
   "<b>Identidades, MFA y acceso condicional</b> centralizados.",
   "<b>Roles administrativos</b> con mínimo privilegio.",
   "<b>Auditoría de licenciamiento:</b> quién tiene qué licencia y si la usa.",
 ])) +
 EB.RECALL([
   ("¿OneDrive vs SharePoint?", "OneDrive = archivos personales; SharePoint = archivos del equipo."),
   ("¿Qué es Entra ID?", "Directorio de identidades: usuarios, MFA, acceso condicional y roles."),
 ])),
("hardware", "💻 Hardware y mantenimiento", "alta",
 EB.B("azul","🧠","Componentes", EB.TAB(["Pieza","Falla típica"], [
   ["<b>CPU / RAM</b>","Lentitud, pantallazos, congelamientos"],
   ["<b>SSD / HDD / NVMe</b>","Disco al 100%, arranque lento, ruidos en HDD"],
   ["<b>PSU</b>","No enciende o se apaga solo"],
   ["<b>GPU</b>","Sin video o artefactos"],
   ["<b>Motherboard / BIOS-UEFI</b>","No POST, fecha perdida, no detecta disco"],
 ])) +
 EB.B("verde","🟢","Diagnóstico exprés", EB.TAB(["Síntoma","Primera prueba"], [
   ["No enciende","PSU, cable, reseat de RAM"],
   ["No da video","GPU/RAM, monitor y cable"],
   ["Lentitud","Task Manager: disco/CPU/RAM; salud del SSD"],
   ["Disco al 100%","Procesos, antivirus, inicio, salud SMART"],
   ["Sobrecalentamiento","Ventiladores, polvo, pasta térmica"],
   ["Windows no inicia","Modo seguro, reparación de inicio"],
   ["Impresora","Cola, driver, red vs USB"],
 ])) +
 EB.RECALL([
   ("¿Disco al 100%?", "Ver proceso en Task Manager, salud SMART, antivirus y programas de inicio."),
 ])),
]
# ============ CONTENIDO: PREGUNTAS DEL EXAMEN ============
# (id, tema_ancla, tema_label, enunciado, opciones[4], indice_correcta, justificacion_html)
PREGUNTAS = [
("p01","redes","Redes",
 "¿Qué diferencia hay entre una dirección IP y una dirección MAC?",
 ["IP identifica físicamente el adaptador; MAC es lógica y cambia.",
  "IP es lógica y cambia según la red; MAC es física y única del adaptador.",
  "Son lo mismo, usadas indistintamente.",
  "IP es única de fábrica; MAC es asignada por DHCP."], 1,
 EB.B("azul","🧠","IP vs MAC",
   "<p><b>IP</b> = dirección lógica que puede cambiar y localiza al equipo en la red. <b>MAC</b> = dirección física única que viene de fábrica y identifica el adaptador.</p>")),
("p02","redes","Redes",
 "Un equipo muestra IP 169.254.100.23. ¿Qué indica?",
 ["No obtuvo IP de DHCP (APIPA).","El DNS no resuelve.",
  "El gateway está caído.","El equipo está en otra VLAN."], 0,
 EB.B("naranja","🛠️","APIPA",
   "<p>El rango <code>169.254.x.x</code> lo asigna el propio sistema (<b>APIPA</b>) cuando no recibe respuesta del servidor DHCP.</p>")),
("p03","redes","Redes",
 "¿Cuál es la cadena correcta para diagnosticar 'no tengo Internet'?",
 ["nslookup → ping 8.8.8.8 → ipconfig",
  "ipconfig → ping gateway → ping 8.8.8.8 → nslookup",
  "ping 8.8.8.8 → nslookup → ipconfig",
  "route print → ping → nslookup"], 1,
 EB.B("mapa","🗺️","Cadena",
   "<p>1) ipconfig (¿IP válida?) 2) ping gateway (¿LAN?) 3) ping 8.8.8.8 (¿Internet?) 4) nslookup (¿DNS?). El paso que falla revela el punto exacto.</p>")),
("p04","ciberseguridad","Ciberseguridad",
 "¿Qué garantiza la <b>confidencialidad</b> en la tríada CIA?",
 ["Que los datos no sean alterados.","Que el sistema esté disponible 24/7.",
  "Que solo quienes deben, puedan acceder.","Que se registre todo en auditoría."], 2,
 EB.B("azul","🧠","CIA",
   "<p><b>Confidencialidad</b> = acceso solo para quien debe (cifrado, permisos). Integridad = no alteración. Disponibilidad = que esté cuando se necesita.</p>")),
("p05","ciberseguridad","Ciberseguridad",
 "Riesgo = ?",
 ["Amenaza + Vulnerabilidad","Amenaza × Vulnerabilidad × Impacto",
  "Impacto − Controles","Vulnerabilidad × Exploit"], 1,
 EB.B("naranja","🛠️","Fórmula de riesgo",
   "<p><b>Riesgo = Amenaza × Vulnerabilidad × Impacto</b>. Para reducirlo: bajar vulnerabilidades (parches) o impacto (backups).</p>")),
("p06","ciberseguridad","Ciberseguridad",
 "Un EDR se diferencia de un antivirus tradicional porque…",
 ["Detecta solo virus conocidos por firma.",
  "Analiza comportamiento en el endpoint y puede responder (aislar, matar proceso).",
  "Solo protege el correo.",
  "Reemplaza al firewall de red."], 1,
 EB.B("verde","🟢","EDR",
   "<p>El EDR observa <b>comportamiento</b>, detecta anomalías (incluido malware sin archivos) y <b>responde</b>: aísla el equipo, mata procesos, revierte cambios.</p>")),
("p07","iam","IAM",
 "Un usuario introduce su contraseña correcta y el sistema le responde «acceso denegado». ¿Qué ocurrió?",
 ["Falló la autenticación.","El servidor DNS no resolvió.",
  "Autenticó correctamente pero no está autorizado para el recurso.",
  "El sistema caducó la contraseña."], 2,
 EB.B("rojo","⚠️","Trampa clásica",
   "<p><b>Autenticación = quién eres</b> (validó la credencial ✓). <b>Autorización = qué puedes hacer</b> (carece de permiso sobre ese recurso).</p>")),
("p08","iam","IAM",
 "¿Qué caracteriza al control de acceso RBAC?",
 ["Los permisos se conceden por atributos del contexto.",
  "Los permisos se asignan al rol que ocupa la persona.",
  "Cada usuario define sus propios permisos.",
  "Los permisos se basan solo en la hora de acceso."], 1,
 EB.B("azul","🧠","RBAC vs ABAC",
   "<p><b>RBAC</b> = acceso por rol (Admin, Soporte…). <b>ABAC</b> = acceso por atributos (usuario, recurso, contexto/hora/ubicación).</p>")),
("p09","sql","SQL",
 "¿Qué devuelve un INNER JOIN entre clientes y pedidos?",
 ["Todos los clientes, tengan o no pedidos.",
  "Solo las filas con coincidencia en ambas tablas.",
  "Solo los clientes sin pedidos.",
  "La unión completa de ambas tablas."], 1,
 EB.B("naranja","🛠️","JOINs",
   "<p><b>INNER</b> = solo coincidencias. <b>LEFT</b> = todo lo de la izquierda + NULLs donde no coincide. Esa es la diferencia que siempre preguntan.</p>")),
("p10","sql","SQL",
 "¿WHERE o HAVING?",
 ["WHERE filtra grupos después de GROUP BY.",
  "HAVING filtra filas antes de agrupar.",
  "WHERE filtra filas; HAVING filtra grupos (permite agregados).",
  "Son intercambiables."], 2,
 EB.B("rojo","⚠️","Trampa SQL",
   "<p><code>WHERE</code> filtra <b>filas</b> antes de agrupar; <code>HAVING</code> filtra <b>grupos</b> tras <code>GROUP BY</code>, permitiendo agregados (<code>COUNT(*)</code>).</p>")),
("p11","ia","IA",
 "¿Qué es RAG?",
 ["Un modelo que entrena con tus datos.",
  "Recuperación + generación: el modelo busca documentos relevantes y responde con esa base.",
  "Una base de datos vectorial.",
  "Un agente que ejecuta código."], 1,
 EB.B("naranja","🛠️","RAG",
   "<p><b>Retrieval-Augmented Generation:</b> convierte documentos en embeddings, recupera los más relevantes y el LLM genera la respuesta apoyándose en ellos → menos alucinaciones, info actualizada.</p>")),
("p12","ia","IA",
 "¿Qué diferencia a un agente de IA de un chatbot?",
 ["El agente genera imágenes.",
  "El agente ejecuta acciones con herramientas (tool calling, APIs).",
  "El chatbot usa modelos más grandes.",
  "No hay diferencia."], 1,
 EB.B("mapa","🗺️","Chatbot vs Agente",
  "<p>El <b>agente</b> ademas de conversar <b>actua</b>: llama herramientas, consulta APIs, escribe archivos y automatiza flujos.</p>")),
("p13","soporte","Soporte",
 "¿Cuál es tu metodología para resolver un incidente?",
 ["Improvisar según el caso","Identificar, reproducir, aislar, diagnosticar, solucionar, validar y documentar","Reiniciar siempre primero","Escalar todo de inmediato"],
 1, "🔵 <b>Metodología de 7 pasos</b> 🟢 Orden defendible de principio a fin ⚠️ <i>Trampa: 'reiniciar primero' no es metodología.</i>"),
("p14","soporte","Soporte",
 "¿Cómo priorizas tickets?",
 ["Por orden de llegada","Por impacto + urgencia + usuarios + criticidad + SLA","Solo por severidad","Por antigüedad del usuario"],
 1, "🔵 <b>Prioridad multifactor</b> 🟢 Impacto, urgencia, usuarios, criticidad y SLA ⚠️ <i>Trampa: FIFO ignora el impacto.</i>"),
("p15","soporte","Soporte",
 "Un equipo no enciende. ¿Primera prueba?",
 ["Reinstalar Windows","Verificar PSU, cable y reseat de RAM","Cambiar el disco","Actualizar drivers"],
 1, "🔵 <b>Sin energía = PSU y conexiones</b> 🟢 Cable, fuente, RAM reseat ⚠️ <i>Trampa: reinstalar sin energía no tiene sentido.</i>"),
("p16","redes","Redes",
 "¿Qué es DNS?",
 ["Protocolo que asigna IPs","Servicio que traduce nombres a IP","Dispositivo que filtra tráfico","Tipo de cableado"],
 1, "🔵 <b>DNS = nombres a IP</b> 🟢 Diagnóstico con <code>nslookup</code> ⚠️ <i>Trampa: confundirlo con DHCP.</i>"),
("p17","redes","Redes",
 "¿Switch vs router?",
 ["Son lo mismo","Switch conecta en LAN; router une redes y enruta","Router solo da Wi-Fi","Switch asigna IPs"],
 1, "🔵 <b>Switch = LAN; router = entre redes</b> 🟢 Router decide rutas y NAT ⚠️ <i>Trampa: 'solo Wi-Fi' es falso.</i>"),
("p18","redes","Redes",
 "¿Qué es una VLAN?",
 ["Una VPN","Segmentación lógica de la red física","Un tipo de cable","Un servidor DNS"],
 1, "🔵 <b>VLAN = LAN virtual</b> 🟢 Separa tráfico sin cableado extra ⚠️ <i>Trampa: no es una VPN.</i>"),
("p19","ciberseguridad","Ciberseguridad",
 "¿Qué es la tríada CIA?",
 ["Un antivirus","Confidencialidad, integridad y disponibilidad","Un tipo de firewall","Un protocolo de red"],
 1, "🔵 <b>CIA = base de la seguridad</b> 🟢 Cifrado, hashes y backups la sostienen ⚠️ <i>Trampa: no es un producto.</i>"),
("p20","ciberseguridad","Ciberseguridad",
 "¿Qué es phishing?",
 ["Virus que cifra archivos","Engaño para robar credenciales con páginas falsas","Ataque de fuerza bruta","Error de configuración"],
 1,
 EB.B("azul","🧠","Phishing",
  "<p><b>Phishing = engaño.</b> Verifica remitente y URL.</p>")),
("p21","iam","IAM",
 "¿Qué es MFA?",
 ["Una contraseña larga","Verificación con 2+ factores: saber, tener y ser","Un tipo de firewall","Un rol de GCP"],
 1, "🔵 <b>MFA = múltiples factores</b> 🟢 Frena phishing y stuffing ⚠️ <i>Trampa: no es solo contraseña.</i>"),
("p22","iam","IAM",
 "¿Qué es mínimo privilegio?",
 ["Dar acceso total","Dar solo los permisos necesarios","Bloquear todo acceso","Compartir cuentas"],
 1, "🔵 <b>Mínimo privilegio</b> 🟢 Reduce superficie de ataque ⚠️ <i>Trampa: acceso total viola el principio.</i>"),
("p23","workspace-gcp","Workspace-GCP",
 "¿Qué es una Service Account?",
 ["Un usuario persona","Identidad para apps y servicios, no para personas","Un buzón compartido","Una licencia de M365"],
 1, "🔵 <b>SA = identidad de servicio</b> 🟢 La app se autentica contra GCP ⚠️ <i>Trampa: no es un usuario.</i>"),
("p24","workspace-gcp","Workspace-GCP",
 "¿Qué es una VPC?",
 ["Un disco en la nube","Red privada virtual para tus recursos","Un tipo de licencia","Un backup"],
 1, "🔵 <b>VPC = tu red en la nube</b> 🟢 Subredes, rutas y firewall ⚠️ <i>Trampa: no es almacenamiento.</i>"),
("p25","m365","M365",
 "¿OneDrive vs SharePoint?",
 ["Son iguales","OneDrive = personal; SharePoint = equipo","SharePoint = personal","OneDrive = correo"],
 1, "🔵 <b>Personal vs equipo</b> 🟢 OneDrive individual, SharePoint colaborativo ⚠️ <i>Trampa: decir que son iguales.</i>"),
("p26","m365","M365",
 "¿Qué es Entra ID?",
 ["Un antivirus","Directorio de identidades: usuarios, MFA y acceso condicional","Un servidor de archivos","Un lenguaje de consulta"],
 1, "🔵 <b>Entra ID = identidades</b> 🟢 Antes Azure AD ⚠️ <i>Trampa: no es antivirus ni storage.</i>"),
("p27","hardware","Hardware",
 "PC lenta con disco al 100%. ¿Qué haces?",
 ["Cambias la CPU","Task Manager: proceso, antivirus, inicio y salud SMART","Reinstalas drivers de video","Cambias la fuente"],
 1, "🔵 <b>Disco al 100% = proceso o salud</b> 🟢 Task Manager + SMART + inicio ⚠️ <i>Trampa: cambiar CPU sin diagnosticar.</i>"),
("p28","sql","SQL",
 "¿Qué es una Primary Key?",
 ["Un índice cualquiera","Identificador único de cada fila, no nulo","Una tabla temporal","Un backup"],
 1, "🔵 <b>PK = identidad de la fila</b> 🟢 Única y NOT NULL ⚠️ <i>Trampa: no es cualquier índice.</i>"),
("p29","sql","SQL",
 "¿Qué es normalización?",
 ["Hacer backups","Organizar tablas para evitar redundancia","Acelerar la red","Cifrar datos"],
 1, "🔵 <b>Normalizar = sin duplicados</b> 🟢 1FN, 2FN y 3FN ⚠️ <i>Trampa: no es backup ni cifrado.</i>"),
("p30","fullstack","Full-Stack",
 "¿Qué es una API?",
 ["Un lenguaje","Contrato para que dos programas se comuniquen","Una base de datos","Un servidor físico"],
 1, "🔵 <b>API = contrato</b> 🟢 Tu sistema expone CRUD por API ⚠️ <i>Trampa: no es un lenguaje.</i>"),
("p31","fullstack","Full-Stack",
 "¿Qué es CRUD?",
 ["Un framework","Create, Read, Update y Delete vía POST, GET, PUT y DELETE","Un tipo de base de datos","Un protocolo de red"],
 1, "🔵 <b>CRUD = 4 operaciones</b> 🟢 Mapea a verbos HTTP ⚠️ <i>Trampa: no es framework.</i>"),
("p32","fullstack","Full-Stack",
 "¿Imagen vs contenedor en Docker?",
 ["Son iguales","Imagen = plantilla; contenedor = instancia corriendo","Contenedor = plantilla","Imagen = proceso vivo"],
 1, "🔵 <b>Plantilla vs instancia</b> 🟢 build crea, run ejecuta ⚠️ <i>Trampa: invertir los términos.</i>"),
("p33","fullstack","Full-Stack",
 "¿Qué es Git?",
 ["Un servidor","Control de versiones: clone, add, commit, push y pull","Un lenguaje","Una nube"],
 1, "🔵 <b>Git = versiones</b> 🟢 Ramas para no romper main ⚠️ <i>Trampa: no es un servidor.</i>"),
("p34","python-auto","Python",
 "¿Para qué usarías Python en soporte TI?",
 ["Diseñar logos","Automatizar altas, reportes, logs y respaldos","Editar video","Jugar"],
 1, "🔵 <b>Python = automatización</b> 🟢 CSV, requests y pandas ⚠️ <i>Trampa: usos fuera de TI.</i>"),
("p35","ia","IA",
 "¿Qué es RAG?",
 ["Un robot","El modelo consulta tus documentos antes de responder","Un lenguaje","Un antivirus"],
 1, "🔵 <b>RAG = grounding</b> 🟢 Reduce alucinaciones ⚠️ <i>Trampa: no es un robot físico.</i>"),
("p36","ia","IA",
 "¿Chatbot vs agente de IA?",
 ["Son iguales","Chatbot responde; agente actúa con herramientas","Agente solo chatea","Chatbot ejecuta tareas"],
 1, "🔵 <b>Responder vs actuar</b> 🟢 Agente = LLM + herramientas + memoria ⚠️ <i>Trampa: decir que son iguales.</i>"),
("p37","iso-gestion","ISO-Gestión",
 "¿Qué es ISO 27001 en 1 frase?",
 ["Un antivirus","Norma de SGSI para proteger confidencialidad, integridad y disponibilidad","Un lenguaje SQL","Un switch"],
 1, "🔵 <b>ISO 27001 = SGSI</b> 🟢 Anexo A con controles ⚠️ <i>Trampa: no es un producto.</i>"),
("p38","iso-gestion","ISO-Gestión",
 "¿Qué significa PAR-hT?",
 ["Un protocolo de red","Problema, Acción, Resultado, Herramientas y Aprendizaje","Un tipo de ticket","Un comando"],
 1, "🔵 <b>PAR-hT = estructura de respuesta</b> 🟢 Úsala en cada ejemplo de 60 a 90 segundos ⚠️ <i>Trampa: no es protocolo ni comando.</i>"),
]
# ============ ENSAMBLADO HTML ============

PRIO = {"alta": "prio-alta", "media-alta": "prio-media", "media": "prio-media", "baja": "prio-baja"}
PRIO_TXT = {"alta": "🔴 Prioridad alta", "media-alta": "🟠 Media-alta", "media": "🟡 Media", "baja": "🔵 Baja"}

def build_toc():
    out = ['<div class="toc">']
    for i, (slug, titulo, _, _) in enumerate(TEMAS, 1):
        out.append(f'<a href="#tema-{slug}"><span class="n">{i}</span>{titulo}</a>')
    out.append('</div>')
    return "".join(out)

def build_guia():
    parts = ['<div id="vista-guia">']
    parts.append(EB.HERO("🎓 Guía Visual — Entrevista Técnica",
        "Soporte TI · Redes · Ciberseguridad · IAM · SQL · IA — navega por tema o ve directo al examen"))
    parts.append(build_toc())
    for i, (slug, titulo, prio, html) in enumerate(TEMAS, 1):
        parts.append(f'<h2 id="tema-{slug}">📌 {i}. {titulo}')
        parts.append(f'<span class="badge {PRIO[prio]}">{PRIO_TXT[prio]}</span></h2>')
        parts.append(html)
    parts.append('<div class="bloque b-recall"><h3>🚀 Siguiente paso</h3>'
                 '<p>Cuando termines de repasar, ve a <b>📝 Examen</b> en el menú superior y comprueba tu dominio por tema. '
                 'Los temas &lt;60% aparecerán como <b>a repasar</b> con enlace directo a esta guía.</p></div>')
    parts.append('</div>')
    return "".join(parts)

def build_examen():
    parts = ['<div id="vista-examen">']
    parts.append(EB.HERO("📝 Examen — Entrevista Técnica",
        "Cada pregunta se corrige AL MOMENTO · tu progreso se guarda automáticamente (localStorage)"))
    parts.append('<div class="ex-intro">'
                 '<b>Instrucciones:</b> responde cada pregunta; al elegir una opción verás al instante si es correcta y la explicación. '
                 'Puedes cerrar la pestaña y volver: tu progreso se conserva. Al responder todas, pulsa <b>✓ Ver resultados</b>.</div>')
    for n, (qid, tema_slug, tema_label, txt, opts, _ans, just) in enumerate(PREGUNTAS, 1):
        parts.append(f'<div class="pregunta" id="cont-{qid}">')
        parts.append(f'<p><span class="pnum">{n}</span><span class="ptema">{tema_label}</span></p>')
        parts.append(f'<p class="qtext">{txt}</p>')
        parts.append('<div class="opciones">')
        for i, o in enumerate(opts):
            parts.append(f'<label class="opcion"><input type="radio" name="{qid}" value="{i}"> <span>{chr(65+i)}) {o}</span></label>')
        parts.append('</div>')
        parts.append(f'<div class="ex-feedback" id="fb-{qid}"></div>')
        parts.append('</div>')
    parts.append(f'<div class="res-panel" id="res-panel">')
    parts.append('<h3>📊 Resultado final</h3>')
    parts.append('<div class="res-global" id="res-global">--</div>')
    parts.append('<div class="res-detalle" id="res-detalle"></div>')
    parts.append('<div class="res-msg" id="res-msg"></div>')
    parts.append('<div id="res-temas"></div>')
    parts.append('<div class="res-repasar" id="res-repasar" style="display:none"></div>')
    parts.append('<div class="res-botones">'
                 '<button onclick="examenV2.mostrarResultados()">📊 Ver resultados</button> '
                 '<button class="reintentar" onclick="examenV2.reintentar()">🔄 Reintentar examen</button></div>')
    parts.append('</div>')
    parts.append('</div>')
    return "".join(parts)

def build_barra():
    return ('<div class="ex-bar">'
            '<span>Progreso: <strong id="prog" style="color:#4ade80">0</strong>/'
            f'{len(PREGUNTAS)}</span>'
            '<div class="bar-wrap"><div class="bar-fill" id="bar-fill" style="width:0%"></div></div>'
            '<button class="ver-resultados" id="btn-resultados" onclick="examenV2.mostrarResultados()">✓ Ver resultados</button>'
            '</div>')
MOTOR_JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "examen_v2.js"), encoding="utf-8").read()

def build_js():
    # Inyectar ID y PREGUNTAS en el motor
    js = MOTOR_JS.replace("var ID = 'EXAMEN_ID';",
                          "var ID = '" + EXAMEN_ID + "';")
    preg_json = []
    for qid, tema_slug, tema_label, txt, opts, ans, just in PREGUNTAS:
        preg_json.append({
            "id": qid, "slug": tema_slug, "tema": tema_label, "txt": txt,
            "opts": opts, "ans": ans, "justHTML": just,
        })
    js = js.replace("var PREGUNTAS = [];", "var PREGUNTAS = " +
                    json.dumps(preg_json, ensure_ascii=False) + ";")
    return js


def build_modo():
    return ('<div class="modo">'
            '<button id="btn-guia" class="activo" onclick="verGuia()">GUIA</button>'
            '<button id="btn-examen" onclick="verExamen()">EXAMEN</button>'
            '<span style="color:#64748b;font-size:.8em;margin-left:10px">El progreso del examen se guarda automaticamente</span></div>')

def build_toggle_js():
    return """
<script>
function verGuia(){
  document.getElementById('vista-guia').style.display='block';
  document.getElementById('vista-examen').style.display='none';
  document.getElementById('btn-guia').classList.add('activo');
  document.getElementById('btn-examen').classList.remove('activo');
  window.scrollTo(0,0);
}
function verExamen(){
  document.getElementById('vista-guia').style.display='none';
  document.getElementById('vista-examen').style.display='block';
  document.getElementById('btn-examen').classList.add('activo');
  document.getElementById('btn-guia').classList.remove('activo');
  window.scrollTo(0,0);
}
document.addEventListener('DOMContentLoaded',
  function(){ verGuia(); });
</script>
"""

def build_html():
    parts = ["<!DOCTYPE html>\n<html lang='es'>\n<head>\n<meta charset='utf-8'>\n",
             "<meta name='viewport' content='width=device-width, initial-scale=1'>\n",
             "<title>Guía + Examen — Entrevista Técnica</title>\n",
             "<style>", EB.CSS, "</style>\n</head>\n<body>\n<div class='wrap'>\n"]
    parts.append(build_modo())
    parts.append(build_guia())
    parts.append(build_examen())
    parts.append(build_barra())
    parts.append(build_toggle_js())
    parts.append("<script>" + build_js() + "</script>")
    parts.append("<div class='foot'>🎓 Generado por ParetoTutor Visual v2 · Guía + Examen en un solo archivo · 100% offline e imprimible a PDF</div>")
    parts.append("</div>\n</body>\n</html>\n")
    return "\n".join(parts)

def main():
    html = build_html()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("OK:", OUT)
    print("Tamaño KB:", round(os.path.getsize(OUT) / 1024, 1))
    print("Temas:", len(TEMAS), "| Preguntas:", len(PREGUNTAS))
    print("Cierra </html>:", html.rstrip().endswith("</html>"))
    print("localStorage presente:", "localStorage" in html)

if __name__ == "__main__":
    main()# ============ ENSAMBLADO HTML ============
