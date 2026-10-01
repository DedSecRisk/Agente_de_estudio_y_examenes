# 📚 EXAMEN RESUELTO — SQL SERVER (Sistema de Gestión Hospitalaria)

> **Fuente:** Microsoft Learn — *Transact-SQL* (SQL Server). Cada respuesta referencia la documentación oficial y evita sintaxis propias de MySQL, tal como exige la sección 12 del enunciado.
>
> **Cómo estudiar este archivo:** 1) Lee primero el **Resumen de frecuencia** y el **Árbol de decisión**. 2) Estudia el **desarrollo implementado** (DDL→DML→DCL→Triggers→Procedures→Vistas) que es el corazón del examen. 3) Repasa las **60 preguntas resueltas** con la tabla de notación al lado. 4) Memoriza la **Asociación final**.

---

## 1️⃣ Resumen del análisis del examen

El examen plantea un único caso: **una base de datos hospitalaria en SQL Server**. Las 60 preguntas giran en torás a 8 bloques conceptuales:

| Bloque | Temas clave | Preguntas | Prioridad |
|---|---|---|---|
| 🏗️ DDL / Modelo relacional | CREATE TABLE, PK, FK, tipos, restricciones, ALTER, DROP | 1‑5, 12‑17, 46‑55, 57 | 🔵 Alta |
| 📊 DML | INSERT / UPDATE / DELETE / SELECT, WHERE, riesgos | 6‑11, 58 | 🔵 Alta |
| 🔐 DCL / Seguridad | Login vs User, GRANT/REVOKE, WITH GRANT OPTION, CASCADE | 22‑26, 55, 7 | 🔵 Alta |
| ⚡ Triggers | AFTER INSERT/UPDATE/DELETE, `inserted`/`deleted` | 27‑33 | 🟡 Media |
| 📦 Procedures | Parámetros, EXEC, ventajas, CRUD | 34‑36 | 🟡 Media |
| 👁️ Vistas | CREATE VIEW, INNER JOIN (≥3 tablas), alias, seguridad | 37‑45, 59 | 🟡 Media |
| Σ Funciones/Variables | AVG/COUNT/SUM/MAX/MIN, `@var`, agregada vs escalar | 18‑21, 6 | 🟡 Media |
| 🔄 Diseño BD | 7 fases, integridad referencial | 46, 56, 60 | 🟡 Media |

> **Top 20% (claves 10/10):** DDL (PK/FK/tipos/restricciones), DML (+ WHERE), DCL (Login/User/GRANT/CASCADE), Triggers lógicos, Procedures, Vistas + INNER JOIN, Fases de diseño.

## 2️⃣ Árbol de decisión — «¿Qué instrucción SQL usar?»

```text
Enunciado del examen                              -> Instrucción / Concepto
├─ "Define/crea la tabla"                          -> CREATE TABLE  (DDL)  🏗️
│   ├─ "claves primarias"                          ->  PRIMARY KEY  (identifica 🔑)
│   ├─ "claves foráneas"                           ->  FOREIGN KEY   (relaciona 🔗)
│   └─ "tipos de datos"                            ->  int, nvarchar, decimal, date...
├─ "modifica la estructura"                        -> ALTER TABLE    (DDL)  ⚙️
├─ "elimina la tabla/columna"                      -> DROP TABLE / ALTER TABLE ... DROP COLUMN (DDL) 🗑️
├─ "agrega información"                            -> INSERT        (DML)  ➕
├─ "modifica información"                          -> UPDATE        (DML)  ✏️  (USA WHERE ⚠️)
├─ "borra información"                             -> DELETE        (DML)  ❌  (USA WHERE ⚠️)
├─ "recupera/consulta"                             -> SELECT        (DML)  🔍
│   ├─ "promedio/suma/contar"                      ->  funciones agregadas AVG/SUM/COUNT
│   └─ "une varias tablas"                         ->  INNER JOIN (solo filas que coinciden)
├─ "da permisos a un usuario"                      -> GRANT         (DCL)  🔓
├─ "quita permisos"                                -> REVOKE        (DCL)  🔒
├─ "acción automática al insertar"                 -> TRIGGER AFTER INSERT  ⚡
├─ "proceso reutilizable con parámetros"           -> PROCEDURE     (EXEC) 📦
├─ "tabla 'guardada' de una consulta"              -> VIEW          👁️
└─ "regla de memoria"                              -> DDL construye · DML manipula · DCL protege
```

## 3️⃣ Tabla de notación de símbolos (SQL Server)

| Símbolo / Término | Significado en este examen |
|---|---|
| `CREATE TABLE` | DDL: define la estructura (columnas + restricciones) de una tabla |
| `PRIMARY KEY (PK)` | Restricción que identifica de forma única cada fila; implícita `NOT NULL` y `UNIQUE` |
| `FOREIGN KEY (FK)` | Restricción que enlaza una columna con la PK de otra tabla para garantizar integridad referencial |
| `ON DELETE {NO ACTION\|CASCADE\|SET NULL\|SET DEFAULT}` | Acción de referencia al borrar el registro padre |
| `ON UPDATE {NO ACTION\|CASCADE}` | Acción de referencia al actualizar la PK padre |
| `IDENTITY(seed,increment)` | Columna autogenerada (equivalente a AUTO_INCREMENT de MySQL, pero solo en SQL Server) |
| `DECLARE @var tipo` | Declara una variable de sesión (`@` = variable en SQL Server) |
| `INSERTED`, `DELETED` | Tablas lógicas invisible que SQL Server crea DENTRO de un trigger para acceder a filas nuevas/viejas |
| `GRANT … TO … WITH GRANT OPTION` | Otorga un permiso y permite al receptor volver a otorgarlo |
| `REVOKE … CASCADE` | Quita el permiso y también los derechos que el receptor había propagado |
| `db_datareader / db_datawriter` | Roles fijos de base de datos: SELECT todo vs INSERT/UPDATE/DELETE todo |
| `INNER JOIN` | Une filas que tienen coincidencia en la cláusula `ON` de AMBAS tablas |
| `E(X), Var(X)` | (No SQL) — usada en preguntas de combinación probabilidad-estadística; aquí solo referencia cruzada |


---

# 4️⃣ DESARROLLO IMPLEMENTADO — Sistema Hospitalario (SQL Server)

> **Enfoque del examen:** teoría *antes* del código, estructura general, código aplicado, explicación línea a línea y conceptos relacionados. Todo es **Transact-SQL (SQL Server)**; respeta la regla 12 (nada de MySQL).

## 4A. ✅ DDL — `CREATE TABLE` (modelo relacional)

Se solicita crear las 7 tablas del modelo definiendo **clave primaria (PK)**, **clave foránea (FK)** con integridad referencial, **tipos de datos** propios de SQL Server y **restricciones** (`NOT NULL`, `CHECK`).

> **📖 Concepto (🔵):**
> - **DDL** (*Data Definition Language*) define la **estructura** (no datos): `CREATE`, `ALTER`, `DROP`.
> - **PRIMARY KEY (🔑)**: identifica únicamente cada fila; es implícitamente `NOT NULL` y `UNIQUE`. Nivel **columna** (`col tipo PRIMARY KEY`) o **tabla** (`CONSTRAINT pk PRIMARY KEY (col)`).
> - **FOREIGN KEY (🔗)**: obliga a que un valor coincida con una PK de otra tabla → integridad referencial.
> - Tipos SQL Server (no MySQL): `int`, `tinyint`, `decimal(p,s)`, `nvarchar(n)`, `varchar(n)`, `date`, `time`, `bit`.

### Modelo relacional resuelto — tablas 1 a 4

```sql
/* 1) HOSPITAL — tabla padre: 1 hospital → N médicos */
CREATE TABLE Hospital
(
    Cve_Hos        int IDENTITY(1,1) NOT NULL,  -- PK autogenerada (SQL Server; NO MySQL AUTO_INCREMENT)
    Nom_Hos        nvarchar(100)    NOT NULL,
    Ciudad_Hos     nvarchar(50),
    Direccion_Hos  nvarchar(200),
    Tel_Hos         nvarchar(20),
    Director        nvarchar(100),
    CONSTRAINT PK_Hospital PRIMARY KEY (Cve_Hos)
);

/* 2) MÉDICO — hija de Hospital, padre de Consulta */
CREATE TABLE Médico
(
    Id_Med       int IDENTITY(1,1) NOT NULL,
    Nom_Med      nvarchar(100) NOT NULL,
    Dir_Med      nvarchar(200),
    Especialidad nvarchar(60)   NOT NULL,
    Edad_Med     tinyint        CHECK (Edad_Med BETWEEN 25 AND 100),
    Clave_Hospital int          NOT NULL,   -- FK → Hospital.Cve_Hos
    CONSTRAINT PK_Médico          PRIMARY KEY (Id_Med),
    CONSTRAINT FK_Médico_Hospital FOREIGN KEY (Clave_Hospital)
        REFERENCES Hospital(Cve_Hos)
        ON DELETE NO ACTION      -- borrar el hospital NO borra sus médicos
        ON UPDATE CASCADE       -- cambiar la PK del hospital se propaga
);

/* 3) PACIENTE — padre de Consulta */
CREATE TABLE Paciente
(
    Id_Pac    int IDENTITY(1,1) NOT NULL,
    Nom_Pac   nvarchar(100)  NOT NULL,
    Dir_Pac   nvarchar(200),
    Tel_Pac   nvarchar(20),
    Edad_Pac  tinyint        CHECK (Edad_Pac BETWEEN 0 AND 120),
    CONSTRAINT PK_Paciente PRIMARY KEY (Id_Pac)
);

/* 4) MEDICAMENTO — padre de Consulta_Medicamento */
CREATE TABLE Medicamento
(
    Cve_Med      int IDENTITY(1,1) NOT NULL,
    Descripción  nvarchar(150)    NOT NULL,
    Marca        nvarchar(80),
    Tamaño       nvarchar(40),
    Gramos       decimal(6,2)     CHECK (Gramos > 0),
    CONSTRAINT PK_Medicamento PRIMARY KEY (Cve_Med)
);
```

> **🔍 Explicación (🔵):** `int IDENTITY(1,1)` auto-incrementa (SQL Server); `CHECK` impone integridad de **dominio**; las restricciones van nombradas (`CONSTRAINT nombre ...`) para claridad; `ON DELETE NO ACTION` rechaza borrado del padre si existen hijos, `ON UPDATE CASCADE` propaga cambios de PK.

### Modelo relacional resuelto — tablas 5 a 7

```sql
/* 5) SERVICIO — padre de Consulta */
CREATE TABLE Servicio
(
    Cve_Ser      int IDENTITY(1,1) NOT NULL,
    Descripción  nvarchar(150)    NOT NULL,
    Tipo_Ser     nvarchar(60),
    Costo        decimal(10,2)    CHECK (Costo >= 0),
    CONSTRAINT PK_Servicio PRIMARY KEY (Cve_Ser)
);

/* 6) CONSULTA — nexo Médico × Paciente × Servicio */
CREATE TABLE Consulta
(
    Cve_Con          int IDENTITY(1,1) NOT NULL,
    Fecha_Con        date             NOT NULL,
    Hora_Con         time             NOT NULL,
    IDN_Med          int              NOT NULL,   -- FK → Médico.Id_Med
    Identificador_Pac int             NOT NULL,   -- FK → Paciente.Id_Pac
    Clave_Ser        int              NOT NULL,   -- FK → Servicio.Cve_Ser
    CONSTRAINT PK_Consulta PRIMARY KEY (Cve_Con),
    CONSTRAINT FK_Consulta_Médico   FOREIGN KEY (IDN_Med)         REFERENCES Médico(Id_Med),
    CONSTRAINT FK_Consulta_Paciente FOREIGN KEY (Identificador_Pac) REFERENCES Paciente(Id_Pac),
    CONSTRAINT FK_Consulta_Servicio FOREIGN KEY (Clave_Ser)       REFERENCES Servicio(Cve_Ser)
);

/* 7) CONSULTA_MEDICAMENTO — tabla intermedia N:M Consulta ↔ Medicamento */
CREATE TABLE Consulta_Medicamento
(
    Consulta     int NOT NULL,   -- FK → Consulta.Cve_Con
    Medicamento  int NOT NULL,   -- FK → Medicamento.Cve_Med
    Cantidad     int NOT NULL CONSTRAINT DF_ConsMed_Defecto DEFAULT (1),
    CONSTRAINT PK_Consulta_Medicamento PRIMARY KEY (Consulta, Medicamento),  -- PK COMPUESTA
    CONSTRAINT FK_CMaConsulta    FOREIGN KEY (Consulta)    REFERENCES Consulta(Cve_Con) ON DELETE CASCADE,
    CONSTRAINT FK_CMaMedicamento FOREIGN KEY (Medicamento) REFERENCES Medicamento(Cve_Med)
);
```

### 🔴 `PRIMARY KEY` vs `FOREIGN KEY` — ¿por qué `Clave_Hospital` es FK?

| PRIMARY KEY (🔑) | FOREIGN KEY (🔗) |
|---|---|
| Identifica **de forma única** cada fila de **su propia** tabla. | **Relaciona** una tabla con la PK de otra. |
| Implícita `NOT NULL` + `UNIQUE`. | Puede repetirse (many-to-one) y aceptar nulos. |
| Una tabla tiene **una** PK (puede ser compuesta). | Una tabla puede tener **varias** FK. |
| `Hospital.Cve_Hos` identifica al hospital. | `Médico.Clave_Hospital` señala **a qué hospital** pertenece. |

> ✅ **`Clave_Hospital` es FK** porque su valor **debe existir** en `Hospital.Cve_Hos` (PK del hospital al que el médico pertenece). No es PK de Médico: varios médicos pertenecen al mismo hospital (relación 1:N).

### ⚠️ Trampas del examen (DDL)
- ❌ Decir que `Clave_Hospital` es PK de Médico → es **FK**.
- ❌ Usar `AUTO_INCREMENT` → es de MySQL; en SQL Server es `IDENTITY`.
- ❌ Olvidar `NOT NULL` en columnas FK obligatorias.
- ❌ No nombrar restricciones (`CONSTRAINT FK_...`) → el examen valora la claridad.


## 4B. ✅ Otras instrucciones DDL (mín. 4)

> **📖 Concepto (🔵):** La DDL no solo crea; también **modifica** y **destruye** estructuras. `ALTER` cambia la definición; `DROP` elimina.

| Instrucción | Qué modifica | Riesgo / consecuencia |
|---|---|---|
| `ALTER TABLE ... ADD col` | Añade una columna. | Si no es `NULL`-able debe incluir `DEFAULT`. |
| `ALTER TABLE ... ALTER COLUMN col` | Cambia tipo o nulidad. | Puede truncar/longitud insuficiente → **pérdida de datos**. |
| `ALTER TABLE ... DROP COLUMN col` | Borra una columna. | ⚠️ Falla si la columna participa en un **índice/índice UNIQUE/FK**. |
| `DROP TABLE` | Elimina la tabla **y** sus índices/restricciones. | ⚠️ **Pierde los datos**; imposible de deshacer sin backup. |
| `sp_rename` | Renombra tabla/columna. | No actualiza referencias en vistas/procedures → usar con cuidado. |

```sql
-- 1) ALTER TABLE: agregar columna + restricción
ALTER TABLE Paciente
ADD Número_Expediente nvarchar(20) NOT NULL
    CONSTRAINT DF_Paciente_Expediente DEFAULT ('S/N');

-- 2) ALTER TABLE: modificar tipo de dato
ALTER TABLE Médico
ALTER COLUMN Especialidad nvarchar(80) NOT NULL;   -- ampliar ancho de texto

-- 3) ALTER TABLE ... DROP COLUMN: borrar una columna
ALTER TABLE Médico
DROP COLUMN Dir_Med;                                -- error si col. está en un índice/FK

-- 4) sp_rename: renombrar la tabla (y una columna)
EXEC sp_rename 'Paciente', 'Pacientes';            -- renombra tabla
EXEC sp_rename 'Pacientes.Tel_Pac', 'Telefono_Paciente';  -- renombra columna (NO uses comillas en el 2º param)

-- 5) DROP TABLE: destruir la tabla (elimina datos + metadatos)
DROP TABLE Consulta_Medicamento;                   -- ⚠️ ¡datos perdidos!
```

> ⚠️ **Trampa del examen:** decir que `DROP TABLE` solo elimina la estructura → **elimina la tabla completa y sus datos**. Y que `ALTER TABLE ... DROP COLUMN` siempre funciona → **falla si la columna está indexada/FK** (documentado en Microsoft Learn: *ALTER TABLE*).


## 5️⃣ DML — Data Manipulation Language

> **📖 Concepto (🔵):** La DML **manipula los datos** (no la estructura): `INSERT`, `UPDATE`, `DELETE`, `SELECT`. Cada operación se hace sobre una tabla diferente, como pide el examen.

### INSERT — agregar registros (tabla `Hospital`)

```sql
INSERT INTO Hospital (Nom_Hos, Ciudad_Hos, Dirección_Hos, Tel_Hos, Director)
VALUES ('Hospital General', 'Ciudad Juárez', 'Av. Héroes 100', '654-1234', 'Dra. López');
-- Cve_Hos se autogenera con IDENTITY, por eso no se incluye en la lista de columnas
```

### UPDATE — modificar registros (tabla `Servicio`)

```sql
UPDATE Servicio
SET Costo = 850.00
WHERE Cve_Ser = 3;       -- ⚠️ WHERE obliga: sin ella, se actualizan TODOS los registros
-- Riesgo: UPDATE sin WHERE = pisar la tabla entera (Costo=850 para TODOS los servicios)
```

### DELETE — borrar registros (tabla `Paciente`)

```sql
DELETE FROM Paciente
WHERE Id_Pac = 50;       -- ⚠️ WHERE obliga: sin ella, borra TODOS los pacientes
-- Riesgo: DELETE sin WHERE = borrado total irreversible (registro por registro + triggers)
```

### SELECT — recuperar información (tablas `Consulta` + `Médico` + `Paciente`)

```sql
SELECT c.Fecha_Con, c.Hora_Con,
       m.Nom_Med AS Médico,
       p.Nom_Pac AS Paciente,
       s.Descripción AS Servicio,
       s.Costo
FROM   Consulta c
INNER JOIN Médico m    ON c.IDN_Med          = m.Id_Med
INNER JOIN Paciente p  ON c.Identificador_Pac = p.Id_Pac
INNER JOIN Servicio s  ON c.Clave_Ser        = s.Cve_Ser
WHERE  c.Fecha_Con >= '2024-01-01'
ORDER BY c.Fecha_Con DESC;
```

> ⚠️ **Trampas del examen (DML):**
> - `UPDATE/DELETE` **sin `WHERE`** afecta **toda la tabla** (pregunta 9 y 10).
> - `SELECT *` vs columnas específicas (pregunta 11): `SELECT *` rompe si se reordean/reordenan columnas y es costoso.
> - `DELETE` (DML, fila a fila, conserva IDENTITY y activa triggers) ≠ `TRUNCATE` (DDL, rápido, reinicia IDENTITY, no activa triggers) ≠ `DROP TABLE` (elimina estructura + datos).

### 6️⃣ Funciones y variables

> **📖 Concepto (🔵):** `DECLARE @var tipo` crea una **variable de sesión** (el `@` es la convención de SQL Server para variables). `=` asigna el **escalar** resultado de una función agregada.

```sql
DECLARE @TotalPacientes  int;          -- variables con @
DECLARE @PromedioEdad    decimal(5,2);
DECLARE @ServicioMasCaro nvarchar(150);

SELECT @TotalPacientes  = COUNT(*)      FROM Paciente;   -- función agregada (sobre muchos rows → 1 valor)
SELECT @PromedioEdad    = AVG(Edad_Pac) FROM Paciente;    -- AVG: promedio
SELECT @ServicioMasCaro = MAX(Descripción) FROM Servicio; -- MAX: sobre texto → orden alfabético

SELECT @TotalPacientes AS Total, @PromedioEdad AS PromEdad, @ServicioMasCaro AS ServicioCaro;
```

| Función | Tipo | Uso en el hospital |
|---|---|---|
| `AVG()` | Agregada | Promedio de edades de pacientes |
| `COUNT()` | Agregada | Nº de consultas realizadas |
| `SUM()` | Agregada | Total de costos facturados |
| `MAX()` / `MIN()` | Agregada | Servicio más/menos costoso |
| `GETDATE()`, `CONCAT()`... | Escalar | Devuelven 1 valor por fila → diferencia con agregadas |

> **🔵 Agregada vs Escalar:** una **función agregada** (AVG/COUNT/SUM/MAX/MIN) colapsa **muchos** registros en **uno** solo; una **función escalar** devuelve un valor **por fila**.


## 7️⃣ DCL — Data Control Language (seguridad)

> **📖 Concepto (🔵):** La DCL **protege** los datos asignando o retirando permisos. **Login = nivel servidor** (inicia sesión en la instancia); **User = nivel base de datos** (el login se "mapea" a un user dentro de la BD). Un login puede mapearse a varios users; un user "sin login" (`CREATE USER ... WITHOUT LOGIN`) es un usuario contenido (contenedores). Un **rol fijo** como `db_datareader` da SELECT a todo y `db_datawriter` da INSERT/UPDATE/DELETE a todo.

```sql
/* Nivel SERVIDOR: crear el login */
CREATE LOGIN DrPerez WITH PASSWORD = 'P@rez2024#';
/* Nivel BASE DE DATOS: mapear ese login a un usuario dentro de la BD hospital */
USE HospitalDB;                                       -- usar la BD del hospital
CREATE USER DrPerez_user FOR LOGIN DrPerez;           -- 1 login → 1 user (puede ser N)

/* Otorgar permisos sobre DOS tablas (con WITH GRANT OPTION) */
GRANT SELECT, INSERT ON Paciente TO DrPerez_user WITH GRANT OPTION;
GRANT SELECT ON Medicamento TO DrPerez_user;
/* => DrPerez_user PUEDE volver a otorgar SELECT/INSERT sobre Paciente a otro usuario */

/* Retirar privilegios propagados con CASCADE */
REVOKE SELECT ON Paciente FROM DrPerez_user CASCADE;
/* CASCADE: además de quitarle SELECT a DrPerez_user, revoca también los derechos
   que DrPerez_user había concedido a otros (porque dependían de su cadena) */
```

| Término | Significado |
|---|---|
| `CREATE LOGIN` | Principal de **servidor**: permite iniciar sesión en la instancia. |
| `CREATE USER` | Principal de **base de datos**: mapa a un login para acceder a la BD. |
| `GRANT` | **Otorga** un permiso a un principal. |
| `WITH GRANT OPTION` | El receptor **también puede otorgar** ese permiso a otros. |
| `REVOKE` | **Quita** un permiso concedido. |
| `CASCADE` | Al revocar (con `GRANT OPTION FOR`), también anula los permisos **propagados**. |
| `REVOKE` vs `DENY` | `REVOKE` quita lo concedido; `DENY` **niega** (tiene prioridad sobre grants). |

> ⚠️ **Trampa del examen:** confundir *login* y *user* como lo mismo → el examen pregunta diferencia precisa (pregunta 26). Y creer que `REVOKE` borra todo → sin `CASCADE` deja intactos los permisos que el usuario ya había re-distribuido.


## 8️⃣ Triggers (3: AFTER INSERT / UPDATE / DELETE)

> **📖 Concepto (🔵):** Un **trigger** es un **procedimiento especial que se ejecuta AUTOMÁTICAMENTE** cuando ocurre un evento DML (`INSERT`/`UPDATE`/`DELETE`) en la tabla. No se llama con `EXEC` (a diferencia de un procedure). SQL Server crea **dos tablas lógicas invisibles** dentro del trigger:
> - **`inserted`**: contiene las filas **nuevas** (después de INSERT/UPDATE).
> - **`deleted`**: contiene las filas **viejas** (antes de DELETE/UPDATE).
> - En un `INSERT` → solo existe `inserted`; en un `DELETE` → solo `deleted`; en un `UPDATE` → ambas.

### ⚡ Trigger 1 — AFTER INSERT (audita nuevas consultas) → usa `inserted`

```sql
CREATE TRIGGER tr_Audita_Consulta_Insert
ON Consulta
AFTER INSERT                       -- se dispara tras un INSERT exitoso en Consulta
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO Bitacora_Consultas (Cve_Con, Fecha_Con, Acción, Fecha_Evento)
    SELECT i.Cve_Con, i.Fecha_Con, 'INSERT', GETDATE()
    FROM inserted i;               -- filas recién insertadas
END;
/* Bitacora_Consultas: tabla auxiliar para auditoría (creada con DDL) */
```

### ⚡ Trigger 2 — AFTER UPDATE (previene edad inválida de médico) → usa `deleted` y `inserted`

```sql
CREATE TRIGGER tr_Médico_Edad_Update
ON Médico
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    IF EXISTS (SELECT 1 FROM inserted WHERE Edad_Med < 25)
    BEGIN
        RAISERROR('La edad del médico no puede ser menor a 25 años.', 16, 1);
        ROLLBACK TRANSACTION;      -- deshace la actualización que viola la regla
    END
END;
-- Comparar inserted (nuevo valor) con deleted (viejo) permite validar cambios específicos
```

### ⚡ Trigger 3 — AFTER DELETE (elimina las líneas hijas de Consulta_Medicamento) → usa `deleted`

```sql
CREATE TRIGGER tr_Consulta_Delete
ON Consulta
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON;
    -- Si se borra una consulta, también se borran sus relaciones con medicamentos
    DELETE cm
    FROM Consulta_Medicamento cm
    INNER JOIN deleted d ON cm.Consulta = d.Cve_Con;   -- filas que se estaban borrando
END;
```

> 🧠 **Regla de memoria:** *Trigger = reacción automática; Procedure = herramienta manual.* El trigger usa `inserted`/`deleted` y **nunca recibe parámetros**; el procedure se llama con `EXEC` y **sí recibe parámetros**.


## 9️⃣ Procedimientos almacenados (4 — CRUD con parámetros)

> **📖 Concepto (🔵):** Un **procedure** (`CREATE PROCEDURE … AS BEGIN … END`) es un **bloque lógico reutilizable** que **se ejecuta con `EXEC`** y **sí recibe parámetros** (a diferencia del trigger). Ventajas: reutilización, plan de ejecución **precompilado** (≈ rendimiento), centralización de lógica y **seguridad** (el usuario llama al procedure sin necesidad de permisos directos sobre las tablas).

```sql
-- 1) PROCEDURE INSERTAR: agrega un médico (recibe parámetros de entrada)
CREATE PROCEDURE sp_InsertarMédico
    @Nom_Med nvarchar(100),
    @Especialidad nvarchar(60),
    @Clave_Hospital int
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO Médico (Nom_Med, Dir_Med, Especialidad, Edad_Med, Clave_Hospital)
    VALUES (@Nom_Med, NULL, @Especialidad, NULL, @Clave_Hospital);
END;
-- Ejecución:  EXEC sp_InsertarMédico 'Dr. Gómez', 'Cardiología', 1;

-- 2) PROCEDURE ACTUALIZAR: cambia la especialidad de un médico
CREATE PROCEDURE sp_ActualizarMédico
    @Id_Med int,
    @NuevaEspecialidad nvarchar(60)
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE Médico
    SET Especialidad = @NuevaEspecialidad
    WHERE Id_Med = @Id_Med;       -- WHERE protege de sobreescibir todo
END;

-- 3) PROCEDURE CONSULTAR: devuelve las consultas de un paciente (usa SELECT)
CREATE PROCEDURE sp_ConsultasPaciente
    @Id_Pac int
AS
BEGIN
    SET NOCOUNT ON;
    SELECT c.Fecha_Con, c.Hora_Con, m.Nom_Med AS Médico, s.Descripción AS Servicio
    FROM Consulta c
    INNER JOIN Médico m ON c.IDN_Med = m.Id_Med
    WHERE c.Identificador_Pac = @Id_Pac
    ORDER BY c.Fecha_Con DESC;
END;
-- Ejecución:  EXEC sp_ConsultasPaciente 5;

-- 4) PROCEDURE ELIMINAR: borra una consulta (y gracias al trigger, también sus medicamentos)
CREATE PROCEDURE sp_EliminarConsulta
    @Cve_Con int
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        BEGIN TRANSACTION;
            DELETE FROM Consulta WHERE Cve_Con = @Cve_Con;  -- dispara tr_Consulta_Delete
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;            -- transacciones explícitas
        RAISERROR('No se pudo eliminar la consulta: %s', 16, 1, ERROR_MESSAGE());
    END CATCH
END;
```

> 🧠 **Regla de memoria:** *Procedure = EXEC + parámetros + reutilizable + plan precompilado.* Trigger = automático + `inserted`/`deleted` + sin parámetros.


## 🔟 Vistas (2 — INNER JOIN con ≥3 tablas)

> **📖 Concepto (🔵):** `CREATE VIEW … AS SELECT …` crea una **tabla virtual guardada**: **no almacena físicamente** los datos, sino la *consulta*. Se consulta como una tabla normal (`SELECT * FROM Vista`). Ventajas: **seguridad** (se ocultan columnas/tables base y se concede permiso solo sobre la vista) y **simplificación** (une varias tablas en una sola). **Alias** (`c`, `m`, `p`) abrevian nombres y desambiguan columnas.

```sql
-- Vista 1: reporte médico (Médico + Hospital + Consultas realizadas)
CREATE VIEW vw_ReporteMedico AS
SELECT m.Nom_Med AS Médico,
       m.Especialidad,
       h.Nom_Hos AS Hospital,
       COUNT(c.Cve_Con) AS NumConsultas
FROM   Médico m
INNER JOIN Hospital h ON m.Clave_Hospital = h.Cve_Hos     -- INNER JOIN: solo coincide
INNER JOIN Consulta c ON c.IDN_Med = m.Id_Med             -- 3 tablas unidas
GROUP BY m.Nom_Med, m.Especialidad, h.Nom_Hos;

-- Vista 2: historial clínico de pacientes (Paciente + Médico + Servicio + Consulta)
CREATE VIEW vw_HistorialPaciente AS
SELECT p.Nom_Pac AS Paciente,
       m.Nom_Med AS Médico,
       s.Descripción AS Servicio,
       c.Fecha_Con,
       s.Costo
FROM   Paciente p
INNER JOIN Consulta c ON c.Identificador_Pac = p.Id_Pac
INNER JOIN Médico m   ON c.IDN_Med = m.Id_Med
INNER JOIN Servicio s ON c.Clave_Ser = s.Cve_Ser;

-- Consultar las vistas (como si fueran tablas):
SELECT * FROM vw_ReporteMedico WHERE NumConsultas > 5;
SELECT Médico, Servicio, Costo FROM vw_HistorialPaciente WHERE Paciente = 'Ana Torres';
```

> ⚠️ **Trampa del examen:** creer que una vista "almacena" los datos → la vista **ejecuta la consulta en tiempo real**. Y que `INNER JOIN` incluye NO coincidencias → **solo conserva filas que coinciden en `ON` en ambas tablas** (para incluir no coincidencias se usa `LEFT/RIGHT JOIN`).

## 1️⪶ Fases del diseño de la base de datos (7)

| # | Fase | Objetivo | Actividad principal | Resultado | Aplicado al hospital |
|---|---|---|---|---|---|
| 1 | Recolección de requisitos | Entender qué se necesita | Entrevistas a médicos/administración | Lista de entidades y atributos | Hospitales, médicos, pacientes, medicamentos… |
| 2 | Diseño conceptual | Modelo independiente del SGDB | Diagrama Entidad-Relación (ER) | Modelo ER | Hospital 1:N Médico, Consulta N:M Medicamento |
| 3 | Diseño lógico | Modelo relacional | PK/FK, normalización (1FN/2FN/3FN) | Esquema relacional | Las 7 tablas con PK/FK del modelo |
| 4 | Diseño físico | Implementación concreta | Tipos SQL Server, índices, particiones | Script DDL | `CREATE TABLE` con `int`, `nvarchar`, índices |
| 5 | Implementación | Construir el sistema | Ejecutar DDL + cargar datos | Base de datos creada | Los `CREATE TABLE` de la sección 4A |
| 6 | Pruebas | Verificar correctitud | Insertar datos, validar FK, prueba de triggers | Bugs corregidos | Probar INSERT/UPDATE con cláusulas WHERE |
| 7 | Mantenimiento | Operar y evolucionar | Backups, índices, versiones, monitoreo | BD operativa | Reuniones, auditorías de permisos (DCL) |

> 🧠 **Regla de memoria:** *Recoleccionar → Conceptual → Lógico → Físico → Implementar → Probar → Mantener* (R‑C‑L‑F‑I‑P‑M). Se diseña **antes** de insertar (pregunta 60) para que las **relaciones y restricciones existan** cuando se ingresan los datos.


---

# 5️⃣ RESPUESTAS — 60 PREGUNTAS DEL EXAMEN (Fundamentadas en Microsoft Learn)

## 📚 Banco de preguntas teóricas — Nivel universitario

### DDL

**1. ¿Qué significa DDL y cuál es su objetivo?**
DDL = *Data Definition Language*. Su objetivo es **definir y modificar la estructura** de la base de datos (tablas, columnas, restricciones, índices), no los datos. Incluye `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME`. *Fuente: Microsoft Learn – CREATE TABLE / ALTER TABLE.*

**2. ¿Diferencia entre `CREATE`, `ALTER` y `DROP`?**
- `CREATE`: **crea** un nuevo objeto (tabla, vista, procedure, trigger…).
- `ALTER`: **modifica** la definición de un objeto existente (añadir/quitar columna, cambiar tipo).
- `DROP`: **elimina** el objeto y, en el caso de `DROP TABLE`, **sus datos y metadatos**.
*Fuente: Microsoft Learn – ALTER TABLE.*

**3. ¿Diferencia entre modificar la estructura y modificar los datos?**
Modificar la **estructura** (`ALTER TABLE`) cambia columnas/restricciones y no afecta directamente al contenido; modificar los **datos** (`INSERT/UPDATE/DELETE`) cambia el contenido sin tocar la estructura. *Fuente: Microsoft Learn – CREATE TABLE / INSERT.*

**4. ¿Qué sucede con los datos cuando se usa `DROP TABLE`?**
Se **pierden los datos y la estructura** de la tabla (columnas, restricciones, índices). No se puede `ROLLBACK` si ya se hizo `COMMIT`. *Fuente: Microsoft Learn – ALTER TABLE (DROP).*

**5. ¿Por qué una PK debe identificar de forma única cada registro?**
Porque la **clave primaria** es el identificador único de cada fila; debe ser `NOT NULL` y `UNIQUE` para que ninguna fila se confunda con otra y para que las FK puedan apuntar a ella sin ambigüedades.


### DML

**6. ¿Qué significa DML?**
DML = *Data Manipulation Language*. **Manipula los datos** de las tablas sin cambiar la estructura: `INSERT`, `UPDATE`, `DELETE`, `SELECT`. *Fuente: Microsoft Learn – INSERT / SELECT.*

```sql
-- INSERT: agrega una fila a Paciente (tabla distinta a las demás operaciones)
INSERT INTO Paciente (Nom_Pac, Dir_Pac, Tel_Pac, Edad_Pac)
VALUES ('Carlos Ruiz', 'Calle 7', '555-1234', 45);

-- UPDATE: modifica un paciente (USA WHERE para no tocar todos) ✔
UPDATE Paciente SET Tel_Pac = '555-9999' WHERE Id_Pac = 8;

-- DELETE: elimina un paciente (USA WHERE) ✔
DELETE FROM Paciente WHERE Id_Pac = 8;

-- SELECT: recupera información
SELECT Nom_Med, Especialidad FROM Médico WHERE Especialidad = 'Cardiología';
```

**7. ¿Diferencia entre `DELETE` y `DROP TABLE`?**
- `DELETE`: **DML** elimina **filas** (una o todas con WHERE); conserva la tabla y los IDENTITY; activa triggers; es reversible con `ROLLBACK`.
- `DROP TABLE`: **DDL** elimina **toda la tabla** (estructura + datos) de una sola vez; es irreversible (pierde índices/restricciones).
*Fuente: Microsoft Learn – DELETE / ALTER TABLE.*

**8. ¿Diferencia entre `DELETE` y `TRUNCATE`?**
- `DELETE`: DML, **fila a fila**, puede usar `WHERE`, activa triggers, conserva el valor de IDENTITY.
- `TRUNCATE`: DDL, **rápido** (desasigna páginas), **no usa WHERE** (borra todo), **no activa triggers**, **reinicia** la semilla de IDENTITY. Requiere menos registro de transacciones.
> ⚠️ `TRUNCATE` **no funciona si la tabla está referenciada por una FK** (a menos que se usen `DELETE`/`CASCADE`).

**9. ¿Riesgo de `UPDATE` sin `WHERE`?**
Actualiza **todas las filas** de la tabla → pérdida masiva de datos (ej. poner el mismo costo a todos los servicios). Siempre usar `WHERE` salvo que se quiera modificar todo a propósito.

**10. ¿Riesgo de `DELETE` sin `WHERE`?**
Borra **todas las filas** de la tabla → datos irrecoverables. Usar siempre `WHERE` o, mejor, una transacción explícita (`BEGIN TRAN … ROLLBACK`). *Fuente: Microsoft Learn – UPDATE / DELETE.*

**11. ¿Diferencia entre `SELECT *` y seleccionar columnas específicas?**
- `SELECT *`: trae **todas** las columnas → costoso, propenso a romperse si se reordenan/reordenan columnas y expone columnas sensibles.
- Elegir columnas (`SELECT col1, col2`): **más rápido**, explícito, seguro y estable ante cambios de esquema.

### Claves y relaciones

**12. ¿Qué es una Primary Key?**
Una **clave primaria** es una columna (o conjunto) que **identifica de forma única** cada fila. Es implícitamente `NOT NULL` y `UNIQUE`. Se declara a nivel columna o tabla con `CONSTRAINT pk PRIMARY KEY (col)`. *Fuente: Microsoft Learn – CREATE TABLE.*

**13. ¿Qué es una Foreign Key?**
Una **clave foránea** es una columna (o conjunto) que **hace referencia a la PK de otra tabla**, garantizando **integridad referencial**: no se puede insertar/actualizar un valor FK que no exista como PK en la tabla padre (ni borrar un padre que tenga hijos, salvo acciones como `CASCADE`). *Fuente: Microsoft Learn – CREATE TABLE (FOREIGN KEY).*

**14. ¿Por qué `Clave_Hospital` puede ser FK en Médico y `Cve_Hos` PK en Hospital?**
`Cve_Hos` es la PK de **Hospital** (identifica al hospital). En **Médico**, `Clave_Hospital` **hace referencia** a `Cve_Hos`: cada médico "pertenece a" un hospital que ya existe. Por eso `Clave_Hospital` es **FK** de Médico que referencia la **PK** de Hospital. Un médico → un hospital (many-to-one). *Fuente: Microsoft Learn – CREATE TABLE (FOREIGN KEY).*

**15. ¿Es obligatorio que PK y FK tengan el mismo nombre?**
**No.** El nombre de la restricción y de las columnas es independiente. lo que importa es que la **columna FK tenga el mismo tipo y longitud** que la **columna PK referenciada**. `Clave_Hospital` ≠ `Cve_Hos` es perfectamente válido. (Los nombres sirven para legibilidad, no para el mecanismo.)

**16. ¿Qué problema si se inserta en Médico un `Clave_Hospital` que no existe en Hospital?**
El motor **rechaza** la inserción con un error de **integridad referencial** (`reference constraint conflict`). No se permite un médico "huhalado" a un hospital inexistente — es la garantía de la FK. *Fuente: Microsoft Learn – CREATE TABLE (FOREIGN KEY).*

**17. ¿Qué es la integridad referencial?**
Mecanismo que **mantiene la coherencia** entre PK y FK: impide valores FK huérfanos, evita inconsistencias (médico sin hospital, consulta sin médico…). Se implementa con la restricción `FOREIGN KEY ... REFERENCES` y acciones `ON DELETE/UPDATE`. *Fuente: Microsoft Learn – CREATE TABLE.*


### Funciones y variables

**18. ¿Qué función se utiliza para obtener un promedio?**
`AVG()` — devuelve el **promedio aritmético** de una columna numérica. *Fuente: Microsoft Learn – funciones de agregación.*

**19. ¿Diferencia entre `COUNT(*)` y `COUNT(columna)`?**
- `COUNT(*)`: cuenta **todas las filas** (incluidos los nulos).
- `COUNT(columna)`: cuenta solo las filas donde `columna` **no es NULL** (ignora nulos).
```sql
SELECT COUNT(*) AS TotalMédicos, COUNT(Edad_Med) AS ConEdad FROM Médico;
```

**20. ¿Qué significa declarar una variable con `DECLARE`?**
`DECLARE @var tipo` **reserva** una variable de sesión con ese tipo. En SQL Server se usa `DECLARE` fuera de los batches dentro del mismo lote; luego se asigna con `SET` o con `=` dentro de `SELECT`. *Fuente: Microsoft Learn – DECLARE @local_variable.*

**21. ¿Qué significa el símbolo `@` en una variable de SQL Server?**
Indica que se trata de una **variable local** (ej. `@Total`). Es la convención obligatoria de SQL Server; sin `@` el nombre se interpreta como columna.

### DCL

**22. ¿Qué significa DCL?**
DCL = *Data Control Language*. Administra **permisos y seguridad** de la base de datos: `GRANT` (otorga) y `REVOKE`/`DENY` (quita/niega). *Fuente: Microsoft Learn – GRANT / REVOKE.*

**23. ¿Diferencia entre `GRANT` y `REVOKE`?**
- `GRANT`: **otorga** un permiso a un principal.
- `REVOKE`: **quita** un permiso previamente concedido (no lo niega explícitamente, simplemente lo elimina). `DENY` va más allá: **niega** el permiso (prioridad sobre grants). *Fuente: Microsoft Learn – GRANT / REVOKE.*

**24. ¿Qué función cumple `WITH GRANT OPTION`?**
Permite al **receptor** del permiso **volver a otorgarlo** a otros principales. Es una delegación controlada del derecho a conceder. *Fuente: Microsoft Learn – GRANT.*

**25. ¿Qué significa usar `CASCADE` al retirar privilegios?**
`REVOKE ... CASCADE` quita el permiso al principal **y también anula los derechos que ese principal había concedido a otros** (porque dependían de su cadena de concesión). Sin `CASCADE`, solo se le quita al receptor directo. *Fuente: Microsoft Learn – REVOKE (transact-sql).*

**26. ¿Diferencia entre un Login y un User en SQL Server?**
- **Login (nivel servidor):** principal de seguridad que **inicia sesión en la instancia** (`CREATE LOGIN …`). Puede ser de SQL Server (contraseña) o de Windows.
- **User (nivel base de datos):** principal que **accede a una base de datos concreta**; se **mapea** a un login (`CREATE USER … FOR LOGIN …`). Un mismo login puede mapearse a varios users; un user puede existir *sin login* (`WITHOUT LOGIN`, contenedor). *Fuente: Microsoft Learn – CREATE LOGIN.*

### Triggers

**27. ¿Qué es un trigger?**
Un **trigger** es un **procedimiento almacenado especial** que **se ejecuta automáticamente** cuando ocurre un evento DML (`INSERT`, `UPDATE`, `DELETE`), DDL o de inicio de sesión en una tabla/vista **sin llamada explícita**. *Fuente: Microsoft Learn – CREATE TRIGGER.*

**28. ¿Principal diferencia entre trigger y procedure?**
El trigger **se dispara solo** ante un evento y **no puede recibir parámetros**; el procedure se **llama explícitamente con `EXEC`** y puede recibir parámetros, devolver valores y ser reutilizado bajo demanda. Un trigger tampoco devuelve resultados directamente.

**29. ¿Cuándo se ejecuta un `AFTER INSERT`?**
Inmediatamente **después** de que se complete un `INSERT` exitoso en la tabla, dentro de la misma transacción. Allí la tabla lógica **`inserted`** contiene las filas nuevas.

**30. ¿Cuándo se ejecuta un `AFTER UPDATE`?**
Inmediatamente **después** de un `UPDATE` exitoso. La tabla **`inserted`** contiene los valores **nuevos** y **`deleted`** los valores **viejos** (estado previo).

**31. ¿Cuándo se ejecuta un `AFTER DELETE`?**
Inmediatamente **después** de un `DELETE` exitoso. La tabla **`deleted`** contiene las filas **eliminadas** (no existe `inserted`).

**32. ¿Qué información contienen las tablas lógicas `inserted` y `deleted`?**
- `inserted`: filas **nuevas** que entraron por `INSERT`/`UPDATE`.
- `deleted`: filas **viejas** removidas por `DELETE`/`UPDATE`.
SQL Server las crea automáticamente **dentro** del scope del trigger y son solo de lectura. *Fuente: Microsoft Learn – DML triggers.*

**33. ¿Por qué un trigger es útil para una bitácora de cambios?**
Porque se **activa automáticamente** en cada cambio y tiene **`inserted`/`deleted`** para conocer los valores antes/después → puede registrar *quién, qué y cuándo* sin depender del programador:
```sql
CREATE TRIGGER tr_Audita_Paciente ON Paciente
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO Bitacora_Paciente (Id_Pac, Accion, Fecha_Auditoria)
    SELECT Id_Pac, 'INSERT/UPDATE/DELETE', GETDATE()  -- 'inserted' y 'deleted'
    FROM   inserted;
END;
```

### Procedures

**34. ¿Qué es un procedimiento almacenado?**
Un **procedure** es una colección de instrucciones SQL **guardada** en la base de datos que se **ejecuta con `EXEC`** y puede recibir/evaluar parámetros. Centraliza lógica, mejora el rendimiento (plan precompilado) y simplifica la seguridad. *Fuente: Microsoft Learn – CREATE PROCEDURE.*

**35. ¿Cuáles son las ventajas de los procedures?**
1. **Reutilización** del código (se escribe una vez, se llama N veces).
2. **Rendimiento**: plan de ejecución **precompilado** y cacheado.
3. **Seguridad**: el usuario ejecuta el procedure sin permiso directo sobre tablas.
4. **Menos tráfico** y mantenimiento centralizado.
5. Reciben **parámetros** de entrada y pueden devolver valores/sets de resultados.

**36. ¿Qué son los parámetros de un procedure?**
Son **variables declaradas** en la definición (`@Param tipo [= default] [OUTPUT]`) que el caller pasa al ejecutar. Pueden ser de **entrada** (valores para usar) o de **salida** (`OUTPUT`). *Fuente: Microsoft Learn – CREATE PROCEDURE.*

**37. ¿Cómo se ejecuta un procedure?**
Con `EXEC` o `EXECUTE` (por posición u omitiendo el nombre del valor con `@Param=valor`):
```sql
EXEC sp_InsertarMédico 'Dra. Ruiz', 'Pediatría', 2;
EXEC sp_ConsultasPaciente @Id_Pac = 5;   -- pasar por nombre
```

**38. ¿Diferencia entre procedure y función?**
- **Procedure**: puede contener cualquier instrucción (`INSERT/UPDATE/DELETE`), no devuelve un valor si no mediante parámetros `OUTPUT` o sets de resultados; contiene lógica de flujo (`IF`, `TRX`).
- **Función escalar/tabla**: **siempre devuelve un valor** (escalar o tabla), es **determinística/sin efectos secundarios** (no puede modificar datos), y por ello se puede usar dentro de `SELECT`, `WHERE`, etc.
- También: **procedure vs trigger**: el procedure se llama con `EXEC`; el trigger se **autoactiva**.

### Vistas

**39. ¿Qué es una vista?**
Una **vista** es una **tabla virtual** definida por una consulta `SELECT` guardada. No almacena los datos: **ejecuta la consulta** cada vez que se usa. *Fuente: Microsoft Learn – CREATE VIEW.*

**40. ¿Una vista almacena físicamente los datos de la consulta?**
**No.** Una vista es una **consulta guardada**; los datos viven en las **tablas base**. Al consultarla, la vista **re-ejecuta el `SELECT`** y muestra resultados actualizados en tiempo real.

**41. ¿Diferencia entre una tabla y una vista?**
- **Tabla**: almacena datos físicamente; ocupa espacio; se inserta/actualiza directamente.
- **Vista**: **no almacena**, es una consulta guardada; no ocupa espacio por datos; se consulta como tabla; sobre ella se puede (con reglas) hacer solo UPDATE/INSERT en algunos casos.

**42. ¿Qué ventaja tiene una vista para combinar tres tablas?**
**Simplifica** el acceso: el usuario hace `SELECT * FROM vw_reporte` en lugar de escribir repetidamente el `INNER JOIN` de 3 tablas, y **oculta** la complejidad del esquema.

**43. ¿Qué hace `INNER JOIN`?**
**Une filas de dos tablas que cumplen la condición `ON`**; solo se devuelven las filas **con coincidencia en ambos lados** del join. Las filas sin pareja se descartan. *Fuente: Microsoft Learn – queries with joins.*

**44. ¿Qué sucede con un registro sin coincidencia en un `INNER JOIN`?**
**Se descarta** del resultado (no aparece), porque `INNER JOIN` solo conserva filas que tienen pareja en la otra tabla.

**45. ¿Qué ventajas de seguridad pueden proporcionar las vistas?**
Permiten **exponer solo ciertas columnas/filas** y **ocultar las tablas base**: se concede permiso sobre la vista y se deniega el acceso directo a las tablas → los usuarios ven únicamente lo autorizado. *Fuente: Microsoft Learn – CREATE VIEW.*

---

## 📚 Preguntas de análisis — Nivel examen universitario

**46. Un médico pertenece a un hospital ya eliminado. ¿Qué problema de integridad referencial se presenta?**
**Violación de integridad referencial**: existe un **niño huérfano** (el médico) cuya FK (`Clave_Hospital`) apunta a una PK que ya no existe. Para prevenirlo, al borrar un `Hospital` con médicos SQL Server arroja un error (`ON DELETE NO ACTION`) y **rechaza** el borrado, o (si se usa `ON DELETE CASCADE`) borra también los médicos. Borrar un padre con hijos sin responder es la inconsistencia que la FK impide.

**47. Un estudiante ejecuta `UPDATE Paciente SET Edad_Pac = 30;` ¿Qué ocurre y por qué?**
Actualiza **la edad de TODOS los pacientes a 30** porque **no hay cláusula `WHERE`**. De forma implícita SQL aplicar el `SET` a cada fila de la tabla. Resultado: todos los pacientes quedan con `Edad_Pac=30`. Evidentemente un error de lógica de negocio muy grave, evitable con `WHERE Id_Pac = ...`.

**48. `DELETE FROM Paciente;` ¿Qué efecto tendrá?**
Borra **todas las filas** de `Paciente` (porque no hay `WHERE`). La tabla **queda vacía** pero **conserva su estructura** (columnas, IDENTITY…). Es irreversible si no hay transacción/backup. (A diferencia de `TRUNCATE`, si hay FK que apunte a Paciente puede fallar.)

**49. ¿Por qué `Consulta_Medicamento` necesita una clave primaria compuesta?**
Porque cada fila representa la **asociación** entre una consulta y un medicamento; **ninguna columna por sí sola es única** (una consulta tiene varios medicamentos y un medicamento está en varias consultas). Solo el **par** `(Consulta, Medicamento)` identifica de forma única cada asociación → **PK compuesta**. Además evita duplicar la misma relación.

**50. Si una consulta puede tener varios medicamentos y un medicamento en varias consultas, ¿qué relación existe?**
Una relación **N:M (muchos a muchos)** entre `Consulta` y `Medicamento`.

**51. ¿Por qué se necesita una tabla intermedia para resolver esa relación?**
Porque un modelo relacional **no representa N:M directamente** con dos tablas; la **tabla intermedia** (`Consulta_Medicamento`) **descompone la N:M en dos relaciones 1:N** (Consulta 1:N intermedia y Medicamento 1:N intermedia), eliminando redundancias y permitiendo la PK compuesta. *Concepto de diseño lógico / normalización.*

**52. ¿Qué sucedería si se almacenaran varios medicamentos directamente en una columna de Consulta?**
Se violaría la **2FN** y la **atomicidad**: habría un **grupo repetitivo** (varios valores en una celda), imposible de consultar/agregar con SQL estándar, con **redundancia** y difícil de mantener. Es justo lo que evita la tabla intermedia normalizada.

**53. ¿Qué ventajas ofrece una vista para consultar Paciente, Médico y Consulta?**
1. **Simplifica** el acceso (no repetir el INNER JOIN de 3 tablas).
2. **Seguridad**: oculta datos sensibles de las tablas base.
3. **Consistencia**: un solo lugar definido para el reporte.
4. **Independencia lógica** ante cambios de esquema en las tablas base.

**54. ¿Cuándo usar un procedure y cuándo un trigger?**
- **Procedure**: cuando se quiere una **operación bajo demanda** reutilizable con parámetros (ej. `sp_InsertarMédico`). Se le llama con `EXEC`.
- **Trigger**: cuando se quiere una **reacción automática e incondicional** ante un evento DML (ej. auditoría de cada INSERT, validación de edad). No se llama; se dispara solo.
En el hospital: procedure para el CRUD que el personal invoca; trigger para auditar/garantizar invariantes automáticamente.

**55. ¿Por qué una BD hospitalaria necesita seguridad y control de permisos?**
Porque maneja **datos sensibles** (expedientes clínicos: salud, datos personales) protegidos por ley. Se debe restringir **quién** ve/modifica qué (solo médicos autorizados, no todo el personal), auditar cambios (triggers) y aplicar el **principio de menor privilegio** mediante DCL (`GRANT`/`REVOKE`) y roles (`db_datareader`/`db_datawriter`).

---

## 📚 Preguntas de desarrollo

**56. Diferencia entre DDL, DML y DCL (2 ejemplos cada una).**
- **DDL** (estructura): `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`.
- **DML** (datos): `INSERT`, `UPDATE`, `DELETE`, `SELECT`.
- **DCL** (permisos): `GRANT`, `REVOKE`.
```sql
-- DDL
CREATE TABLE Médico (...);          ALTER TABLE Médico ADD Correo nvarchar(80);
-- DML
INSERT INTO Médico (...) VALUES (...);   UPDATE Médico SET Especialidad='X' WHERE Id_Med=1;
-- DCL
GRANT SELECT ON Médico TO usuario;      REVOKE SELECT ON Médico FROM usuario;
```

**57. ¿Cómo se relacionan Hospital y Médico mediante PK y FK?**
`Hospital.Cve_Hos` es la **PK** (identifica al hospital). En `Médico`, la columna `Clave_Hospital` es **FK** que `REFERENCES Hospital(Cve_Hos)`. Relación **1:N**: un hospital tiene muchos médicos; cada médico pertenece a **un solo** hospital. La FK garantiza que todo médico apunte a un hospital existente.

**58. ¿Qué ocurre paso a paso al insertar una nueva consulta médica?**
1. Se cancela/lanza `INSERT INTO Consulta (...)` con `IDN_Med`, `Identificador_Pac`, `Clave_Ser`, fecha y hora.
2. El motor **valida las 3 FK**: que `IDN_Med` exista en `Médico`, `Identificador_Pac` en `Paciente` y `Clave_Ser` en `Servicio`. Si alguna no existe → **error de integridad referencial** y no se inserta.
3. Se asigna `Cve_Con` automáticamente (`IDENTITY`).
4. Se dispara el **trigger AFTER INSERT** (`tr_Audita_Consulta_Insert`) que registra la operación en `Bitacora_Consultas` usando `inserted`.
5. Se confirma la fila (COMMIT implícito) y queda disponible para consultas/reportes.

**59. ¿Cómo usarías una vista para un reporte con Paciente, Médico, Fecha, Servicio y Costo?**
```sql
CREATE VIEW vw_ReportePacientes AS
SELECT p.Nom_Pac AS Paciente,
       m.Nom_Med AS Médico,
       c.Fecha_Con AS Fecha,
       s.Descripción AS Servicio,
       s.Costo
FROM   Paciente p
INNER JOIN Consulta c ON c.Identificador_Pac = p.Id_Pac
INNER JOIN Médico m   ON c.IDN_Med = m.Id_Med
INNER JOIN Servicio s ON c.Clave_Ser = s.Cve_Ser;
-- Consulta posterior:
SELECT * FROM vw_ReportePacientes WHERE Costo > 500 ORDER BY Fecha DESC;
```

**60. ¿Por qué el diseño debe realizarse antes de insertar información?**
Porque los **datos dependen de la estructura**: si no se definen antes las **tablas, PK, FK y restricciones** (integridad referencial, dominio), se ingresan datos **inconsistentes** (médicos sin hospital, edades inválidas) que luego son **muy costosos** de corregir/limpiar. Diseñar primero garantiza que la BD **acepte solo datos válidos** y cumpla el modelo relacional del problema.

---

## 🧠 Asociación final para memorizar (regla rápida)

```text
SQL
├── DDL → Estructura 🏗️   CREATE / ALTER / DROP
├── DML → Datos 📊         INSERT / UPDATE / DELETE / SELECT
├── DCL → Permisos 🔐      GRANT / REVOKE
├── TCL → Transacciones 🔄 COMMIT / ROLLBACK
├── PK  → Identifica 🔑
├── FK  → Relaciona 🔗
├── TRIGGER → Automático ⚡ (inserted/deleted, sin parámetros)
├── PROCEDURE → Reutilizable 📦 (EXEC + parámetros)
└── VIEW → Consulta guardada 👁️ (no almacena)
```

> **Regla rápida:** *DDL construye, DML manipula, DCL protege, PK identifica, FK relaciona, Trigger reacciona, Procedure reutiliza y View muestra.*

---

## 🚨 Simulacro Visual de Emergencia (10 respuestas rápidas)

1. ¿Qué instrucción crea la estructura de `Médico`? → `CREATE TABLE` (DDL).
2. ¿Cómo se enlaza `Médico.Clave_Hospital`? → **FK** `REFERENCES Hospital(Cve_Hos)`.
3. ¿`UPDATE` sin `WHERE`? → Actualiza **toda** la tabla (peligro).
4. ¿Qué tabla lógica contiene las filas "viejas" en un `DELETE`? → `deleted`.
5. ¿Cómo se llama un procedure? → `EXEC`.
6. ¿Una vista almacena físicamente los datos? → **No**.
7. ¿`INNER JOIN` conserva filas sin coincidencia? → **No** (solo las que coinciden).
8. ¿Diferencia Login vs User? → Login = nivel servidor; User = nivel base de datos (mapea al login).
9. ¿Cuál tabla resuelve la N:M Consulta↔Medicamento? → `Consulta_Medicamento` (PK compuesta).
10. ¿Qué hace `REVOKE ... CASCADE`? → Quita el permiso también a los propagados.

**RESPUESTAS:** 1) `CREATE TABLE` · 2) FK → `REFERENCES Hospital(Cve_Hos)` · 3) Toda la tabla · 4) `deleted` · 5) `EXEC` · 6) No · 7) No · 8) Login=servidor, User=BD · 9) `Consulta_Medicamento` · 10) Revoca en cascada.

---

*Guía terminada. Todas las respuestas se basan en la documentación oficial de Microsoft Learn (Transact-SQL, SQL Server) e incorporan la metodología visual ParetoTutor: 🔵 concepto, 🟠 fórmula, 🟢 ejemplo, 🔴 trampa.*