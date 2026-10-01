# -*- coding: utf-8 -*-
r"""
Generador: Guia_Visual_Entrevista_Tecnica.html
ParetoTutor Visual - Estilo: fondo #0F172A, bloques 3 capas (2.2)
Basado en: Guia_Entrevista_Tecnica_Christian_Garcia.pdf (05 págs.)
Salida:   Directorio 'Guias terminadas'.
"""
import os

OUT = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Guia_Visual_Entrevista_Tecnica.html"

CSS = """
:root{--azul:#38bdf8;--rojo:#ef4444;--verde:#22c55e;--naranja:#f59e0b;--morado:#6366f1}
*{box-sizing:border-box}
body{background:#0F172A;color:#e2e8f0;font-family:'Segoe UI',Calibri,Arial,sans-serif;margin:0;padding:22px;line-height:1.45}
.wrap{max-width:1050px;margin:0 auto}
h1{font-size:1.9em;color:#f8fafc;letter-spacing:.4px;text-align:center}
.sub{text-align:center;color:#94a3b8;font-size:.95em}
h2{font-size:1.35em;color:#f1f5f9;border-bottom:2px solid #475569;padding-bottom:4px;margin-top:26px}
h3{font-size:1.12em;color:#e2e8f0}
.badge{display:inline-block;background:#1e293b;color:#94a3b8;border:1px solid #475569;border-radius:6px;padding:1px 9px;font-size:.78em;margin:0 3px}
table{border-collapse:collapse;width:100%;font-size:.92em;margin:6px 0}
th,td{border:1px solid #475569;padding:6px 8px;text-align:left}
th{background:#1e293b;color:#cbd5e1}
.toc{background:#1e293b;border:2px solid #475569;border-radius:10px;color:#cbd5e1;padding:12px 16px;column-count:2;column-gap:28px}
.toc a{color:#7dd3fc;text-decoration:none}
.toc a:hover{text-decoration:underline}
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
table.a{background:#1e293b}
table.a th{background:#334155;color:#f1f5f9}
.nav{background:#0f1729;border:2px solid #6366f1;border-radius:10px;color:#e0e0ff;padding:8px;font-size:.9em;text-align:center;position:sticky;top:0;z-index:9}
.nav a{color:#a5b4fc;text-decoration:none;margin:0 3px}
.cmd{display:block;background:#0d1b2e;border:1px solid #475569;color:#7dd3fc;padding:4px 10px;border-radius:6px;font-family:Consolas,monospace;font-size:.88em;margin:2px 0;white-space:pre-wrap}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
details{background:#0f1729;border:1px solid #6366f1;border-radius:8px;margin:5px 0;padding:7px}
summary{color:#a5b4fc;font-weight:bold;cursor:pointer}
.foot{text-align:center;color:#64748b;font-size:.8em;margin-top:18px}
blockquote{background:#0f1729;border-left:4px solid #f59e0b;color:#fef3c7;padding:6px 12px;margin:6px 0}
.kbd{background:#1e293b;color:#38bdf8;border:1px solid #38bdf8;border-radius:4px;padding:0 6px;font-family:Consolas,monospace}
@media print{body{zoom:.92}}
"""

def H2(uid, icono, titulo):
    return f'<h2 id="{uid}">{icono} {titulo}</h2>'

def B(estilo, emoji, titulo, html_cuerpo):
    return (f'<div class="bloque b-{estilo}"><h3>{emoji} {titulo}</h3>{html_cuerpo}</div>')

def lista_items(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def tab(cab, filas, extra=""):
    ths = "".join(f"<th>{c}</th>" for c in cab)
    trs = ""
    for f in filas:
        tds = "".join(f"<td>{c}</td>" for c in f)
        trs += f"<tr>{tds}</tr>"
    return f'<table class="{extra}"><tr>{ths}</tr>{trs}</table>'

secciones = []

secciones.append("""
<div class="wrap">

<h1>🎓 GUÍA VISUAL: ENTREVISTA TÉCNICA</h1>
<p class="sub">Soporte TI · Infraestructura · Ciberseguridad · Automatización — <b style="color:#7dd3fc">Christian Aldair García Ochoa</b> · Guía offline imprimible a PDF</p>

<div class="nav">
📌 <b>Ruta rápida:</b> <a href="#perfil">Perfil</a> · <a href="#arbol">Árbol</a> · <a href="#notacion">Notación</a> · <a href="#soporte">Soporte</a> · <a href="#redes">Redes</a> · <a href="#sec">Ciberseguridad</a> · <a href="#iam">IAM</a> · <a href="#gcp">GCP</a> · <a href="#m365">M365</a> · <a href="#hw">HW</a> · <a href="#sql">SQL</a> · <a href="#py">Python</a> · <a href="#fs">Full-Stack</a> · <a href="#git">Git/Docker</a> · <a href="#ia">IA</a> · <a href="#iso">ISO</a> · <a href="#jira">Jira</a> · <a href="#preguntas">Preguntas</a> · <a href="#prioridad">Prioridad</a> · <a href="#simulacro">Simulacro</a>
</div>
""")

# ---------- ÍNDICE ----------
secciones.append(H2("indice","🗺️","Contenido de la guía") + """
<div class="toc">
<a href="#arbol">1. Árbol de decisión (troubleshooting)</a><br>
<a href="#notacion">2. Tabla de notación y siglas</a><br>
<a href="#perfil">3. Tu experiencia (métricas clave)</a><br>
<a href="#soporte">4. Soporte TI y Troubleshooting</a><br>
<a href="#redes">5. Redes y conectividad</a><br>
<a href="#sec">6. Ciberseguridad</a><br>
<a href="#iam">7. IAM — Identidades y accesos</a><br>
<a href="#gcp">8. Google Workspace y GCP</a><br>
<a href="#m365">9. Microsoft 365</a><br>
<a href="#hw">10. Hardware y mantenimiento</a><br>
<a href="#sql">11. SQL y bases de datos</a><br>
<a href="#py">12. Python, C++ y automatización</a><br>
<a href="#fs">13. Full-Stack y APIs</a><br>
<a href="#git">14. Git y Docker</a><br>
<a href="#ia">15. IA y agentes</a><br>
<a href="#iso">16. ISO 27001</a><br>
<a href="#jira">17. Jira y Monday</a><br>
<a href="#preguntas">18. Preguntas + respuestas modelo</a><br>
<a href="#prioridad">19. Prioridad de estudio</a><br>
<a href="#prep">20. Preparación de respuestas (PAR-hT)</a><br>
<a href="#simulacro">21. 🚨 Simulacro visual de emergencia</a><br>
</div>
""")

# ---------- PERFIL / EXPERIENCIA ----------
secciones.append(H2("perfil","🧠","3. Tu experiencia: lo que DEBES poder explicar") + """
<div class="bloque b-azul"><h3>🧠 Regla de oro de la entrevista</h3>
<p>Por cada tecnología de tu CV debes responder 4 cosas: <b>qué es</b>, <b>para qué sirve</b>, <b>cómo la usaste</b> y <b>qué problema resolviste</b>.</p>
</div>
<div class="bloque b-mapa"><h3>🗺️ Método PAR-hT (tu guion de respuesta)</h3>
<table>
<tr><th>Paso</th><th>Qué incluir</th></tr>
<tr><td><b>Problema</b></td><td>Cuál era la situación, quién la reportaba, por qué era crítica.</td></tr>
<tr><td><b>Acción</b></td><td>Qué hiciste exactamente (qué comandos, herramientas, pasos).</td></tr>
<tr><td><b>Resultado</b></td><td>Dato medible: tiempo, %, tickets, 0 recurrencias.</td></tr>
<tr><td><b>Herramientas</b></td><td>Windows, GCP, Jira, SQL, IA… las que usaste.</td></tr>
<tr><td><b>Aprendizaje</b></td><td>Qué cambiaste para que no vuelva a ocurrir.</td></tr>
</table>
</div>
""")

secciones.append("""<div class="bloque b-verde"><h3>🟢 Ejemplo de respuesta (60-90 seg)</h3>
<p><b>“En DfSoft atendí 278 tickets con 98.6% de efectividad. Por ejemplo, un incidente de accesos (IAM) afectaba a 20 usuarios: detecté que era un problema de <b>deprovisioning</b> incompleto al cambiar de rol. Ejecuté el flujo de altas/bajas, validé con permisos RBAC y documenté el manual. Resultado: resolución el mismo día y 0 recurrencias en los siguientes 3 meses.”</b></p>
</div>
<div class="bloque b-rojo"><h3>⚠️ Trampa de entrevista</h3>
<ul>
<li>❌ Decir que “solucionaste todo” sin datos. <b>Usa número</b>: 278, 98.6%, 66 tickets IAM, 15 manuales, 80% avance.</li>
<li>❌ Atribuirte tecnologías que no puedas explicar con un ejemplo real. Tu CV se audita con preguntas de seguimiento.</li>
<li>✅ Ten listos <b>3 incidentes</b>: uno de soporte, uno de accesos/seguridad, uno de infraestructura/redes.</li>
</ul></div>
""")

# ---------- MÉTRICAS ----------
secciones.append(H2("metricas","📊","Métricas que debes poder defender") + """
<table>
<tr><th>Dato</th><th>Qué significa</th><th>Cómo defenderlo</th></tr>
<tr><td><b>278 tickets</b></td><td>Volumen de incidencias atendidas en soporte TI.</td><td>“Atendía en promedio X tickets/día cubriendo HW, SW, red y accesos.”</td></tr>
<tr><td><b>98.6% efectividad</b></td><td>Resultado documentado de resolución.</td><td>“Resueltos a primera instancia o dentro del SLA tras validar con el usuario.”</td></tr>
<tr><td><b>66 tickets IAM</b></td><td>Accesos, contraseñas y autenticadores.</td><td>“Altas/bajas, reseteo de contraseñas, MFA y permisos.”</td></tr>
<tr><td><b>15 manuales técnicos</b></td><td>Documentación generada con agentes de IA.</td><td>“Guías paso a paso para el equipo: instalación, config y troubleshooting.”</td></tr>
<tr><td><b>80% avance</b></td><td>Política de accesos, matriz y flujos de altas/bajas.</td><td>“Documento la política; falta aprobación final y revisión legal.”</td></tr>
<tr><td><b>Full-Stack</b></td><td>Sistema de inventario y usuarios con arquitectura relacional.</td><td>“Frontend (HTML/CSS/JS) + Backend (API) + Base de datos SQL.”</td></tr>
</table>
""")

# ---------- ÁRBOL DE DECISIÓN ----------
secciones.append(H2("arbol","🌳","1. Árbol de decisión: diagnóstico de un incidente TI") + """
<div class="bloque b-mapa"><h3>🗺️ Flujo de diagnóstico (identificar → reproducir → aislar → diagnosticar → solucionar → validar → documentar)</h3>
<table>
<tr><td>🧩 <b>¿Qué reporta el usuario?</b></td><td>➡️</td><td>🔁 <b>¿Se reproduce?</b></td><td>➡️</td><td>🧪 <b>¿Se aísla?</b></td><td>➡️</td><td>🔍 <b>¿Causa raíz?</b></td><td>➡️</td><td>🛠️ <b>¿Solución?</b></td><td>➡️</td><td>✅ <b>¿Validado?</b></td><td>➡️</td><td>📝 <b>¿Documentado?</b></td></tr>
<tr><td>Escucha y registra</td><td></td><td>Recrea la falla</td><td></td><td>Trocea el sistema</td><td></td><td>Busca en logs</td><td></td><td>Aplica fix</td><td></td><td>Confirma con usuario</td><td></td><td>Manual / ticket</td></tr>
</table>
</div>
""")

secciones.append("""<div class="bloque b-azul"><h3>🧠 Cómo priorizar (impacto × urgencia × alcance)</h3>
<table>
<tr><th>Criterio</th><th>Pregunta clave</th></tr>
<tr><td><b>Impacto</b></td><td>¿Detiene operación crítica o es cosmético?</td></tr>
<tr><td><b>Urgencia</b></td><td>¿Tiene SLA o fecha límite?</td></tr>
<tr><td><b>Usuarios afectados</b></td><td>¿1 persona o 200?</td></tr>
<tr><td><b>Criticidad</b></td><td>¿Área core (ventas, producción) o soporte interno?</td></tr>
<tr><td><b>SLA</b></td><td>¿Cuánto tiempo tenemos contratado para resolver?</td></tr>
</table>
<p class="sub"><b>Fórmula mental:</b> <b style="color:#fef3c7">Prioridad = Impacto + Urgencia + Usuarios + Criticidad − Tiempo transcurrido</b></p>
</div>
<div class="bloque b-naranja"><h3>🛠️ Conceptos que debes dominar de memoria</h3>
<ul>
<li><b>Incidente:</b> interrupción no planificada de un servicio.</li>
<li><b>Solicitud (request):</b> petición de cambio, acceso o información (no es falla).</li>
<li><b>Problema:</b> causa raíz de uno o varios incidentes recurrentes.</li>
<li><b>Escalamiento:</b> pasar el ticket a L2/L3 o a otra área cuando excede tu alcance.</li>
<li><b>SLA:</b> acuerdo de nivel de servicio (tiempo máximo de respuesta o resolución).</li>
<li><b>Resolución:</b> el servicio queda restaurado y validado con el usuario.</li>
</ul>
</div>
""")

# ---------- TABLA DE NOTACIÓN ----------
not_rows = [
["TCP/IP","Protocolo de control de transmisión / Protocolo de Internet","Lenguaje base de las comunicaciones en red."],
["OSI","Modelo de 7 capas de interconexión","Marco para entender/diagnosticar redes por capas."],
["IP","Internet Protocol (IPv4/IPv6)","Dirección lógica que identifica un dispositivo en la red."],
["MAC","Media Access Control","Dirección física única de la tarjeta de red."],
["DHCP","Dynamic Host Configuration Protocol","Asigna IP automáticamente."],
["DNS","Domain Name System","Traduce nombres (google.com) a IP."],
["NAT","Network Address Translation","Traduce IP privadas a públicas para salir a Internet."],
["VLAN","Virtual LAN","Segmenta la red lógicamente aunque esté en el mismo switch."],
["VPN","Virtual Private Network","Túnel cifrado para acceso remoto seguro."],
["LAN/WAN","Red de área local / amplia","LAN = oficina/casa; WAN = Internet/redes amplias."],
["CIDR","Classless Inter-Domain Routing (/24)","Notación para definir subredes y máscaras."],
["HTML/CSS/JS","Markup / estilos / scripting","Trilogía del frontend web."],
["HTTP","HyperText Transfer Protocol","Protocolo de peticiones/respuestas web (GET, POST…)."],
["REST","Representational State Transfer","Estilo arquitectónico de API basado en HTTP."],
["CRUD","Create, Read, Update, Delete","Las 4 operaciones básicas de datos."],
["JSON","JavaScript Object Notation","Formato estándar de intercambio de datos."],
]

not_rows += [
["API","Application Programming Interface","Contrato para que sistemas se comuniquen."],
["SQL","Structured Query Language","Lenguaje para consultar bases de datos relacionales."],
["PK / FK","Primary Key / Foreign Key","Identificador único / referencia a otra tabla."],
["ACID","Atomicity, Consistency, Isolation, Durability","Garantías de las transacciones."],
["RAM/CPU/SSD","Memoria / procesador / almacenamiento","Componentes clave del hardware."],
["BIOS/UEFI","Firmware de arranque","Inicia el hardware y el sistema operativo."],
["IAM","Identity and Access Management","Gestión de identidades y permisos."],
["RBAC","Role-Based Access Control","Permisos por rol."],
["ABAC","Attribute-Based Access Control","Permisos por atributos (contexto, datos…)."],
["MFA","Multi-Factor Authentication","2+ factores para autenticar."],
["SSO","Single Sign-On","1 login para varias aplicaciones."],
["EDR","Endpoint Detection & Response","Detección y respuesta en endpoints."],
["CIA","Confidentiality, Integrity, Availability","Tríada de la seguridad de la información."],
["SLA","Service Level Agreement","Acuerdo de nivel de servicio."],
["GCP","Google Cloud Platform","Plataforma cloud de Google."],
["VPC","Virtual Private Cloud","Red aislada dentro de la nube."],
["VM","Virtual Machine","Computadora emulada en software."],
["LLM","Large Language Model","Modelo grande de lenguaje (IA generativa)."],
["RAG","Retrieval-Augmented Generation","IA + recuperación de documentos para responder con base."],
["Embedding","Vector numérico de texto","Representa significado para búsqueda semántica."],
["Token","Unidad de texto del LLM","En qué se divide la entrada/salida del modelo."],
["SGSI / ISMS","Sistema de Gestión de Seguridad de la Información","Núcleo de ISO 27001."],
]

secciones.append(H2("notacion","🔤","2. Tabla de notación y siglas críticas") + """
<div class="bloque b-azul"><h3>🧠 Glosario exprés de la entrevista</h3>
""" + tab(["Sigla","Significado","Para qué sirve en 1 frase"], not_rows, "a") + """
</div>
""")

# ---------- SOPORTE TI ----------
secciones.append(H2("soporte","🛡️","4. Soporte TI y Troubleshooting (PRIORIDAD 1)"))
secciones.append("""
<div class="bloque b-azul"><h3>🧠 Windows 10/11: áreas que debes dominar</h3>
<ul>
<li><b>Usuarios y permisos:</b> perfiles en <code>C:\\Users</code>, permisos NTFS (lectura/escritura), estándar vs administrador.</li>
<li><b>Servicios:</b> <code>services.msc</code>, iniciar/reiniciar, servicios críticos de terceros.</li>
<li><b>Administrador de dispositivos:</b> drivers con 🔺 amarilla o ❌.</li>
<li><b>Event Viewer:</b> <code>eventvwr.msc</code> → logs de sistema, seguridad, aplicaciones; filtrar por severidad y código.</li>
<li><b>Task Manager / Monitor de recursos:</b> CPU, RAM, disco, red, procesos zombi.</li>
<li><b>Controladores y actualizaciones:</b> Windows Update, drivers del fabricante (SCCM/HP), rollback de drivers.</li>
</ul>
</div>
<div class="bloque b-verde"><h3>🟢 Ejemplo: equipo “lento” (desglose práctico)</h3>
<ul>
<li><b>Paso 1:</b> Abrir Task Manager → pestaña Rendimiento: ¿CPU top, RAM al 100%, disco?.</li>
<li><b>Paso 2:</b> Ordenar procesos por % de uso → identificar el responsable (navegador, indexador, actualizador).</li>
<li><b>Paso 3:</b> Comprobar disco al 100% (HDD saturado, OneDrive sincronizando, virus) e inicio de Windows.</li>
<li><b>Paso 4:</b> Kill/actualizar/quitar del inicio el proceso; limpiar temporales; validar velocidad.</li>
<li><b>Solución típica:</b> actualizar controladores, ampliar RAM, o cambiar HDD→SSD si es HW antiguo.</li>
</ul>
</div>
<div class="bloque b-rojo"><h3>⚠️ Trampas frecuentes del examen</h3>
<ul>
<li>❌ Confundir <b>usuario estándar</b> con <b>administrador</b>: el estándar no puede instalar sin contraseña de admin.</li>
<li>❌ Reiniciar el servicio sin <b>documentar</b> ni verificar que el servicio realmente quedó activo.</li>
<li>❌ No separar <b>hardware vs software</b>: un BSOD puede ser driver, RAM defectuosa o disco dañado → aísla con diagnóstico.</li>
</ul>
</div>
""")

# ---------- REDES ----------
secciones.append(H2("redes","🌐","5. Redes y conectividad (PRIORIDAD 2)"))
secciones.append("""
<div class="bloque b-azul"><h3>🧠 Conceptos que SIEMPRE preguntan</h3>
<ul>
<li><b>IP vs MAC:</b> IP es dirección <b>lógica</b> (cambia, identifica en la red), MAC es <b>física</b> (única, viene de fábrica, identifica el adaptador).</li>
<li><b>IPv4 vs IPv6:</b> IPv4 = 32 bits (192.168.1.1); IPv6 = 128 bits (2001:db8::1), más espacio, autoconfiguración, sin NAT.</li>
<li><b>IP pública vs privada:</b> públicas viajan por Internet; privadas son internas — rangos: <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>.</li>
<li><b>Gateway:</b> puerta de enlace / ruta por defecto → por donde sale todo lo que no es de la red local.</li>
<li><b>NAT:</b> traduce IP privada → pública para que muchos equipos compartan una salida.</li>
<li><b>DHCP:</b> asigna IP automáticamente (DORA: Discover, Offer, Request, Ack).</li>
<li><b>DNS:</b> resuelve nombres a IP; si falla DNS “tienes Internet pero no navegas”.</li>
<li><b>ARP:</b> asocia IP ↔ MAC dentro de la LAN (<code>arp -a</code>).</li>
<li><b>VLAN:</b> segmenta la red lógicamente (seguridad y rendimiento) aunque los equipos estén en el mismo switch físico.</li>
<li><b>Switch vs router:</b> switch conmuta dentro de la LAN (MAC); router enruta entre redes (IP) y sale a Internet.</li>
<li><b>Wi-Fi/AP:</b> acceso inalámbrico: SSID, canal, banda 2.4/5 GHz, WPA2/WPA3.</li>
</ul>
</div>
<div class="bloque b-naranja"><h3>🛠️ Comandos Windows de diagnóstico (memoriza)</h3>
<div class="cmd">ipconfig          → IP, máscara, gateway
ipconfig /all     → + MAC, DNS, DHCP lease
ping 8.8.8.8      → ¿hay conectividad? (latencia) — probar IP primero, luego nombre
tracert google.com→ ¿en qué salto se pierde?
nslookup google.com → ¿resuelve DNS? ¿qué IP devuelve?
arp -a            → tabla IP↔MAC local
netstat -ano      → puertos abiertos y conexiones conectadas
route print       → tabla de rutas (gateway por defecto)</div>
</div>
<div class="bloque b-mapa"><h3>🗺️ Flujo de diagnóstico “no tengo Internet”</h3>
<table><tr><th>#</th><th>Prueba</th><th>Si falla →</th></tr>
<tr><td>1</td><td><code>ipconfig</code>: ¿tengo IP válida? (169.254.x.x = no hubo DHCP)</td><td>Red / cable / DHCP</td></tr>
<tr><td>2</td><td><code>ping gateway</code>: ¿llego a la puerta de enlace?</td><td>LAN / switch / cable</td></tr>
<tr><td>3</td><td><code>ping 8.8.8.8</code>: ¿salida a Internet?</td><td>ISP / router / NAT</td></tr>
<tr><td>4</td><td><code>nslookup google.com</code>: ¿resuelve DNS?</td><td>Servidor DNS</td></tr>
<tr><td>5</td><td>Navegador: ¿error de proxy o certificado?</td><td>Proxy / hora / firewall</td></tr>
</table>
</div>
<div class="bloque b-verde"><h3>🟢 Ejemplo respuesta corta</h3>
<p><b>“¿Qué es DNS? Es el ‘directorio telefónico’ de Internet: traduce nombres como google.com a direcciones IP. Cuando un usuario no navega pero sí tiene IP, primero valido <code>nslookup</code>; si no resuelve, el problema es DNS y reviso los servidores configurados.”</b></p>
</div>
<div class="bloque b-rojo"><h3>⚠️ Trampa típica</h3>
<p>❌ Decir que “<code>ping</code> falla = no hay Internet”. No: <code>ping</code> puede fallar porque el firewall icmp bloquea. La cadena completa (IP→gateway→8.8.8.8→DNS) es la que da el veredicto.</p>
</div>
""")

# ---------- CIBERSEGURIDAD ----------
secciones.append(H2("sec","🔐","6. Ciberseguridad (PRIORIDAD 3)") + """
<div class="bloque b-azul"><h3>🧠 Tríada CIA y lenguaje de riesgo</h3>
<table>
<tr><th>Concepto</th><th>Significado</th><th>Ejemplo</th></tr>
<tr><td><b>Confidencialidad</b></td><td>Solo quien debe, accede.</td><td>Cifrado, contraseñas, permisos.</td></tr>
<tr><td><b>Integridad</b></td><td>Los datos no se alteran.</td><td>Hashes, firmas, versionado.</td></tr>
<tr><td><b>Disponibilidad</b></td><td>El servicio está cuando se necesita.</td><td>Backups, alta disponibilidad, DDoS.</td></tr>
</table>
<p><b>Relación clave:</b> Riesgo = Amenaza × Vulnerabilidad × Impacto.<br>
<b>Amenaza:</b> algo que puede causar daño (hacker, malware, error humano). <b>Vulnerabilidad:</b> debilidad que lo permite (parche ausente, mala contraseña). <b>Exploit:</b> código que aprovecha la vulnerabilidad.</p>
</div>
""")

secciones.append("""<div class="bloque b-rojo"><h3>⚠️ Ataques que debes reconocer a la primera</h3>
<ul>
<li><b>Phishing:</b> email/falsa página para robar credenciales (urgente, enlace raro, remitente falso).</li>
<li><b>Ransomware:</b> cifra archivos y pide rescate → la defensa #1 es backups 3-2-1.</li>
<li><b>Brute force:</b> probar contraseñas por fuerza → MFA + políticas de bloqueo.</li>
<li><b>Credential stuffing:</b> usar credenciales filtradas en varios sitios → MFA + gestor de contraseñas.</li>
<li><b>Ingeniería social:</b> manipular a la persona (vishing, pretexting, tailgating) → capacitación.</li>
<li><b>Malware:</b> troyanos, spyware, keyloggers, sin archivos (fileless).</li>
</ul>
</div>
<div class="bloque b-naranja"><h3>🛠️ Estrategias de defensa (memoriza la lista)</h3>
<ul>
<li><b>Mínimo privilegio:</b> dar solo los permisos necesarios por rol y tiempo.</li>
<li><b>Defense in depth:</b> varias capas: firewall + EDR + MFA + segmentación + backups.</li>
<li><b>Hardening:</b> endurecer el sistema: cerrar servicios, puertos y cuentas no usadas.</li>
<li><b>Patching:</b> actualizar a tiempo (los exploits atacan versiones viejas).</li>
<li><b>Firewall:</b> filtra tráfico por reglas (perímetro y host).</li>
<li><b>Antivirus vs EDR:</b> AV detecta por firma; EDR analiza <b>comportamiento</b> en el endpoint, detecta y <b>responde</b> (aislar, matar proceso).</li>
<li><b>Logs y monitoreo:</b> SIEM centraliza eventos y alertas (¿quién accedió, cuándo, desde dónde?).</li>
</ul>
</div>
<div class="bloque b-verde"><h3>🟢 Respuesta modelo</h3>
<p><b>“¿Qué es un EDR? Es una herramienta que monitorea los equipos (endpoints) buscando comportamiento malicioso, no solo firmas conocidas. Detecta, alerta y responde —por ejemplo, aislando el equipo. El antivirus tradicional queda corto contra malware sin archivos.”</b></p>
</div>
""")

# ---------- IAM ----------
secciones.append(H2("iam","🪪","7. IAM — Identidades y accesos (PRIORIDAD 3)") + """
<div class="bloque b-azul"><h3>🧠 La frase que te salva la entrevista</h3>
<blockquote>“<b>Autenticación</b> es verificar <b>quién eres</b>; <b>autorización</b> es decidir <b>qué puedes hacer</b>. La <b>auditoría</b> registra qué hiciste.”</blockquote>
<ul>
<li><b>Identidad:</b> quién es el usuario (cuenta, atributos, grupo).</li>
<li><b>IAM = Identity & Access Management:</b> el conjunto de procesos, políticas y herramientas para gestionar identidades, accesos y su ciclo de vida.</li>
<li><b>Ciclo de vida:</b> altas (provisioning), cambios (rol) y bajas (deprovisioning) — la baja olvidada es una vulnerabilidad clásica.</li>
</ul>
</div>
<div class="bloque b-naranja"><h3>🛠️ Modelos de control de acceso</h3>
<table>
<tr><th>Modelo</th><th>En qué se basa</th><th>Cuándo usarlo</th></tr>
<tr><td><b>RBAC</b></td><td>Rol del usuario (Admin, Soporte, Auditor).</td><td>Organizaciones con puestos definidos; simple y escalable.</td></tr>
<tr><td><b>ABAC</b></td><td>Atributos: usuario + recurso + contexto (hora, ubicación, departamento).</td><td>Acceso dinámico y fino (acceso solo en horario laboral, solo a su sede).</td></tr>
</table>
<p><b>MFA (2FA):</b> algo que sabes (clave) + algo que tienes (app/token) + algo que eres (biometría).<br>
<b>SSO:</b> un solo login abre varias apps (token federado: SAML/OIDC).</p>
</div>
<div class="bloque b-verde"><h3>🟢 Ejemplo con tu experiencia</h3>
<p><b>“En mis 66 tickets de IAM atendía altas, bajas, reseteo de contraseñas y autenticadores MFA. Cuando alguien cambiaba de puesto, ajustaba su rol (RBAC) para aplicar mínimo privilegio.”</b></p>
</div>
<div class="bloque b-rojo"><h3>⚠️ Trampa clásica</h3>
<p>❌ Confundir autenticación y autorización. Pregunta “caza-bobos”: <i>“Un usuario puso su contraseña y el sistema le llama ‘acceso denegado’ ¿es un fallo de autenticación?”</i> → <b>No</b>: autenticó bien, pero <b>no está autorizado</b> para ese recurso.</p>
</div>
""")

# ---------- GCP / WORKSPACE ----------
secciones.append(H2("gcp","☁️","8. Google Workspace y GCP (PRIORIDAD 6)") + """
<div class="bloque b-azul"><h3>🧠 Google Workspace (administración)</h3>
<ul>
<li><b>Usuarios y grupos:</b> cuentas de la organización, grupos de distribución y grupos de seguridad.</li>
<li><b>Roles:</b> superadmin (todo), admin de usuarios, admin de grupos, admin de Drive…</li>
<li><b>Drive y Shared Drives:</b> Drive personal vs Shared Drive (pertenece al equipo, no a la persona — si alguien se va, la info queda).</li>
<li><b>MFA:</b> obligatorio para admins; recomendado para todos.</li>
<li><b>Políticas:</b> contraseñas, suspensión, retención y debiles.</li>
<li><b>Suspensión y licencias:</b> suspender no borra; liberar licencia al dar de baja.</li>
</ul>
</div>
<div class="bloque b-azul"><h3>🧠 GCP (conceptos de nube)</h3>
<ul>
<li><b>Proyecto:</b> el contenedor principal que agrupa recursos, IAM y presupuesto.</li>
<li><b>Recursos:</b> VMs (Compute Engine), almacenamiento (Cloud Storage/GCS), redes (VPC), APIs.</li>
<li><b>IAM en GCP:</b> quién (principal: usuario o Service Account) → qué rol (permisos) → sobre qué recurso.</li>
<li><b>Service Account vs usuario:</b> el SA es identidad <b>no humana</b> para que una app/máquina se autentique y use la API (usar SA dedicado por servicio, mínimo privilegio, rotar llaves).</li>
<li><b>VPC:</b> red virtual aislada con subredes, firewalls y reglas.</li>
<li><b>Cloud Storage:</b> buckets (objetos) con control de acceso por IAM.</li>
<li><b>Logs y APIs:</b> Cloud Logging centraliza; APIs con OAuth/API keys para integrar.</li>
</ul>
</div>
<div class="bloque b-verde"><h3>🟢 Diferencia "usuario vs Service Account" (te la van a pedir)</h3>
<p><b>Usuario</b> = persona con inicio de sesión (contraseña + MFA) que opera la consola.<br>
<b>Service Account</b> = identidad de máquina/aplicación con claves JSON, sin login humano, usada para automatización y APIs. Recomendación: <b>una SA por servicio</b>, con el mínimo rol, y llaves rotadas periódicamente.</p>
</div>
""")

# ---------- M365 ----------
secciones.append(H2("m365","💼","9. Microsoft 365 (PRIORIDAD MEDIA)") + """
<div class="bloque b-azul"><h3>🧠 M365 en 1 minuto</h3>
<ul>
<li><b>Usuarios y licencias:</b> cada usuario tiene asignadas licencias (Exchange, Teams, OneDrive) — auditoría para detectar licencias "fantasma".</li>
<li><b>Exchange Online:</b> correo corporativo, alias, cuotas, reglas.</li>
<li><b>OneDrive:</b> almacenamiento personal, sincronización local.</li>
<li><b>SharePoint:</b> sitios/equipos de documentos → control de versiones y permisos.</li>
<li><b>Teams:</b> canales/equipos (grupos M365 por debajo), llamadas, integraciones.</li>
</ul>
</div>
<div class="bloque b-naranja"><h3>🛠️ Entra ID (Azure AD) — lo que preguntan</h3>
<ul>
<li>Es el <b>directorio de identidades</b> de Microsoft: autentica usuarios y aplicaciones.</li>
<li><b>MFA</b> (políticas condicionales), <b>roles administrativos</b> (Global Admin, User Admin, Group Admin…), <b>auditoría</b> de inicios de sesión y licenciamiento.</li>
<li>Permite <b>SSO</b> entre M365 y apps de terceros vía SAML/OIDC.</li>
</ul>
</div>
<div class="bloque b-rojo"><h3>⚠️ Trampa</h3>
<p>❌ Decir "Exchange" cuando te preguntan por el directorio (eso es <b>Entra ID</b>). Exchange = correo; Entra ID = identidad.</p>
</div>
""")

# ---------- HARDWARE ----------
secciones.append(H2("hw","🖥️","10. Hardware y mantenimiento (PRIORIDAD 4)") + """
<div class="bloque b-azul"><h3>🧠 Componentes: qué hace cada uno</h3>
<table>
<tr><th>Sigla</th><th>Función</th><th>Si falla… síntomas</th></tr>
<tr><td><b>CPU</b></td><td>Procesa instrucciones.</td><td>Lentitud, sobrecalentamiento, PC no inicia.</td></tr>
<tr><td><b>RAM</b></td><td>Memoria temporal de trabajo.</td><td>Congelaciones, BSOD, “memoria insuficiente”.</td></tr>
<tr><td><b>Motherboard</b></td><td>Conecta todos los componentes.</td><td>No da video, no enciende (buscar códigos de pitido/beep).</td></tr>
<tr><td><b>SSD/HDD/NVMe</b></td><td>Almacenamiento.</td><td>Disco 100%, ruidos (HDD), archivos corruptos.</td></tr>
<tr><td><b>GPU</b></td><td>Gráficos.</td><td>Artefactos en pantalla, no da video, pantalla negra.</td></tr>
<tr><td><b>PSU</b></td><td>Fuente de alimentación.</td><td>No enciende, reinicios aleatorios, apagones.</td></tr>
<tr><td><b>BIOS/UEFI</b></td><td>Firmware de arranque.</td><td>No detecta disco de arranque, no inicia.</td></tr>
</table>
</div>
""")

secciones.append("""<div class="bloque b-mapa"><h3>🗺️ Diagnóstico rápido por síntoma</h3>
<table>
<tr><th>Síntoma</th><th>Checar en orden</th></tr>
<tr><td><b>No enciende</b></td><td>1) PSU/cable 2) botón 3) memoria RAM (asentarla) 4) tarjeta de video 5) fuente muerta.</td></tr>
<tr><td><b>No da video</b></td><td>1) cable/monitor 2) GPU 3) RAM (beeps) 4) probar con video integrado.</td></tr>
<tr><td><b>Lentitud</b></td><td>1) Task Manager 2) disco 100% 3) RAM 4) inicio saturado 5) malware.</td></tr>
<tr><td><b>Disco al 100%</b></td><td>1) indexación/OneDrive 2) antivirus escaneando 3) HDD moribundo→SMART.</td></tr>
<tr><td><b>Sobrecalentamiento</b></td><td>1) ventiladores 2) polvo 3) pasta térmica 4) flujo de aire.</td></tr>
<tr><td><b>Windows no inicia</b></td><td>1) disco de arranque en BIOS 2) modo seguro 3) reparar arranque 4) restore.</td></tr>
<tr><td><b>Impresora</b></td><td>1) cola de impresión atascada 2) driver 3) puerto/USB/red 4) atascos de papel/tinta.</td></tr>
</table>
</div>
<div class="bloque b-naranja"><h3>🛠️ Clonación y mantenimiento</h3>
<ul>
<li><b>Clonar disco:</b> HDD→SSD con herramientas de imagen; validar sector por sector; probar arranque antes de dar de baja el original.</li>
<li><b>Backup 3-2-1:</b> 3 copias, 2 medios, 1 fuera del sitio — argumento de seguridad y recuperación.</li>
<li><b>SMART:</b> monitor de salud del disco; revisar en diagnóstico de fallas.</li>
</ul>
</div>
""")

# ---------- SQL ----------
secciones.append(H2("sql","🗃️","11. SQL y bases de datos (PRIORIDAD 5)"))
secciones.append("""
<div class="bloque b-azul"><h3>🧠 Cláusulas SQL que debes escribir sin pensar</h3>
<div class="cmd">SELECT col1, col2      -- qué columnas
FROM tabla              -- de dónde
WHERE condicion         -- filtro de filas
GROUP BY col1           -- agrupar para agregados
HAVING condicion        -- filtro después de agrupar
ORDER BY col1 ASC/DESC  -- ordenar
LIMIT N / TOP N         -- limitar resultados
UNION                  -- combinar consultas (sin duplicados)</div>
</div>
<div class="bloque b-naranja"><h3>🛠️ JOINs en 1 tabla (te la juegan con esto)</h3>
<table>
<tr><th>JOIN</th><th>Qué devuelve</th><th>Cuándo usarlo</th></tr>
<tr><td><b>INNER JOIN</b></td><td>Solo filas con coincidencia en <b>ambas</b> tablas.</td><td>“Dame clientes que SÍ tienen pedidos.”</td></tr>
<tr><td><b>LEFT JOIN</b></td><td>TODAS las filas de la izquierda + coincidencias; si no hay match, NULLs a la derecha.</td><td>“Dame todos los clientes, tengan o no pedidos.”</td></tr>
<tr><td><b>RIGHT JOIN</b></td><td>Espejo del LEFT (todo de la derecha).</td><td>Raro: prefiere LEFT.</td></tr>
</table>
<p><b>Regla mental:</b> LEFT JOIN conserva la tabla "principal" (la de la izquierda en el FROM); INNER solo conserva lo que casa.</p>
</div>
""")

secciones.append("""<div class="bloque b-verde"><h3>🟢 Ejemplo práctico (respuesta de entrevista)</h3>
<p>“Quiero usuarios con su inventario asignado, incluyendo los usuarios sin inventario.”</p>
<div class="cmd">SELECT u.nombre, i.codigo
FROM usuarios u
LEFT JOIN inventario i ON u.id = i.usuario_id
ORDER BY u.nombre;</div>
<p><b>Paso a paso:</b> 1) <code>usuarios</code> es mi tabla base (left) → 2) <code>LEFT JOIN inventario</code> trae el inventario que casa → 3) los que no tienen inventario aparecen con <code>NULL</code> → 4) ordeno.</p>
</div>
<div class="bloque b-azul"><h3>🧠 Claves, índices y diseño</h3>
<ul>
<li><b>Primary Key (PK):</b> identificador único y no nulo de la tabla (<code>id INT PRIMARY KEY</code>).</li>
<li><b>Foreign Key (FK):</b> columna que referencia la PK de otra tabla (integridad referencial).</li>
<li><b>Índice:</b> estructura que acelera las búsquedas (a costa de escritura) → en columnas de WHERE/JOIN frecuentes.</li>
<li><b>Normalización:</b> eliminar redundancia y dependencias anómalas (1FN, 2FN, 3FN: “la clave, toda la clave, y nada más que la clave”).</li>
<li><b>Constraints:</b> NOT NULL, UNIQUE, CHECK, DEFAULT → reglas de integridad en la BD.</li>
<li><b>NULL:</b> ausencia de valor (¡no es 0 ni cadena vacía!).</li>
</ul>
</div>
<div class="bloque b-naranja"><h3>🛠️ Transacciones ACID</h3>
<ul>
<li><b>A</b>tomicidad: todo o nada.</li>
<li><b>C</b>onsistencia: la BD nunca queda en estado inválido.</li>
<li><b>I</b>solación: las transacciones concurrentes no se pisan.</li>
<li><b>D</b>urabilidad: lo confirmado persiste (aunque se caiga el sistema).</li>
</ul>
<p><b>Views:</b> consultas guardadas como "tablas virtuales" (seguridad y reutilización). <b>Stored Procedures:</b> lógica en la BD, reutilizable y parametrizable (reduce SQL injection si se usa correctamente).</p>
</div>
<div class="bloque b-rojo"><h3>⚠️ Trampa clásica</h3>
<p>❌ Confundir <code>WHERE</code> con <code>HAVING</code>. <code>WHERE</code> filtra filas <b>antes</b> de agrupar; <code>HAVING</code> filtra grupos <b>después</b> de <code>GROUP BY</code> (con agregados). Pregunta típica: “clientes con más de 5 pedidos” → <code>HAVING COUNT(*) &gt; 5</code>.</p>
</div>
""")

# ---------- PYTHON / C++ / AUTOMATIZACIÓN ----------
secciones.append(H2("py","🐍","12. Python, C++ y automatización (PRIORIDAD 8)"))
secciones.append("""
<div class="bloque b-azul"><h3>🧠 Python: lo esencial para defender en entrevista</h3>
<ul>
<li><b>Tipos:</b> int, float, str, bool, list, dict, tuple, set, None.</li>
<li><b>Listas:</b> orden, mutables, <code>append()</code>, <code>len()</code>, slicing <code>a[1:3]</code>.</li>
<li><b>Diccionarios:</b> clave:valor, <code>d.get(k)</code>, <code>d.keys()</code>, <code>in</code>.</li>
<li><b>Funciones:</b> <code>def f(a, b=2):</code> return; args/kwargs.</li>
<li><b>Clases:</b> <code>__init__</code>, métodos, atributos, herencia simple.</li>
<li><b>Excepciones:</b> try/except/else/finally, capturar errores sin romper.</li>
<li><b>Módulos y pip:</b> import, <code>pip install</code>, entornos virtuales (<code>venv</code>).</li>
<li><b>Archivos y JSON:</b> open(), json.load/dump, requests para APIs.</li>
</ul>
</div>
<div class="bloque b-mapa"><h3>🗺️ Método de automatización (frase de ejecución)</h3>
<table><tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>
<tr><td>Tarea repetitiva</td><td>➡️ entradas/salidas</td><td>➡️ implementación</td><td>➡️ validación</td><td>➡️ manejo de errores</td><td>➡️ documentación</td></tr></table>
<p><b>Ejemplo a mencionar:</b> “Automaticé el alta de usuarios: leía un CSV, validaba duplicados, creaba la cuenta (API), registraba el resultado y enviaba resumen por correo.”</p>
</div>
<div class="bloque b-azul"><h3>🧠 C++ (nivel medio-bajo, no te atrapes)</h3>
<ul>
<li><b>Punteros vs referencias:</b> puntero = variable que guarda una dirección (<code>*p</code>, <code>&amp;x</code>); referencia = alias inmutable.</li>
<li><b>Clases:</b> encapsulación, <b>herencia</b> y <b>polimorfismo</b> (mismo método, distinto comportamiento).</li>
<li><b>STL:</b> contenedores listos: vector, map, string → menos código, menos bugs.</li>
</ul>
</div>
<div class="bloque b-rojo"><h3>⚠️ Trampa</h3>
<p>❌ Profundizar en C++ si no lo usas a diario: el entrevistador valora que <b>sepas qué es</b> y cuándo elegirlo, no que memorices sintaxis rara. Prioriza Python, SQL y automatización.</p>
</div>
""")

# ---------- FULL-STACK ----------
secciones.append(H2("fs","🧩","13. Full-Stack y APIs (PRIORIDAD 9)") + """
<div class="bloque b-mapa"><h3>🗺️ Flujo que debes dibujar de memoria</h3>
<div class="cmd">Frontend (HTML/CSS/JS)  --HTTP/JSON-->  API / Backend  --SQL-->  Base de datos
       ^                                              |          |
       +--------------------respuesta JSON--------------+          |
                                        (validación, autenticación, errores)</div>
</div>
<div class="bloque b-azul"><h3>🧠 Frontend vs Backend</h3>
<table>
<tr><th></th><th>Frontend</th><th>Backend</th></tr>
<tr><td><b>Qué es</b></td><td>Lo que ve el usuario.</td><td>Lógica, datos y seguridad del servidor.</td></tr>
<tr><td><b>Tecnologías</b></td><td>HTML, CSS, JavaScript, DOM.</td><td>Lenguaje de servidor (Python/Node…), API, SQL.</td></tr>
<tr><td><b>HTTP/JSON</b></td><td>Consume respuestas.</td><td>Publica endpoints.<br></td></tr>
</table>
</div>
<div class="bloque b-naranja"><h3>🛠️ API REST / CRUD</h3>
<ul>
<li><b>API:</b> contrato de comunicación entre sistemas (endpoints + métodos + formato).</li>
<li><b>REST:</b> estilo basado en HTTP: recursos con URL + método (GET, POST, PUT/PATCH, DELETE).</li>
<li><b>CRUD ↔ HTTP:</b> Create=POST · Read=GET · Update=PUT/PATCH · Delete=DELETE.</li>
<li><b>JSON:</b> formato de datos: <code>{"usuario": "cgar", "rol": "admin"}</code>.</li>
<li><b>Prácticas:</b> validar entradas, códigos de estado (<code>200, 400, 401, 403, 404, 500</code>), autenticación/autorización en el backend, nunca confiar en el frontend.</li>
</ul>
</div>
<div class="bloque b-verde"><h3>🟢 Ejemplo (tu sistema Full-Stack)</h3>
<p><b>“Construí un sistema de inventario y usuarios con arquitectura relacional. El frontend en HTML/CSS/JS consume una API REST; el backend valida, autentica y ejecuta SQL (INSERT/SELECT/UPDATE/DELETE) contra la base. Si el usuario no tiene rol, el backend devuelve 403.”</b></p>
</div>
""")

# ---------- GIT / DOCKER ----------
secciones.append(H2("git","📦","14. Git y Docker (PRIORIDAD 7)"))
secciones.append("""
<div class="bloque b-azul"><h3>🧠 Git en un minuto</h3>
<ul>
<li><b>Repositorio:</b> historial de versiones del proyecto.</li>
<li><b>Commit:</b> instantánea guardada con mensaje.</li>
<li><b>Branch:</b> línea paralela de trabajo (main, feature/x).</li>
<li><b>Merge:</b> unir ramas.</li>
<li><b>Pull request:</b> pedir revisión antes de integrar.</li>
<li><b>Conflicto:</b> dos cambios sobre la misma línea → resolverlo manualmente (no regenerar todo).</li>
<li><b>.gitignore:</b> archivos que no se versionan (secrets, node_modules…).</li>
</ul>
</div>
<div class="bloque b-naranja"><h3>🛠️ Comandos (léelos como un flujo)</h3>
<div class="cmd">git clone URL        → traer el repo
git status           → ¿qué cambió?
git add .            → preparar cambios
git commit -m "msg"  → guardar snapshot
git pull             → bajar cambios
git push             → subir cambios
git branch feature/x → crear rama
git checkout -b x    → crear y moverse
git merge rama       → integrar
git log --oneline    → historial</div>
</div>
<div class="bloque b-azul"><h3>🧠 Docker en 1 minuto</h3>
<ul>
<li><b>Imagen = plantilla</b> (código + sistema + dependencias empaquetadas).</li>
<li><b>Contenedor = instancia ejecutable</b> de la imagen (aislada, ligera).</li>
<li><b>Dockerfile:</b> receta para construir la imagen.</li>
<li><b>Registry:</b> almacén de imágenes (Docker Hub).</li>
<li><b>Volumen:</b> persistencia de datos fuera del contenedor.</li>
<li><b>Port mapping:</b> <code>-p 8080:80</code> → expone el puerto interno al host.</li>
</ul>
</div>
<div class="bloque b-verde"><h3>🟢 Flujo de comandos</h3>
<div class="cmd">docker build -t mi-app .   → construir imagen
docker run -d -p 8080:80 mi-app → lanzar contenedor
docker ps                 → contenedores activos
docker stop &lt;id&gt;          → detener
docker exec -it &lt;id&gt; bash → entrar al contenedor</div>
<p><b>Frase clave:</b> “Imagen es la plantilla; el contenedor es la copia en ejecución.”</p>
</div>
<div class="bloque b-rojo"><h3>⚠️ Trampa</h3>
<p>❌ Decir que “Docker es una máquina virtual”. Diferencia: VM virtualiza hardware completo; Docker virtualiza el SO compartiendo el kernel del host → más ligero y rápido.</p>
</div>
""")

# ---------- IA / AGENTES ----------
secciones.append(H2("ia","🤖","15. IA y agentes (PRIORIDAD 11)") + """
<div class="bloque b-azul"><h3>🧠 Conceptos base</h3>
<ul>
<li><b>IA generativa:</b> modelos que crean contenido nuevo (texto, imagen, código).</li>
<li><b>LLM:</b> modelo de lenguaje masivo entrenado con texto (GPT, Claude, Llama).</li>
<li><b>Prompt:</b> instrucción que le das al modelo. <b>Tokens:</b> unidades en las que se divide el texto (aprox. 1 token ≈ 0.75 palabra en inglés). <b>Contexto:</b> ventana de texto que el modelo puede "ver".</li>
</ul>
</div>
<div class="bloque b-mapa"><h3>🗺️ Chatbot vs Agente (la diferencia que debes explicar)</h3>
<table>
<tr><th>Chatbot</th><th>Agente</th></tr>
<tr><td>Responde preguntas con su conocimiento.</td><td>Además <b>ejecuta acciones</b>: llama tools, consulta APIs, modifica archivos, automatiza flujos.</td></tr>
<tr><td>No tiene acceso al exterior.</td><td>Puede usar <b>tool calling</b> (buscar, calcular, escribir) dentro de un flujo.</td></tr>
</table>
<p class="sub">Frase: <b>“El agente es un chatbot con manos y herramientas.”</b></p>
</div>
<div class="bloque b-naranja"><h3>🛠️ RAG y embeddings (tu experiencia con 15 manuales IA)</h3>
<ul>
<li><b>Embedding:</b> convertir texto en un <b>vector numérico</b> que captura su significado.</li>
<li><b>RAG (Retrieval-Augmented Generation):</b> el modelo <b>recupera</b> información de una base/documentos y luego <b>genera</b> la respuesta con esa base → respuestas actuales y <b>con fuente</b>.</li>
<li><b>Por qué importa:</b> reduce <b>alucinaciones</b> (inventos del modelo) y permite usar documentación interna sin reentrenar.</li>
</ul>
</div>
<div class="bloque b-rojo"><h3>⚠️ Alucinaciones y seguridad</h3>
<ul>
<li><b>Alucinación:</b> respuesta falsa dicha con seguridad → siempre <b>validar</b> contra fuente confiable.</li>
<li>Cómo controlarla: prompt con instrucciones, RAG con fuentes citadas, validación automática y revisión humana.</li>
<li><b>Seguridad de la información:</b> no mandar datos personales/sensibles a modelos externos; revisar políticas; logs de uso.</li>
</ul>
</div>
<div class="bloque b-verde"><h3>🟢 Tu anécdota real</h3>
<p><b>“Generé 15 manuales técnicos con agentes de IA: definí el prompt, el agente consultaba la documentación interna y redactaba el manual, y yo validaba cada paso antes de publicarlo. Eso evita manuales inventados.”</b></p>
</div>
""")

# ---------- ISO 27001 ----------
secciones.append(H2("iso","🏛️","16. ISO 27001 (PRIORIDAD 10)") + """
<div class="bloque b-azul"><h3>🧠 Qué es ISO/IEC 27001</h3>
<ul>
<li>Estándar internacional para un <b>SGSI/ISMS</b> (Sistema de Gestión de Seguridad de la Información).</li>
<li>No es solo tecnología: es un <b>sistema de gestión</b> (política, riesgos, personas, procesos, controles y mejora continua).</li>
<li>Versión <b>2022</b>: 4 temas (organizacional, de personas, físicas y tecnológicas) y <b>93 controles</b> en el Anexo A.</li>
<li><b>Enfoque por riesgos:</b> identificas amenazas, valoras impacto, defines controles y medidas.</li>
</ul>
</div>
<div class="bloque b-mapa"><h3>🗺️ Ciclo PDCA (mejora continua)</h3>
<table>
<tr><th>Plan</th><th>Do</th><th>Check</th><th>Act</th></tr>
<tr><td>Política, alcance, evaluación de riesgos, objetivos.</td><td>Implementar controles y procedimientos.</td><td>Auditorías internas, métricas, revisión.</td><td>Acciones correctivas y mejora.</td></tr>
</table>
</div>
<div class="bloque b-naranja"><h3>🛠️ Vocabulario que debes usar</h3>
<ul>
<li><b>SGSI (ISMS):</b> el sistema de gestión de seguridad de la información.</li>
<li><b>Gestión de riesgos:</b> identificar → analizar → evaluar → tratar (mitigar, transferir, aceptar, evitar).</li>
<li><b>Controles:</b> medidas del Anexo A (políticas, control de accesos, cifrado, backups, gestión de incidentes…).</li>
<li><b>Políticas y procedimientos:</b> documentos que dicen el “qué” y el “cómo”.</li>
<li><b>Evidencias:</b> registros que demuestran que se cumple.</li>
<li><b>Auditoría y certificación:</b> externa, periódica; con auditorías internas anuales antes.</li>
<li><b>Declaración de aplicabilidad (SoA):</b> qué controles aplican y por qué.</li>
</ul>
</div>
<div class="bloque b-rojo"><h3>⚠️ La trampa de la honestidad (crítica para ti)</h3>
<p>❌ Afirmar que “implementaste toda la norma”. Lo correcto:</p>
<blockquote>“Apoyé el proceso documental orientado a ISO 27001: redacté la política de accesos (80% de avance), la matriz de roles y los flujos de altas/bajas, alineados con los controles de acceso del Anexo A. La implementación completa es un proyecto de la organización.”</blockquote>
</div>
""")

# ---------- JIRA / MONDAY ----------
secciones.append(H2("jira","📋","17. Jira y Monday (PRIORIDAD MEDIA-BAJA)") + """
<div class="bloque b-azul"><h3>🧠 Vocabulario de ticketing</h3>
<ul>
<li><b>Ticket:</b> registro de una petición o incidencia.</li>
<li><b>Incidente vs request:</b> falla de servicio vs petición de acceso/cambio.</li>
<li><b>Prioridad vs severidad:</b> prioridad = orden de atención (negocio); severidad = gravedad del impacto técnico.</li>
<li><b>SLA:</b> tiempo comprometido de respuesta/resolución.</li>
<li><b>Escalamiento:</b> pasar a otro nivel/área cuando se excede el alcance o SLA.</li>
<li><b>Asignación, estado y resolución:</b> quién lo atiende, en qué etapa va (nuevo→en progreso→resuelto→cerrado) y cómo se cerró (resuelto, duplicado, no aplica).</li>
</ul>
</div>
<div class="bloque b-verde"><h3>🟢 Cómo responder "¿cómo priorizas tickets?"</h3>
<p>“Evalúo 5 factores: <b>impacto</b> (¿detiene producción?), <b>urgencia</b> (¿SLA?), <b>usuarios afectados</b>, <b>criticidad</b> del área y el <b>tiempo transcurrido</b>. Un incidente que apaga cajas con 100 usuarios va antes que una solicitud de permiso.”</p>
</div>
""")

# ---------- PREGUNTAS + RESPUESTAS ----------
secciones.append(H2("preguntas","🎤","18. Preguntas de entrevista con respuestas modelo"))
secciones.append("""
<div class="bloque b-azul"><h3>🧠 Soporte TI — respuestas cortas y seguras</h3>
<table>
<tr><th>Pregunta</th><th>Respuesta modelo (15-25 seg)</th></tr>
<tr><td><b>¿Cuál es tu metodología para resolver un incidente?</b></td><td>“Identificar → reproducir → aislar → diagnosticar → solucionar → validar → documentar. Siempre registro el ticket y confirmo con el usuario al final.”</td></tr>
<tr><td><b>¿Cómo diferencias un problema de hardware de uno de software?</b></td><td>“Pruebo el software primero: modo seguro, drivers, actualizaciones, reinstalación. Si falla incluso en un entorno limpio y reaparece tras cambiar componentes, sospecho hardware. Ejemplo: BSOD que persiste tras reinstalar = probable RAM o disco.”</td></tr>
<tr><td><b>¿Qué es un SLA?</b></td><td>“Acuerdo de nivel de servicio: define tiempos máximos de respuesta y resolución que la empresa se compromete a cumplir con el cliente.”</td></tr>
<tr><td><b>¿Cómo priorizas tickets?</b></td><td>“Por impacto, urgencia, usuarios afectados, criticidad y SLA. Un incidente de caja registradora con 100 usuarios parados gana a una solicitud de permiso.”</td></tr>
<tr><td><b>¿Cuándo escalas un incidente?</b></td><td>“Cuando excede mi alcance técnico, requiero permisos de otro equipo, o riesgo incumplir el SLA. Escalo SIEMPRE con contexto: qué se hizo, qué se probó y qué se necesita.”</td></tr>
</table>
</div>
""")

secciones.append("""
<div class="bloque b-azul"><h3>🧠 Redes — respuestas modelo</h3>
<table>
<tr><th>Pregunta</th><th>Respuesta modelo</th></tr>
<tr><td><b>¿Qué es DNS?</b></td><td>“El directorio telefónico de Internet: traduce nombres (google.com) a direcciones IP. Sin él, tendrías que memorizar IPs.”</td></tr>
<tr><td><b>¿Qué es DHCP?</b></td><td>“Protocolo que asigna IP, máscara, gateway y DNS automáticamente. Proceso DORA: Discover, Offer, Request, Ack. Si un equipo no obtiene DHCP aparece 169.254.x.x.”</td></tr>
<tr><td><b>¿IP vs MAC?</b></td><td>“IP es lógica y cambia (identifica en la red); MAC es física, única y viene de fábrica (identifica el adaptador). ARP las relaciona dentro de la LAN.”</td></tr>
<tr><td><b>¿Qué es un gateway?</b></td><td>“La puerta de enlace o ruta por defecto: por donde sale todo el tráfico que no pertenece a la red local.”</td></tr>
<tr><td><b>¿Qué es NAT?</b></td><td>“Traduce IPs privadas internas a una IP pública de salida. Permite que muchos equipos compartan una sola conexión a Internet.”</td></tr>
<tr><td><b>¿Switch vs router?</b></td><td>“El switch conmuta dentro de la red local (por MAC); el router enruta entre redes (por IP), sale a Internet y hace NAT y firewall básico.”</td></tr>
<tr><td><b>¿Qué es una VLAN?</b></td><td>“Segmentación lógica de una red física: separo departamentos o tipos de tráfico en el mismo switch para seguridad y rendimiento.”</td></tr>
<tr><td><b>¿Cómo diagnosticas que un usuario no tiene Internet?</b></td><td>“Cadena en 5 pasos: 1) ipconfig (¿IP válida?), 2) ping al gateway, 3) ping 8.8.8.8 (salida), 4) nslookup (¿resuelve DNS?), 5) navegador/proxy. El paso que falla indica el punto exacto.”</td></tr>
<tr><td><b>¿IPv4 vs IPv6?</b></td><td>“IPv4: 32 bits, ~4.3 mil millones de direcciones, usamos NAT para sobrevivir. IPv6: 128 bits, cifras enormes, sin necesidad de NAT, autoconfiguración y seguridad mejorada.”</td></tr>
</table>
</div>
""")

secciones.append("""
<div class="bloque b-rojo"><h3>⚠️ Seguridad — respuestas modelo</h3>
<table>
<tr><th>Pregunta</th><th>Respuesta modelo</th></tr>
<tr><td><b>¿Qué es IAM?</b></td><td>“Identity and Access Management: gestionar identidades, autenticación, autorización y auditoría durante todo el ciclo de vida (altas, cambios, bajas, con mínimo privilegio).”</td></tr>
<tr><td><b>¿Autenticación vs autorización?</b></td><td>“Autenticación = quién eres (credenciales); autorización = qué puedes hacer (permisos). Puedo autenticar correctamente y aun así no estar autorizado.”</td></tr>
<tr><td><b>¿Qué es MFA?</b></td><td>“Autenticación multifactor: algo que sabes + algo que tienes y/o algo que eres. Añade una barrera aunque roben la contraseña.”</td></tr>
<tr><td><b>¿Qué es RBAC?</b></td><td>“Control de acceso basado en roles: el permiso se asigna al rol, no a la persona. Ejemplo: rol Auditor solo lectura.”</td></tr>
<tr><td><b>¿Qué es mínimo privilegio?</b></td><td>“Dar solo los permisos necesarios para hacer el trabajo, nada más. Reduce el impacto si la cuenta se compromete o un empleado se va.”</td></tr>
<tr><td><b>¿Qué es una vulnerabilidad?</b></td><td>“Debilidad o fallo del sistema que un atacante podría explotar. Ejemplo: software sin parchear o contraseña débil.”</td></tr>
<tr><td><b>¿Amenaza vs vulnerabilidad?</b></td><td>“La amenaza es quien/qué puede hacer daño (hacker, malware); la vulnerabilidad es la debilidad que lo permite. Riesgo = amenaza × vulnerabilidad × impacto.”</td></tr>
<tr><td><b>¿Qué es un firewall?</b></td><td>“Dispositivo que filtra el tráfico según reglas: permite o bloquea conexiones por IP, puerto y protocolo. Puede ser de red o de host.”</td></tr>
<tr><td><b>¿Qué es un EDR?</b></td><td>“Detección y respuesta en endpoints: monitorea comportamiento en el equipo, detecta actividad maliciosa (no solo firmas) y responde, p. ej. aislando el equipo.”</td></tr>
<tr><td><b>¿Qué es ISO 27001?</b></td><td>“Estándar internacional de gestión de seguridad de la información (SGSI): política, riesgos, controles, auditoría y mejora continua.”</td></tr>
</table>
</div>
""")

secciones.append("""
<div class="bloque b-azul"><h3>🧠 Cloud / GCP — respuestas modelo</h3>
<table>
<tr><th>Pregunta</th><th>Respuesta modelo</th></tr>
<tr><td><b>¿Qué es GCP?</b></td><td>“Google Cloud Platform: plataforma cloud de Google con cómputo (Compute Engine), almacenamiento (Cloud Storage), redes (VPC) y servicios de datos/IA, gestionados por proyectos e IAM.”</td></tr>
<tr><td><b>¿IAM en GCP?</b></td><td>“Define quién (usuario o Service Account) puede hacer qué (rol/permisos) sobre qué recurso (proyecto, bucket, VM). Se asignan roles predefinidos o personalizados.”</td></tr>
<tr><td><b>¿Qué es una Service Account?</b></td><td>“Identidad no humana usada por aplicaciones y servicios para autenticarse contra la API de Google. Se crea una por servicio, con mínimo privilegio y llaves rotadas.”</td></tr>
<tr><td><b>¿Qué es una VPC?</b></td><td>“Red virtual privada dentro de la nube: subredes, firewall, rutas y control de acceso → aislamiento y segmentación de recursos.”</td></tr>
<tr><td><b>¿Recurso vs proyecto?</b></td><td>“El proyecto es el contenedor (agrupa recursos, IAM y presupuesto); el recurso es lo que hay dentro: VMs, buckets, redes, APIs.”</td></tr>
<tr><td><b>¿Usuario vs Service Account?</b></td><td>“El usuario es persona (login + MFA); la Service Account es máquina (clave JSON, sin login) para automatización y APIs.”</td></tr>
</table>
</div>
""")

secciones.append("""
<div class="bloque b-naranja"><h3>🛠️ SQL — respuestas modelo</h3>
<table>
<tr><th>Pregunta</th><th>Respuesta modelo</th></tr>
<tr><td><b>¿Qué es una Primary Key?</b></td><td>“Columna (o conjunto) que identifica de forma única cada fila; no puede ser NULL ni repetirse.”</td></tr>
<tr><td><b>¿Qué es una Foreign Key?</b></td><td>“Columna que referencia la PK de otra tabla; garantiza integridad referencial (no puedes referenciar un id inexistente).”</td></tr>
<tr><td><b>¿INNER JOIN vs LEFT JOIN?</b></td><td>“INNER devuelve solo coincidencias entre ambas; LEFT devuelve todo de la izquierda y rellena con NULL donde no haya match a la derecha.”</td></tr>
<tr><td><b>¿Qué es un índice?</b></td><td>“Estructura que acelera búsquedas y JOINs sobre una columna, a cambio de escritura más lenta y más espacio.”</td></tr>
<tr><td><b>¿Qué es normalización?</b></td><td>“Organizar las tablas para eliminar redundancia y dependencias anómalas. Regla 3FN: la clave, toda la clave y nada más que la clave.”</td></tr>
<tr><td><b>¿Qué es una transacción?</b></td><td>“Conjunto de operaciones que se ejecutan como una unidad: o todas se aplican o ninguna (ACID). Ejemplo: transferencia bancaria.”</td></tr>
</table>
</div>
""")

secciones.append("""
<div class="bloque b-azul"><h3>🧠 Desarrollo — respuestas modelo</h3>
<table>
<tr><th>Pregunta</th><th>Respuesta modelo</th></tr>
<tr><td><b>¿Qué es una API?</b></td><td>“Interfaz que permite que dos sistemas se comuniquen: expone endpoints con reglas claras (qué datos, qué métodos, qué formato).”</td></tr>
<tr><td><b>¿Qué es REST?</b></td><td>“Estilo de API basado en HTTP: recursos identificados por URL y acciones con métodos GET, POST, PUT, DELETE. Sin estado.”</td></tr>
<tr><td><b>¿Qué es CRUD?</b></td><td>“Las 4 operaciones de datos: Create (POST), Read (GET), Update (PUT/PATCH), Delete (DELETE).”</td></tr>
<tr><td><b>¿Qué es JSON?</b></td><td>“Formato ligero de intercambio de datos: pares clave-valor. <code>{"id":1,"nombre":"Ana"}</code>. Es el estándar de las APIs web.”</td></tr>
<tr><td><b>¿Frontend vs backend?</b></td><td>“Frontend: lo que ve y usa el usuario (HTML, CSS, JS). Backend: lógica, datos, seguridad y APIs del servidor.”</td></tr>
<tr><td><b>¿Qué es Git?</b></td><td>“Sistema de control de versiones: historial de cambios, ramas y colaboración sin pisarse el trabajo.”</td></tr>
<tr><td><b>¿Qué es Docker?</b></td><td>“Plataforma de contenedores: empaqueta app + dependencias en una imagen; el contenedor es la instancia en ejecución, portátil y aislada.”</td></tr>
<tr><td><b>¿Imagen vs contenedor?</b></td><td>“Imagen = plantilla (receta con código y dependencias); contenedor = instancia ejecutándose de esa imagen. Puedo tener muchos contenedores de una imagen.”</td></tr>
</table>
</div>
""")

secciones.append("""
<div class="bloque b-verde"><h3>🟢 IA — respuestas modelo</h3>
<table>
<tr><th>Pregunta</th><th>Respuesta modelo</th></tr>
<tr><td><b>¿Qué es un LLM?</b></td><td>“Modelo de lenguaje grande: red neuronal entrenada con enorme cantidad de texto para predecir y generar texto coherente.”</td></tr>
<tr><td><b>¿Qué es un agente de IA?</b></td><td>“Sistema que además de conversar ejecuta acciones: usa herramientas (tool calling), consulta APIs, procesa datos y automatiza flujos.”</td></tr>
<tr><td><b>¿Chatbot vs agente?</b></td><td>“El chatbot responde con su conocimiento; el agente actúa: llama herramientas y ejecuta tareas dentro de un flujo.”</td></tr>
<tr><td><b>¿Qué es RAG?</b></td><td>“Recuperación + generación: el modelo busca documentos relevantes (embeddings) y genera la respuesta apoyándose en ellos. Reduce alucinaciones y usa info actualizada.”</td></tr>
<tr><td><b>¿Qué es un embedding?</b></td><td>“Representación numérica (vector) de un texto que captura su significado; permite búsqueda semántica por similitud.”</td></tr>
<tr><td><b>¿Cómo controlarías respuestas incorrectas?</b></td><td>“Con prompts limitados, RAG con fuentes citadas, validación automática de la salida y revisión humana antes de publicar. Nunca automatizar sin validar.”</td></tr>
</table>
</div>
""")

# ---------- PRIORIDAD DE ESTUDIO ----------
secciones.append(H2("prioridad","🎯","19. Prioridad de estudio (Pareto: Top 20% = 80% del resultado)") + """
<div class="bloque b-naranja"><h3>🛠️ Tabla de prioridades — la lista que debes respetar</h3>
""" + tab(["Nº","Área","Profundidad","Acción concreta"], [
["1","Troubleshooting / Soporte TI","Alta","Memoriza metodología 7 pasos + ejemplos de Windows."],
["2","Redes TCP/IP","Alta","Domina IP/MAC, DNS, DHCP, gateway, NAT y cadena iPhone→DNS."],
["3","IAM / Ciberseguridad","Alta","Frase autenticación vs autorización + MFA/RBAC + tríada CIA."],
["4","Windows / Hardware","Alta","Síntoma → orden de pruebas; clonación y 3-2-1."],
["5","SQL","Media-Alta","Escribe INNER/LEFT JOIN y explica PK/FK/normalización."],
["6","Google Workspace / GCP","Media-Alta","Service Account vs usuario; proyecto vs recurso."],
["7","Git / Docker","Media","Comandos base + imagen vs contenedor."],
["8","Python / Automatización","Media","Método 6 pasos + ejemplo de automatización real."],
["9","Full-Stack","Media","Dibuja flujo Frontend→API→BD; CRUD↔HTTP."],
["10","ISO 27001","Media","SGSI, riesgos, controles y tu rol DOCUMENTAL (no exagerar)."],
["11","IA / Agentes","Media","Chatbot vs agente; RAG y alucinaciones."],
["12","C++","Baja-Media","Solo conceptos: punteros, clases, herencia."],
], "a") + """
</div>
<div class="bloque b-azul"><h3>🧠 La regla Pareto aplicada</h3>
<p>El <b>Top 20%</b> (Soporte, Redes, IAM/Seguridad, Windows/HW) genera el <b>80% de las preguntas</b>. Domínalo primero con ejemplos reales; el resto se estudia en segundo plano.</p>
</div>
""")

# ---------- PREPARACIÓN DE RESPUESTAS ----------
secciones.append(H2("prep","🧰","20. Preparación de respuestas: tu guion de 60-90 seg") + """
<div class="bloque b-recall"><h3>🧠 Los 4 materiales que debes tener listos</h3>
<ul>
<li><b>1) Resumen de tu experiencia en DfSoft</b> (60-90 segundos con PAR-hT).</li>
<li><b>2) Tres incidentes reales:</b> uno de <b>soporte</b>, uno de <b>accesos/seguridad</b> y uno de <b>infraestructura/redes</b> — cada uno con Problema → Acción → Resultado → Herramientas → Aprendizaje.</li>
<li><b>3) Un ejemplo de automatización</b> (script/agente) y <b>4) un ejemplo Full-Stack</b> (sistema inventario).</li>
</ul>
</div>
<div class="bloque b-rojo"><h3>⚠️ Regla de oro final</h3>
<p>❌ <b>No atribuyas a tu experiencia</b> tecnologías o responsabilidades que no puedas respaldar con un ejemplo real. Un “sí, usé Docker” sin saber explicar imagen vs contenedor destruye credibilidad.</p>
</div>
<div class="bloque b-verde"><h3>🟢 Plantilla de incidente (cronómetro 60-90 seg)</h3>
<div class="cmd">P  “En DfSoft reportaron que X dejó de funcionar para N usuarios…”
A  “Reproduje, aislé y encontré que era Y; apliqué Z (comando/proceso)…”
R  “Quedó resuelto en H horas y validé con el usuario; 0 recurrencias en N meses.”
T  “Usé Windows/Event Viewer, Jira, SQL, GCP/IAM…”
h  “Documenté el manual para que no vuelva a pasar y avisé al equipo.”</div>
</div>
""")

# ---------- SIMULACRO ----------
secciones.append(H2("simulacro","🚨","21. Simulacro visual de emergencia") + """
<div class="bloque b-recall"><h3>🧠 Repaso activo — responde ANTES de mirar</h3>
<details><summary>Q1. ¿Qué diferencia a un agente de IA de un chatbot?</summary><p>El agente ejecuta acciones: usa herramientas (tool calling), consulta APIs y automatiza flujos; el chatbot solo conversa con su conocimiento.</p></details>
<details><summary>Q2. ¿INNER JOIN o LEFT JOIN?</summary><p>INNER solo filas que coinciden; LEFT todas las de la izquierda + NULLs donde no coincide.</p></details>
<details><summary>Q3. ¿Autenticación vs autorización?</summary><p>Autenticación = quién eres; autorización = qué puedes hacer.</p></details>
<details><summary>Q4. ¿Qué es una Service Account?</summary><p>Identidad no humana de máquina/app para autenticarse contra la API; mínimo privilegio y llaves rotadas.</p></details>
<details><summary>Q5. ¿Cuál es la primera prueba en "no tengo Internet"?</summary><p>ipconfig: verificar que tengas IP válida (169.254.x.x = falló DHCP).</p></details>
</div>
""")

# ---------- CIERRE ----------
html_out = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guía Visual — Entrevista Técnica (Christian García Ochoa)</title>
<style>""" + CSS + """</style>
</head>
<body>
""" + "\n".join(secciones) + """
<div class="foot">
Guía Visual de Estudio — ParetoTutor Visual · Basada en: <i>Guia_Entrevista_Tecnica_Christian_Garcia.pdf</i> +
información oficial (Google Cloud, Advisera/ISO 27001, Check Point, Okta, IBM, DigitalOcean) · Generado el 23-Sep-2026 ·
Documento 100% offline e imprimible a PDF.
</div>
</div>
</body>
</html>
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html_out)

print("OK generado:", OUT)
print("Tamaño:", os.path.getsize(OUT), "bytes")
print("Bloques div:", html_out.count("<div "))
print("Cierra html:", html_out.rstrip().endswith("</html>"))