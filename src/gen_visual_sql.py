# -*- coding: utf-8 -*-
"""Genera Guia_Visual_SQL.html (modo OSCURO, paleta 3 capas) para el examen de
SQL Server del Sistema Hospitalario."""

OUT = r"C:\Users\theda\OneDrive\Documentos\Agentes\Estudio de examen\Guias terminadas\Guia_Visual_SQL.html"

CSS = """
body{font-family:'Segoe UI',Arial,sans-serif;max-width:960px;margin:20px auto;padding:0 16px;
     color:#E2E8F0;line-height:1.6;background:#0F172A;}
header{background:linear-gradient(135deg,#0C4A6E,#0284C7);color:#fff;border-radius:14px;
     padding:22px;margin-bottom:12px;box-shadow:0 2px 10px rgba(0,0,0,.45);}
header h1{margin:0;font-size:1.9em;} header p{margin:6px 0 0;font-size:1.05em;opacity:.92;}
h2.seccion{color:#60A5FA;margin-top:26px;border-bottom:3px solid #0284C7;padding-bottom:4px;}
h3{margin:14px 0 6px;}
.bloque{border-radius:10px;padding:12px 16px;margin:10px 0;}
.azul{background:rgba(56,189,248,.10);border:2px solid #38bdf8;color:#bae6fd;}
.rojo{background:rgba(248,113,113,.10);border:2px solid #ef4444;color:#fecaca;}
.verde{background:rgba(34,197,94,.10);border:2px solid #22c55e;color:#bbf7d0;}
.naranja{background:rgba(245,158,11,.10);border:2px solid #f59e0b;color:#fef3c7;}
.mapa{background:#1e293b;border:2px dashed #475569;color:#cbd5e1;}
.recall{background:#0f1729;border:2px solid #6366f1;color:#e0e0ff;}
pre{background:#0b1120;border:1px solid #334155;border-radius:8px;padding:12px;overflow-x:auto;
     color:#a5f3fc;font-family:Consolas,'Courier New',monospace;font-size:.92em;}
code{background:#1e293b;color:#7dd3fc;padding:1px 5px;border-radius:5px;font-family:Consolas,monospace;}
pre code{background:none;color:inherit;padding:0;}
table{border-collapse:collapse;margin:10px 0;width:100%;}
th,td{border:1px solid #475569;padding:7px 10px;text-align:left;}
th{background:rgba(100,116,139,.22);color:#fff;}
tr:nth-child(even) td{background:rgba(255,255,255,.03);}
.badge{display:inline-block;background:rgba(255,255,255,.14);padding:2px 10px;border-radius:20px;
     margin-right:6px;font-size:.85em;}
.arbol{background:#1e293b;border:2px dashed #475569;color:#cbd5e1;padding:12px;border-radius:8px;
     font-family:Consolas,monospace;white-space:pre;overflow-x:auto;line-height:1.5;font-size:.9em;}
.simulacro{border:2px solid #6366f1;border-radius:12px;padding:16px;margin-top:26px;background:#0f1729;}
ol.indexol li{margin:3px 0;}
.resp{background:rgba(34,197,94,.08);border-left:4px solid #22c55e;padding:10px;border-radius:6px;margin-top:10px;}
.footer{text-align:center;margin-top:30px;color:#64748b;font-size:.9em;}
"""

def bloque(cls, icono, titulo, contenido):
    return (f"<div class='bloque {cls}'><h3 style='margin-top:0'>{icono} {titulo}</h3>"
            f"{contenido}</div>")

def seccion(titulo):
    return f"<h2 class='seccion'>{titulo}</h2>"
ARBOL = """Enunciado del examen                       -> Instruccion / Concepto
- define estructura                    -> CREATE TABLE (DDL) 🏗
   - claves primarias                 -> PRIMARY KEY (identifica)
   - claves ajenas                    -> FOREIGN KEY ... REFERENCES (relaciona)
- modifica estructura                 -> ALTER TABLE (DDL)
- elimina tabla/columna               -> DROP TABLE / DROP COLUMN (DDL)
- agrega informacion                  -> INSERT (DML)
- modifica informacion (usa WHERE)    -> UPDATE (DML)
- borra informacion (usa WHERE)       -> DELETE (DML)
- recupera / consulta                 -> SELECT (DML)
-   promedio / suma / contar           -> AVG / SUM / COUNT
-   une varias tablas                 -> INNER JOIN (solo filas que coinciden)
- da permisos a un usuario             -> GRANT (DCL)
- quita permisos                       -> REVOKE [CASCADE] (DCL)
- accion automatica al insertar        -> TRIGGER AFTER INSERT
- proceso reutilizable con parametros  -> PROCEDURE (EXEC)
- tabla guardada de una consulta       -> VIEW
Regla de oro: DDL construye . DML manipula . DCL protege . PK identifica . FK relaciona
"""
ARBOL_HTML = f"<div class='arbol'>{ARBOL}</div>"

NOTACION = """<table><tr><th>Simbolo / Termino</th><th>Significado</th></tr>
<tr><td><code>CREATE TABLE</code></td><td>DDL que define la estructura (columnas + restricciones)</td></tr>
<tr><td><code>PRIMARY KEY</code></td><td>Identifica de forma unica cada fila (NOT NULL + UNIQUE)</td></tr>
<tr><td><code>FOREIGN KEY</code></td><td>Relaciona una tabla con la PK de otra (integridad referencial)</td></tr>
<tr><td><code>ON DELETE CASCADE</code></td><td>Al borrar el padre se borran los hijos</td></tr>
<tr><td><code>IDENTITY(n,1)</code></td><td>Auto-incremento en SQL Server (no AUTO_INCREMENT)</td></tr>
<tr><td><code>@variable</code></td><td>Variable local de sesion en SQL Server</td></tr>
<tr><td><code>inserted / deleted</code></td><td>Tablas logicas del trigger: filas nuevas / viejas</td></tr>
<tr><td><code>WITH GRANT OPTION</code></td><td>El receptor puede volver a otorgar el permiso</td></tr>
<tr><td><code>REVOKE ... CASCADE</code></td><td>Quita el permiso tambien a los propagados</td></tr>
<tr><td><code>INNER JOIN</code></td><td>Solo filas con coincidencia en la clausula ON de ambas tablas</td></tr>
<tr><td><code>EXEC</code></td><td>Ejecuta un procedimiento almacenado</td></tr></table>"""
COD_DDL = """<pre><code>CREATE TABLE Hospital (
    Cve_Hos int IDENTITY(1,1) NOT NULL,
    Nom_Hos nvarchar(100)     NOT NULL,
    Ciudad_Hos nvarchar(50),
    CONSTRAINT PK_Hospital PRIMARY KEY (Cve_Hos)
);
CREATE TABLE Medico (
    Id_Med  int IDENTITY(1,1) NOT NULL,
    Nom_Med nvarchar(100)     NOT NULL,
    Clave_Hospital int        NOT NULL,          -- FK hacia Hospital
    CONSTRAINT PK_Medico          PRIMARY KEY (Id_Med),
    CONSTRAINT FK_Medico_Hospital FOREIGN KEY (Clave_Hospital)
        REFERENCES Hospital(Cve_Hos) ON DELETE NO ACTION
);</code></pre>"""

DDL_CONTENIDO = bloque("azul", "🧠", "Concepto: PRIMARY KEY vs FOREIGN KEY",
    "<b>PK (🔑)</b> identifica de forma unica cada fila (NOT NULL + UNIQUE). "
    "<b>FK (🔗)</b> relaciona con la PK de otra tabla garantizando <b>integridad referencial</b>."
) + bloque("naranja", "🛠️", "Codigo aplicado", COD_DDL) + bloque("rojo", "⚠️", "Trampas del examen",
    "<ul><li>❌ Clave_Hospital NO es PK de Medico, es <b>FK</b>.</li>"
    "<li>❌ En SQL Server NO usar AUTO_INCREMENT, usar IDENTITY.</li>"
    "<li>⚠️ DROP TABLE pierde estructura <b>y</b> datos.</li></ul>")

COD_DML = """<pre><code>-- DML: INSERT / UPDATE / DELETE / SELECT (una sobre cada tabla)
INSERT INTO Hospital (Nom_Hos, Ciudad_Hos)
VALUES ('Hospital General', 'Ciudad Juarez');        -- INSERT

UPDATE Servicio SET Costo = 850 WHERE Cve_Ser = 3;  -- UPDATE (USA WHERE)

DELETE FROM Paciente WHERE Id_Pac = 50;             -- DELETE (USA WHERE)

SELECT c.Fecha_Con, m.Nom_Med, p.Nom_Pac, s.Descripcion
FROM   Consulta c
INNER JOIN Medico m   ON c.IDN_Med = m.Id_Med
INNER JOIN Paciente p ON c.Identificador_Pac = p.Id_Pac;
-- OJO: UPDATE/DELETE sin WHERE = modifica TODA la tabla</code></pre>"""

DML_CONTENIDO = bloque("azul", "🧠", "Concepto: DML (Data Manipulation Language)",
    "Manipula los <b>datos</b> (no la estructura): INSERT, UPDATE, DELETE, SELECT."
) + bloque("naranja", "🛠️", "Codigo aplicado", COD_DML) + bloque("verde", "💡", "Dato clave",
    "En UPDATE/DELETE el WHERE es <b>esencial</b>; sin el se afecta toda la tabla."
) + bloque("rojo", "⚠️", "Trampas",
    "DELETE != TRUNCATE != DROP TABLE (fila a fila vs rapido vs destructivo).")

COD_DCL = """<pre><code>-- DCL: Login (servidor) vs User (base de datos)
CREATE LOGIN DrPerez WITH PASSWORD = 'P@ss2024#';   -- nivel SERVIDOR
USE HospitalDB;
CREATE USER DrPerez_user FOR LOGIN DrPerez;          -- mapea login hacia el user (BD)

GRANT SELECT, INSERT ON Paciente TO DrPerez_user WITH GRANT OPTION;  -- permite delegar
REVOKE SELECT ON Paciente FROM DrPerez_user CASCADE;                 -- anula propagados</code></pre>"""

DCL_CONTENIDO = bloque("azul", "🧠", "Concepto: DCL (Data Control Language)",
    "<b>Login</b> = nivel servidor (inicia sesion). <b>User</b> = nivel base de datos (mapea al login). "
    "GRANT otorga; REVOKE quita; WITH GRANT OPTION permite delegar; CASCADE anula los propagados."
) + bloque("naranja", "🛠️", "Codigo aplicado", COD_DCL) + bloque("rojo", "⚠️", "Trampas",
    "No confundir Login (servidor) con User (BD). Sin CASCADE, REVOKE deja intactos los permisos ya re-distribuidos.")

COD_TRIG = """<pre><code>CREATE TRIGGER tr_Audita_Consulta_Insert
ON Consulta
AFTER INSERT              -- se ejecuta automaticamente
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO Bitacora (Cve_Con, Accion, Fecha_Evento)
    SELECT i.Cve_Con, 'INSERT', GETDATE() FROM inserted i;  -- filas nuevas
END;
-- inserted (nuevas) . deleted (viejas) . UPDATE: ambas</code></pre>"""

TRIG_CONTENT = bloque("azul", "🧠", "Concepto: Trigger",
    "Procedure especial que <b>se dispara solo</b> ante INSERT/UPDATE/DELETE, sin parametros ni EXEC. "
    "inserted = filas nuevas; deleted = filas viejas."
) + bloque("naranja", "🛠️", "AFTER INSERT (con inserted)", COD_TRIG) + bloque("verde", "💡", "AFTER UPDATE/DELETE",
    "UPDATE: inserted + deleted; DELETE: solo deleted. Ideal para auditorias."
) + bloque("rojo", "⚠️", "Trampas",
    "Trigger != Procedure: el trigger no recibe parametros y no se invoca.")
COD_PROC = """<pre><code>CREATE PROCEDURE sp_InsertarMedico
    @Nom_Med nvarchar(100),
    @Especialidad nvarchar(60),
    @Clave_Hospital int                -- parametros de entrada
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO Medico (Nom_Med, Especialidad, Clave_Hospital)
    VALUES (@Nom_Med, @Especialidad, @Clave_Hospital);
END;
-- Ejecutar:  EXEC sp_InsertarMedico 'Dr. Gomez', 'Cardiologia', 1;</code></pre>"""

PROC_CONTENIDO = bloque("azul", "🧠", "Concepto: Procedure",
    "Bloque logico <b>reutilizable</b> que recibe <b>parametros</b> y se ejecuta con EXEC. "
    "Ventajas: plan precompilado, centralizacion y seguridad."
) + bloque("naranja", "🛠️", "Codigo aplicado (Insertar)", COD_PROC) + bloque("rojo", "⚠️", "Trampas",
    "Procedure = EXEC + parametros + reutilizable. Trigger = automatico + sin parametros.")

COD_VIEW = """<pre><code>-- Vista: reporte con Paciente + Medico + Fecha + Servicio + Costo
CREATE VIEW vw_ReportePacientes AS
SELECT p.Nom_Pac AS Paciente, m.Nom_Med AS Medico,
       c.Fecha_Con AS Fecha, s.Descripcion AS Servicio, s.Costo
FROM   Paciente p
INNER JOIN Consulta c ON c.Identificador_Pac = p.Id_Pac
INNER JOIN Medico m   ON c.IDN_Med = m.Id_Med
INNER JOIN Servicio s ON c.Clave_Ser = s.Cve_Ser;
-- Consultar:  SELECT * FROM vw_ReportePacientes WHERE Costo > 500;</code></pre>"""

VIEW_CONTENIDO = bloque("azul", "🧠", "Concepto: Vista",
    "Tabla <b>virtual</b>: no almacena datos, guarda la consulta. INNER JOIN solo conserva filas con coincidencia en ON."
) + bloque("naranja", "🛠️", "Codigo aplicado (3 tablas)", COD_VIEW) + bloque("verde", "💡", "Ventajas",
    "Simplificacion, seguridad (oculta tablas base) y consistencia del reporte."
) + bloque("rojo", "⚠️", "Trampas",
    "Una vista no almacena fisicamente los datos; re-ejecuta la consulta cada vez.")

DISENO_HTML = """<table><tr><th>#</th><th>Fase</th><th>Resultado</th></tr>
<tr><td>1</td><td>Recoleccion de requisitos</td><td>Lista de entidades y atributos</td></tr>
<tr><td>2</td><td>Diseno conceptual</td><td>Diagrama Entidad-Relacion</td></tr>
<tr><td>3</td><td>Diseno logico</td><td>Esquema relacional con PK/FK</td></tr>
<tr><td>4</td><td>Diseno fisico</td><td>Script DDL con tipos SQL Server e indices</td></tr>
<tr><td>5</td><td>Implementacion</td><td>Base de datos creada y con datos</td></tr>
<tr><td>6</td><td>Pruebas</td><td>Validacion de integridad y triggers</td></tr>
<tr><td>7</td><td>Mantenimiento</td><td>Backups, indices, evolucion</td></tr></table>"""

DISENO_CONTENIDO = bloque("mapa", "🗺️", "Las 7 fases del diseno", DISENO_HTML) + bloque(
    "recall", "🧠", "Regla de memoria",
    "R-C-L-F-I-P-M: Recolectar, Conceptual, Logico, Fisico, Implementar, Probar, Mantener. Se disena ANTES de insertar.")

PREGUNTAS_HTML = """<table><tr><th>#</th><th>Respuesta corta</th></tr>
<tr><td>1-5</td><td>DDL: CREATE define, ALTER modifica, DROP elimina; PK unica + NOT NULL</td></tr>
<tr><td>6-11</td><td>DML: INSERT/UPDATE/DELETE/SELECT; WHERE obliga en UPDATE/DELETE</td></tr>
<tr><td>12-17</td><td>PK identifica, FK relaciona; Clave_Hospital es FK</td></tr>
<tr><td>18-21</td><td>AVG = promedio; COUNT(*) incluye nulos; @ = variable local</td></tr>
<tr><td>22-26</td><td>GRANT/REVOKE; WITH GRANT OPTION=delegar; CASCADE=propaga; Login vs User</td></tr>
<tr><td>27-33</td><td>Trigger es automatico; AFTER INSERT usa inserted; inserted/deleted</td></tr>
<tr><td>34-38</td><td>Procedure = EXEC + parametros; reuso + seguridad + rendimiento</td></tr>
<tr><td>39-45</td><td>Vista no almacena; INNER JOIN solo coincide; seguridad al ocultar columnas</td></tr>
<tr><td>46-55</td><td>Integridad referencial, huerfanos, PK compuesta N:M, menor privilegio</td></tr>
<tr><td>56-60</td><td>DDL/DML/DCL; PK-FK; pasos de un INSERT; vista reporte; diseno previo</td></tr></table>"""

REPUESTAS_CONTENIDO = bloque("verde", "🎯", "60 preguntas resueltas", PREGUNTAS_HTML) + bloque(
    "recall", "🧠", "Asociacion final",
    "DDL construye · DML manipula · DCL protege · PK identifica · FK relaciona · Trigger reacciona · Procedure reutiliza · View muestra")

TABLA_F = """<table><tr><th>Bloque</th><th>Prioridad</th></tr>
<tr><td> DDL (CREATE/ALTER/DROP/PK/FK)</td><td> Alta (Preg. 1-5, 12-17, 46-55)</td></tr>
<tr><td> DML (INSERT/UPDATE/DELETE/SELECT + WHERE)</td><td> Alta (Preg. 6-11)</td></tr>
<tr><td> DCL (Login/User, GRANT/REVOKE/CASCADE)</td><td> Alta (Preg. 22-26)</td></tr>
<tr><td> Triggers (AFTER INSERT/UPDATE/DELETE)</td><td> Media (Preg. 27-33)</td></tr>
<tr><td> Procedures (EXEC + parametros)</td><td> Media (Preg. 34-38)</td></tr>
<tr><td> Vistas + INNER JOIN (3+ tablas)</td><td> Media (Preg. 39-45)</td></tr>
<tr><td> Diseno BD (7 fases)</td><td> Media (Preg. 56-60)</td></tr></table>"""

TEMAS_HTML = [
    ("DDL - CREATE TABLE (modelo relacional)", DDL_CONTENIDO),
    ("DML - INSERT / UPDATE / DELETE / SELECT", DML_CONTENIDO),
    ("DCL - Login/User + GRANT/REVOKE/CASCADE", DCL_CONTENIDO),
    ("Triggers - AFTER INSERT/UPDATE/DELETE", TRIG_CONTENT),
    ("Procedures - CRUD con EXEC y parametros", PROC_CONTENIDO),
    ("Vistas + INNER JOIN (3+ tablas)", VIEW_CONTENIDO),
    ("Fases del diseno de la base de datos", DISENO_CONTENIDO),
    ("Banco de preguntas resueltas (60)", REPUESTAS_CONTENIDO),
]

SIM_Q = [
    "1) Que instruccion crea la estructura de Medico?",
    "2) Como se enlaza Medico.Clave_Hospital?",
    "3) Que ocurre con un UPDATE sin WHERE?",
    "4) Que tabla logica guarda las filas viejas en un DELETE?",
    "5) Como se llama un procedure?",
    "6) Una vista almacena fisicamente los datos?",
    "7) INNER JOIN conserva filas sin coincidencia?",
    "8) Diferencia entre Login y User?",
    "9) Que tabla resuelve la relacion N:M Consulta <-> Medicamento?",
    "10) Que hace REVOKE ... CASCADE?",
]
SIM_R = [
    "1) CREATE TABLE (DDL).",
    "2) Como FK hacia REFERENCES Hospital(Cve_Hos).",
    "3) Modifica TODA la tabla (peligro).",
    "4) deleted.",
    "5) Con EXEC.",
    "6) No; es una consulta guardada.",
    "7) No; solo las filas que coinciden.",
    "8) Login = servidor; User = BD (mapea al login).",
    "9) Consulta_Medicamento (PK compuesta).",
    "10) Quita el permiso tambien a los propagados.",
]

sim = ['<div class="simulacro"><h3> Simulacro Visual de Emergencia (10 preguntas)</h3>']
sim.append("<ol>")
for q in SIM_Q:
    sim.append(f"<li>{q}</li>")
sim.append("</ol>")
sim.append('<div class="resp"><h4 style="background:#22C55E;color:#fff;display:inline-block;padding:2px 10px;border-radius:6px">RESPUESTAS</h4>')
for r in SIM_R:
    sim.append(f"<p>{r}</p>")
sim.append("</div></div>")

body = [f"<header><h1>GUIA VISUAL DE ESTUDIO: SQL SERVER</h1>"
        f"<p>Configuracion visual: codigo de colores (conceptos, trampas, ejemplos, formulas) y repaso activo.</p>"
        f"<p><span class='badge'>Sistema hospitalario</span> "
        f"<span class='badge'>SQL Server (Transact-SQL)</span> "
        f"<span class='badge'>60 preguntas + desarrollo</span></p></header>"]

body.append("<h2 class='seccion'>Arbol de decision</h2>")
body.append(ARBOL_HTML)
body.append("<h2 class='seccion'>Tabla de notacion</h2>")
body.append(NOTACION)
body.append("<h2 class='seccion'>Prioridad de temas (Top 20%)</h2>")
body.append(bloque("azul", "", "Bloques del examen", TABLA_F))
body.append("<h2 class='seccion'>Indice</h2>")
body.append("<ol class='indexol'>")
for titulo, _ in TEMAS_HTML:
    body.append(f"<li>{titulo}</li>")
body.append("</ol>")
for titulo, contenido in TEMAS_HTML:
    body.append(seccion(titulo) + "\n" + contenido)
body.append("".join(sim))
body.append('<div class="footer">Guia generada por ParetoTutor Visual - Base: Microsoft Learn (Transact-SQL, SQL Server). Imprime a PDF (Ctrl+P).</div>')

html = ("<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
        "<title>Guia Visual de SQL Server</title><style>" + CSS + "</style></head><body>"
        + "\n".join(body) + "</body></html>")

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("GUARDADO:", OUT)
print("Bytes HTML:", len(html))
