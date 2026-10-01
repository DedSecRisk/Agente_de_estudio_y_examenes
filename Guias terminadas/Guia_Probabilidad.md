# GUÍA DE ESTUDIO OFFLINE: PROBABILIDAD

> **Resumen del análisis:** Se procesaron **8 exámenes únicos** extraídos de 10 imágenes (`Proba 1`–`Proba 10`, con 2 pares duplicados) y el libro de referencia *Probabilidad y Estadística* (388 pp.). Frecuencia de aparición de temas:

| Tema | Frecuencia (de 8 exámenes) | Prioridad |
|---|---|---|
| Teorema de Probabilidad Total y Bayes | 6 | Alta |
| Distribución Normal | 6 | Alta |
| Distribución Binomial (y su aprox. normal/Poisson) | 6 | Alta |
| Variable Aleatoria Continua / Función de densidad (cálculo de k) | 4 | Alta |
| Variable Aleatoria Discreta (tabla, esperanza, varianza) | 4 | Alta |
| Distribución Exponencial | 4 | Alta |
| Probabilidad Condicional e Independencia | 3 | Media |
| Distribución Geométrica | 3 | Media |
| Distribución de Poisson | 2 | Media |
| Análisis Combinatorio / Permutaciones | 2 | Baja |
| Distribución Hipergeométrica | 1 | Baja |

> **Nota:** Todos los temas de la tabla (los 6 de Prioridad Alta y también los de Prioridad Media/Baja: Condicional, Geométrica, Poisson, Hipergeométrica y Combinatoria) cuentan con su sección completa en esta guía, con el mismo formato de Concepto, Trampas, Visualización, Ejemplo Teórico, Ejercicio Práctico y Claves.

**Top 20% (garantizan 7/10):** Bayes + Probabilidad Total, Normal, Binomial (con aprox. normal/Poisson) y Exponencial. Con estos dominas gran parte de los reactivos típicos de examen.

---

## 📌 Teorema de Probabilidad Total y Teorema de Bayes
**1. Concepto en breve:** La *probabilidad total* P(A) suma las "ramas" que llevan a un mismo resultado A partiendo de causas mutuamente excluyentes (B1, B2, ..., Bn). *Bayes* invierte la pregunta: si ya ocurrió A, ¿qué probabilidad hay de que haya venido de una causa concreta (Bk)? Son el anverso y reverso del mismo árbol.

**2. Trampas del examen:** Aparecen en casi todos los exámenes (Proba 1, 2, 4, 6, 7, 8). Suelen disfrazar a Bayes con historias: "un producto defectuoso salió de tal máquina", "a qué caja pertenece la bola", "qué aeropuerto es". La trampa clásica es confundir P(B|A) con P(A|B): lee SIEMPRE el texto ("probabilidad de que provenga de X" → denominador = P(elegir X)·P(resultado|X), numerador = esa misma rama).

**3. Visualización:**
```
Probabilidad total                  Bayes
   B1 ─(p1)─> A                     Queremos P(Bk|A)
   B2 ─(p2)─> A      P(A) =          P(Bk)·P(A|Bk)
   B3 ─(p3)─> A      p1+p2+p3        P(Bk|A) = ─────────────
   ...                                p1+p2+p3+... (todo el árbol)
```

**4. Ejemplo Teórico:** *"Define el teorema de probabilidad total y enuncia el de Bayes (Cap. 1 del libro)."*
**Respuesta:** Si A resulta de uno de los sucesos mutuamente excluyentes B1,...,Bn cuya unión es el espacio muestral, entonces P(A) = Σ P(Bi)·P(A|Bi). El Teorema de Bayes plantea la probabilidad inversa: P(Bk|A) = [P(Bk)·P(A|Bk)] / Σ P(Bi)·P(A|Bi).

**5. Ejercicio Práctico (estilo examen):**
Una fábrica tiene 3 máquinas. M1 produce 50%, M2 30%, M3 20% de las piezas. % defectuosas: M1=3%, M2=4%, M3=5%. Se elige una pieza al azar. (a) ¿Probabilidad de que sea defectuosa? (b) Si resultó defectuosa, ¿qué probabilidad de que proceda de M1?
(a) P(D) = 0.50·0.03 + 0.30·0.04 + 0.20·0.05 = 0.015+0.012+0.010 = **0.037 (3.7%)**.
(b) P(M1|D) = (0.50·0.03)/(0.037) = 0.015/0.037 = **≈ 0.4054 (40.5%)**.

**6. Claves / Formulario:**
- Probabilidad total: `P(A) = P(B1)·P(A|B1) + P(B2)·P(A|B2) + ...`
- Bayes: `P(Bk|A) = [P(Bk)·P(A|Bk)] / P(A)` (divide la rama buscada entre la total).
- Regla de oro: el denominador de Bayes = P(A) total.

---
## 📌 Distribución Binomial (y su aproximación Normal / Poisson)
**1. Concepto en breve:** Modela el número de "éxitos" X en n ensayos independientes con probabilidad fija p (p.ej. acertar, aprobar, defecto). Cada resultado interesa "exactamente X", "a lo más" o "al menos". Fórmula: P(X=r) = C(n,r)·p^r·(1−p)^(n−r).

**2. Trampas del examen:** Los problemas (Proba 1, 3, 4, 6, 7: tiro al blanco, examen de opción múltiple, tornillos defectuosos) exigen traducir *"al menos 2" = 1 − P(0) − P(1)*, y *"más de 5"* con la aproximación normal. Cuidado: cuando p es pequeña y n grande, la binomial tiende a **Poisson (λ=np)**.

**3. Visualización:**
```
n=3, p=0.4  (q=0.6)
P(r=1) = C(3,1)·0.4^1·0.6^2 = 3·0.4·0.36 = 0.432
 Media μ = n·p
 Desvío σ = √(n·p·q)
```

**4. Ejemplo Teórico:** *"¿En qué consiste la aproximación de la distribución binomial a la normal? Menciona la condición práctica."*
**Respuesta:** si n es grande y tanto np como nq > 5, la binomial se aproxima a la normal con variable tipificada z = (X−np)/√(npq); con ello puedes calcular probabilidades de varios valores discretos.

**5. Ejercicio Práctico:** Un tirador acierta con probabilidad 0.6. Dispara 5 veces. (a) Probabilidad de "exactamente 3 aciertos". (b) Probabilidad de "al menos 2 aciertos".
(a) C(5,3)·0.6³·0.4² = 10·0.216·0.16 = **0.3456**.
(b) P(al menos 2) = 1 − [P(0)+P(1)] = 1 − [0.4⁵ + 5·0.6·0.4⁴] = 1 − [0.01024 + 0.07680] = **0.91296**.

**6. Claves / Formulario:**
- P(X=r) = C(n,r)·p^r·(1−p)^(n−r); P(al menos k) = 1 − Σ (menores a k).
- Media μ = n·p; varianza σ² = n·p·q; desvío σ = √(npq).
- Normal si np y nq > 5; Poisson (λ=np) si p pequeña (np < 5).

---

## 📌 Distribución Normal (y tipificación z)
**1. Concepto en breve:** Es la distribución continua en forma de campana (gaussiana), con media μ y desvío σ. Para resolver se **tipifica**: z = (x−μ)/σ, y luego se busca en la tabla de la normal estándar N(0,1). Se usa en Proba 1, 3, 6, 8 (tamaños de tornillos, tiempo de camioneta, peso, etc.).

**2. Trampas del examen:** Piden hallar probabilidades acumuladas (P(X<30), P(X entre...)) y a veces "despejar el valor": dado el percentil, hallar el dato. Trampa: complementar con P = 1 − (tabla) cuando piden "mayor que". No olvides tipificar antes de leer la tabla; si z sale negativo, usa simetría.

**3. Visualización:**
```
      N(μ,σ)                N(0,1)
         /\
        /  \      z=(x−μ)/σ
   μ    |  |      0    →   tabla Φ(z)
     (campana simétrica; área total = 1)
```

**4. Ejemplo Teórico:** *"¿Qué es tipificar una variable normal?"*
**Respuesta:** convertir X (de media μ y desvío σ cualesquiera) en una normal estándar Z con μ=0 y σ=1, mediante z=(x−μ)/σ, para poder usar la única tabla N(0,1).

**5. Ejercicio Práctico:** El peso de un empaque se distribuye N(25, σ=4). (a) P(X<30): z=(30−25)/4=1.25; P(z<1.25)=**0.8944**. (b) ¿Cuánto pesa el percentil 90 (debajo de él cae el 90%)? z=1.28 → x=μ+z·σ=25+1.28·4 = **30.12 kg**.

**6. Claves / Formulario:**
- z=(x−μ)/σ; P(X<x)=Φ(z); P(X>x)=1−Φ(z).
- Simetría: Φ(−z)=1−Φ(z).
- Percentil k: x=μ+z_k·σ con z_k sacado de la tabla.

---
## 📌 Distribución Exponencial
**1. Concepto en breve:** Modela el tiempo de espera entre llegadas o la vida útil de equipos. Si X ~ exponencial con parámetro λ = 1/μ (media μ), la probabilidad de que supere un tiempo x es P(X > x) = e^(−λx) y la acumulada P(X < x) = 1 − e^(−λx). Aparece en Proba 3, 4, 6, 7 (tiempo de parqueo, vida de un televisor, llamadas, etc.).

**2. Trampas del examen:** Frecuente confundir "media = μ" con "parámetro λ": si te dan la media, primero λ = 1/μ. Cuando piden P(X > t) se usa directo e^(−λt); cuando piden P(X < t) o "entre a y b" se usa 1 − e^(−λt) o la diferencia de acumuladas. No inviertas los papeles.

**3. Visualización:**
```
f(x) = λ e^(−λx)   (x≥0)
      |.
      | .
      |   .        P(X > t) = e^(−λt)  (área a la derecha de t)
      |    .́
      |     ...
      +------------------ t -------
```

**4. Ejemplo Teórico:** *"¿Cuál es el parámetro de la distribución exponencial y cómo se obtiene a partir del tiempo medio?"*
**Respuesta:** la exponencial tiene parámetro λ (tasa), y la media es 1/λ; por tanto λ = 1/media. La varianza vale 1/λ².

**5. Ejercicio Práctico:** La vida de un componente es exponencial con media 8 años. (a) P(que dure más de 10 años): λ=1/8; P(X>10)=e^(−10/8)=e^(−1.25)=**0.2865**. (b) P(que falle antes de 4 años): P(X<4)=1−e^(−0.5)=**0.3935**.

**6. Claves / Formulario:**
- λ = 1/μ (media); Jamás uses μ como λ.
- Supervivencia: P(X>t) = e^(−λ t); falla prematura: P(X<t)=1−e^(−λt).
- Media = 1/λ; varianza = 1/λ².

---

## 📌 Variable Aleatoria Continua (función de densidad, cálculo de k)
**1. Concepto en breve:** En distribución continua (p.ej. `f(x)=k·g(x)` en un intervalo), el área bajo la curva entre a y b da P(a<X<b). Primero se calcula **k** con ∫ f(x) dx = 1 (probabilidad total = 1), y luego se integra para hallar probabilidades y esperanzas (µ = ∫ x·f(x) dx).

**2. Trampas del examen:** En Proba 1, 3, 4, 6 piden "determina la constante k" integrando entre los extremos del dominio y luego "calcula P en un intervalo". Trampa: olvidar que el área total DEBE valer 1 antes de calcular cualquier probabilidad.

**3. Visualización:**
```
f(x)=k·x² en [0,3]
  ∫₀³ k·x² dx = k·[x³/3]₀³ = k·(27/3) = 9k
  9k = 1  ⇒  k = 1/9
```

**4. Ejemplo Teórico:** *"¿Por qué debe cumplirse que ∫ f(x) dx = 1 en toda distribución de densidad?"*
**Respuesta:** es la probabilidad total del suceso seguro; el área bajo la función de densidad en todo el espacio muestral debe sumar 1.

**5. Ejercicio Práctico:** Saques X con densidad f(x)=k·x² en [0,3]. (a) halla k; (b) P(1<X<2). (a) ∫₀³ k x² dx = 9k = 1 → **k=1/9**. (b) P = (1/9)·∫₁² x² dx = (1/9)·(8/3 − 1/3) = (1/9)·(7/3) = **7/27 ≈ 0.259**.

**6. Claves:** - k: ∫ f(x) dx (todo el dominio) = 1. - P(a<X<b) = ∫ₐ f(x) dx. - E(X) = ∫ x·f(x) dx.
## 📌 Variable Aleatoria Discreta (tabla, esperanza, varianza)
**1. Concepto en breve:** En variable discreta, X toma valores enteros (lanzar dados, número de eventos) con probabilidades p(x) en un tabla. La suma de p(x) = 1. La esperanza E(X) = Σ x·p(x) y la varianza Var(X) = Σ x²·p(x) − [E(X)]².

**2. Trampas del examen:** En Proba 1, 3, 5 piden "construir la distribución de probabilidad y hallar E(X) y/o Var(X)" para un experimento (p.ej. suma de dos dados, divisores/múltiplos). Trampa: no respetar que Σ p = 1 y aplicar mal la fórmula de la varianza (restar E al cuadrado al final).

**3. Visualización (suma de dos dados):**
```
Suma  2:1/36  3:2/36  4:3/36 ... 7:6/36 ... 12:1/36
E(X) = Σ x·p(x);  Var(X) = Σ x²·p(x) − E(X)²
```

**4. Ejemplo Teórico:** *"Define esperanza matemática y varianza de una variable aleatoria discreta."*
**Respuesta:** E(X) es la media poblacional, E(X)=Σ x·p(x). Var(X) mide la dispersión, Var(X)=E(X²)−[E(X)]².

**5. Ejercicio Práctico:** Sea X la sumatoria de dos dados. Halla E(X). Los valores 2,...,12 con p=(1,2,3,4,5,6,5,4,3,2,1)/36. E(X)=Σ x·p = 252/36 = **7**. (Var(X)=35/6 aprox.).

**6. Claves / Formulario:**
- Σ p(x) = 1 (siempre verifícalo al construir la tabla).
- E(X) = Σ x·p(x); media del juego = Σ x·p(x).
- Var(X) = Σ x²·p(x) − (E(X))².

---

## 📌 Probabilidad Condicional e Independencia
**1. Concepto en breve:** P(B|A) es la probabilidad de B **dado que** ya ocurrió A, e "informa" que el espacio muestral se reduce a A. Fórmula clave: P(A∩B)=P(A)·P(B|A); si P(A∩B)=P(A)·P(B), los sucesos son independientes (A no aporta información a B).

**2. Trampas del examen:** Aparece en Proba 1 y 5, sobre todo con "sin reemplazo" y "con reemplazo" (cartas, bolas). Con reemplazo las extracciones son independientes (nº de cartas constante); sin reemplazo el denominador baja en 1 cada vez y la probabilidad cambia. No la confundas con Bayes: aquí NO hay "causas previas".

**3. Visualización:**
```
Con remplazo            Sin remplazo (baraja de 52)
P(A rey)=4/52           P(rey 2º | rey 1º) = 3/51
P(rey 2º)=4/52          (queda 1 as menos y 51 cartas)
independientes          cambia el denominador cada vez
P(A∩B)=P(A)·P(B)        P(A∩B)=P(A)·P(B|A)
```

**4. Ejemplo Teórico:** *"¿Cuándo se dice que dos sucesos A y B son independientes?"*
**Respuesta:** si la ocurrencia de uno no afecta al otro, es decir P(B|A)=P(B) o, equivalentemente, P(A∩B)=P(A)·P(B).

**5. Ejercicio Práctico:** De una baraja (52) se sacan 2 cartas sin reemplazo. (a) ¿Probabilidad de que la segunda sea un as si la primera NO fue as? Quedan 51 cartas con 4 ases → P=4/51. (b) ¿Probabilidad de que ambas sean ases? P=(4/52)·(3/51)=**1/221≈0.00452**.

**6. Claves / Formulario:**
- P(B|A) = P(A∩B)/P(A), con P(A)>0.
- Multiplicación: P(A∩B)=P(A)·P(B|A).
- Independencia ⟺ P(A∩B)=P(A)·P(B); sin reemplazo el denominador cambia.

---

## 📌 Distribución Geométrica
**1. Concepto en breve:** Cuenta **hasta cuántos ensayos hay que esperar para el primer éxito** (p.ej. "¿cuántas monedas antes de obtener águila?"). P(X=r)=q^(r−1)·p, con p=prob. de éxito y q=1−p. Su media es 1/p.

**2. Trampas del examen:** Es la de Proba 4, 6 y 7 ("hasta que aparece..."). Confundirla con la binomial negativa (éxitos hasta el r-ésimo) o con la binomial (n fijo). Aquí n NO está fijo; la variable es "en el intento número r". Ojo: la primera vez puede ser r=1 (probabilidad p).

**3. Visualización:**
```
p=0.25  (éxito), q=0.75
Intento r:  1       2        3         4
P(X=r):   0.25   0.75·0.25  0.75²·0.25 0.75³·0.25
Media = 1/p = 4 intentos
La probabilidad cae de forma geométrica: p, pq, pq²,...
```

**4. Ejemplo Teórico:** *"¿Cuál es la diferencia entre la distribución geométrica y la binomial?"*
**Respuesta:** en la geométrica el número de ensayos es variable y termina en el primer éxito; en la binomial el número de ensayos n es fijo y se cuentan todos los éxitos.

**5. Ejercicio Práctico:** La probabilidad de que un disparo haga blanco es 0.2. (a) ¿Probabilidad de que el primer acierto ocurra en el 4º disparo? P=(0.8)³·0.2=**0.1024**. (b) ¿Número esperado de disparos? 1/p=**5**.

**6. Claves / Formulario:**
- P(X=r)=q^(r−1)·p para r=1,2,3,...
- Media E(X)=1/p; varianza Var(X)=q/p².
- "Primer éxito" / "hasta que..." → geométrica.

---

## 📌 Distribución de Poisson
**1. Concepto en breve:** Modela el número de **sucesos raros o poco frecuentes en un intervalo fijo** (tiempo o espacio), como llamadas por minuto, errores por página o accidentes. Fórmula: P(X=r)=e^(−λ)·λ^r / r!, donde λ es la tasa media del intervalo.

**2. Trampas del examen:** Aparece en Proba 2 y 8 (ej. ventas de jamón, casos de una enfermedad). Es la **aproximación de la binomial** cuando n es grande y p pequeña, tomando λ=np. No confundas λ con n o con el índice r: λ es la "media de eventos", r es el valor que se pregunta.

**3. Visualización:**
```
λ = 2 eventos promedio
P(X=0)=e^(−2)·2⁰/0! = e^(−2)     ≈ 0.135
P(X=1)=e^(−2)·2¹/1! = 2·e^(−2)   ≈ 0.271
P(X=2)=e^(−2)·2²/2! = 2·e^(−2)   ≈ 0.271
La forma se concentra alrededor de λ.
```

**4. Ejemplo Teórico:** *"¿Bajo qué condición la distribución binomial se aproxima con la Poisson?"*
**Respuesta:** si n es grande y p muy pequeña (en la práctica np < 5, con p→0), la binomial se aproxima con la Poisson usando λ=n·p.

**5. Ejercicio Práctico:** En promedio hay 6 llamadas por minuto (λ=6). (a) P(lleguen exactamente 4): P=e^(−6)·6⁴/4!=**≈0.1339**. (b) P(lleguen al menos 2): 1−[P(0)+P(1)]=1−e^(−6)·(1+6)=**≈0.9826**.

**6. Claves / Formulario:**
- P(X=r)=e^(−λ)·λ^r / r!
- Media = λ y varianza = λ (E(X)=Var(X)=λ).
- Binomial → Poisson con λ=np cuando n grande y p pequeña.

---

## 📌 Distribución Hipergeométrica
**1. Concepto en breve:** Modela el número de éxitos al hacer un **muestreo SIN reemplazo** de una población finita con dos tipos de elementos. Fórmula: P(X=r)=[C(b,r)·C(s, n−r)] / C(b+s, n), con b elementos del tipo "éxito", s del otro y n extraídos.

**2. Trampas del examen:** Es la del Proba 8 (p.ej. sacar bolas/objetos sin devolver). La trampa es usarla con reemplazo (eso sería binomial). Si el texto dice "sin reemplazo" o "sin devolución" de una población pequeña → hipergeométrica; si la población es grande o hay reemplazo → binomial.

**3. Visualización:**
```
Caja: 3 rojas, 2 azules ; saco 2 sin reemplazo
P(1 roja) = [C(3,1)·C(2,1)] / C(5,2)
          = (3·2)/10 = 0.6
C(b,r)·C(s,n−r) en el numerador; C(total,n) abajo.
```

**4. Ejemplo Teórico:** *"¿Cuál es la diferencia clave entre la distribución hipergeométrica y la binomial?"*
**Respuesta:** la hipergeométrica se usa con muestreo **sin reemplazo** en una población finita (la probabilidad cambia en cada extracción); la binomial supone reemplazo o probabilidad constante.

**5. Ejercicio Práctico:** De 10 piezas, 4 están defectuosas y 6 buenas. Se toman 3 al azar sin reemplazo. ¿Probabilidad de sacar exactamente 1 defectuosa? P=[C(4,1)·C(6,2)]/C(10,3)=(4·15)/120=**0.5**.

**6. Claves / Formulario:**
- P(X=r)=[C(b,r)·C(s, n−r)] / C(b+s, n).
- "Sin reemplazo", población finita → hipergeométrica.
- Media = n·b/(b+s).

---

## 📌 Análisis Combinatorio y Permutaciones
**1. Concepto en breve:** Son técnicas de conteo para hallar espacios muestrales equiprobables: **permutación** (importa el orden) P(n,r)=n!/(n−r)!, **combinación** (no importa el orden) C(n,r)=n!/[r!(n−r)!]. La probabilidad clásica es casos favorables / casos posibles.

**2. Trampas del examen:** Se usan en Proba 2 (p.ej. bolas/letras de una caja) para contar "cuántos resultados". La trampa es decidir si el orden importa: si importa → permutación; si no → combinación. Con repetición se multiplican potencias; sin repetición se usa factorial.

**3. Visualización:**
```
Permutación P(5,2)=5!/(5−2)!=20   (AB ≠ BA)
Combinación C(5,2)=5!/(2!·3!)=10  (AB = BA)
Principio fundamental: m1·m2·m3... opciones
```

**4. Ejemplo Teórico:** *"¿Cuándo se usa permutación y cuándo combinación?"*
**Respuesta:** si el orden de elección es relevante (puestos, cifras) → permutación; si solo interesa el grupo formado (comités, manos de cartas) → combinación.

**5. Ejercicio Práctico:** De una caja con 5 bolas numeradas se extraen 2. (a) ¿Cuántos resultados ordenados? P(5,2)=**20**. (b) ¿Cuántos grupos desordenados? C(5,2)=**10**. (c) ¿Probabilidad de sacar la bola "1" y la "2" en algún orden? 2/20=**0.1**.

**6. Claves / Formulario:**
- Permutación: P(n,r)=n!/(n−r)! (sí importa el orden).
- Combinación: C(n,r)=n!/[r!(n−r)!] (no importa el orden).
- P(A)= (casos favorables)/(casos posibles).

---


## 🚨 Simulacro de Emergencia
*Preguntas rápidas para repaso, en estilo de exámenes reales.*
1. Enuncia el Teorema de Probabilidad Total y cuándo aplicas Bayes.
2. P(X=r) en binomial; ¿cuándo la binomial → Poisson?
3. ¿Cómo tipificas una variable normal? Da la fórmula de z.
4. Calcula la probabilidad de que una variable exponencial con media 10 supere 8.
5. ¿Cuál es la condición para que una densidad f(x) sea válida?
6. Escribe la definición de esperanza E(X) y varianza para variable discreta.
7. En un lanzamiento de dos dados, ¿P(sumatoria par) y E(sumatoria)?
8. ¿Qué significa muestreo sin reemplazo y cómo cambia la probabilidad?
9. ¿Cuál es la P(X>t) en una exponencial vs P(X<t)?
10. Si P(A∩B)=P(A)P(B), ¿qué puedes concluir de A y B?

**RESPUESTAS:** 1) P(A)=ΣP(Bi)P(A|Bi); Bayes = P(Bk|A). 2) C(n,r)p^r q^(n−r); si p→pequeña, λ=np. 3) z=(x−μ)/σ y tabla N(0,1). 4) e^(−8λ) (si media μ=1/λ, P(X>8)=e^(−8/μ)); ojo λ=1/μ. 5) f(x)>0 y área total=1. 6) E(X)=Σxp(x); Var=Σx²p(x)−E². 7) P(suma par)=18/36=0.5; E(suma)=7. 8) sin reemplazo: cambia denominador según cartas restantes (P(ej. rey)=4/52 → 4/51 tras quitar una). 9) Supervivencia e^(−λt); P(X<t)=1−e^(−λt). 10) A y B son independientes.