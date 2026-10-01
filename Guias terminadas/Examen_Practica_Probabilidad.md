# EXAMEN DE PRÁCTICA DE PROBABILIDAD (10 preguntas con solución detallada)

> **Estilo y método:** imita los exámenes de Probabilidad de UPIICSA analizados (Proba 1–10). Resuélvelo primero y luego compara con las **respuestas explicadas paso a paso** que aparecen después de cada enunciado. Los temas priorizan el Top 20% (Bayes, Normal, Binomial, Exponencial) más los de prioridad alta restantes.

---

## SECCIÓN A — ENUNCIADOS

**1. (Probabilidad total y Bayes)** Una fábrica tiene 3 líneas de producción. L1 elabora el 50% de las piezas, L2 el 30% y L3 el 20%. La proporción de piezas defectuosas es: L1=3%, L2=4%, L3=5%. Se elige una pieza al azar:
   (a) ¿Cuál es la probabilidad de que sea defectuosa?
   (b) Si resultó defectuosa, ¿cuál es la probabilidad de que provenga de la línea L3?

**2. (Distribución binomial)** Un vendedor logra cerrar una venta con probabilidad 0.30 en cada visita que hace. Visita 8 clientes independientes.
   (a) ¿Cuál es la probabilidad de que cierre exactamente 3 ventas?
   (b) ¿Cuál es la probabilidad de que cierre al menos 2 ventas?

**3. (Aproximación normal a la binomial)** El 40% de los habitantes de una colonia usa el servicio de autobús. Se toma una muestra de 100 personas. Aproximadamente, ¿cuál es la probabilidad de que **más de 45** utilicen el autobús? ¿Y de que sean **entre 35 y 50** inclusive? (usa aproximación normal con corrección de continuidad).

**4. (Distribución normal pura)** El peso de un paquete se distribuye normalmente con media 25 kg y desvío 4 kg.
   (a) ¿Qué probabilidad hay de que un paquete pese menos de 30 kg?
   (b) ¿Qué peso supera al 90% de los paquetes (bajo el cual cae el 90%)?

**5. (Distribución exponencial)** La duración de un componente eléctrico sigue una distribución exponencial con una vida media de 8 años.
   (a) ¿Cuál es la probabilidad de que dure más de 10 años?

**6. (Variable aleatoria continua — cálculo de k)** La función de densidad de una variable aleatoria X es f(x) = k·x para 0 ≤ x ≤ 2 y 0 en otro caso.
   (a) Determina el valor de k.
   (b) Calcula P(0.5 < X < 1.5).
   (c) Halla la esperanza E(X).

**7. (Variable aleatoria discreta — tabla, esperanza, varianza)** Un experimento consiste en lanzar dos dados. Sea X = valor absoluto de la diferencia (|d1 − d2|).
   (a) Construye la tabla de distribución de probabilidades de X.
   (b) Calcula E(X) y Var(X).

**8. (Probabilidad condicional / sin reemplazo)** De una baraja completa (52 cartas) se extraen 2 cartas al azar sin reposición.
   (a) ¿Cuál es la probabilidad de que la segunda sea un as si la primera NO fue un as?
   (b) ¿Cuál es la probabilidad de que las dos sean ases?

**9. (Distribución de Poisson)** En una central de llamadas llegan en promedio 6 llamadas por minuto. Asumiendo distribución de Poisson:
   (a) ¿Cuál es la probabilidad de que en un minuto lleguen exactamente 4 llamadas?
   (b) ¿Cuál es la probabilidad de que en un minuto lleguen al menos 2 llamadas?

**10. (Teorema de Bayes)** Una caja contiene 3 bolas azules y 2 rojas; y otra caja contiene 2 bolas azules y 5 rojas. Se elige una caja al azar y se extrae una bola. La bola resultó azul. ¿Cuál es la probabilidad de que provenga de la PRIMERA caja?

---
---

## SECCIÓN B — RESPUESTAS EXPLICADAS PASO A PASO

**PREGUNTA 1 (probabilidad total + Bayes)**
(a) Probabilidad total: P(defecto) = P(L1)·P(D|L1) + P(L2)·P(D|L2) + P(L3)·P(D|L3)
= 0.50·0.03 + 0.30·0.04 + 0.20·0.05 = 0.015 + 0.012 + 0.010 = **0.037 (3.7%)**
(b) Bayes: P(L3|D) = [P(L3)·P(D|L3)]/P(D) = (0.20·0.05)/0.037 = 0.010/0.037 = **≈ 0.2703 (27.0%)**
> *Clave:* el denominador SIEMPRE es P(defecto) total = 0.037; el numerador, la rama L3 de ese mismo árbol.

**PREGUNTA 2 (binomial)**
(a) P(X=3) = C(8,3)·0.3³·0.7^(8−3) = 56·(0.027)·(0.16807) = 56·0.004538 = **≈ 0.2541**
(b) P(X ≥ 2) = 1 − P(X=0) − P(X=1)
P(0)=0.7⁸=0.057648; P(1)=8·0.3·0.7⁷=8·0.3·0.0823543=0.19765
P(≥2)=1−0.057648−0.19765=**≈ 0.7447**
> *Clave:* "al menos 2" se resuelve por complemento (1 − casos menores).

**PREGUNTA 3 (normal-aproximación)**
n=100, p=0.4 → μ=n p=40, σ=√(100·0.4·0.6)=√24≈4.899.
(a) "más de 40" significa X≥41; inicio en 40.5: z=(40.5−40)/4.899≈0.102. P(z>0.102)=1−Φ(0.102)=1−0.541≈**0.459**.
(b) entre 34.5 y 50.5: z1=(34.5−40)/4.899=−1.122, z2=(50.5−40)/4.899=2.143. P=Φ(2.143)−Φ(−1.122)=0.9838−0.1314=**≈0.852**.
> *Clave:* para variables discretas se corrige con ±0.5 (continuidad) antes de tipificar.

**PREGUNTA 4 (normal)**
(a) z=(30−25)/4=1.25 → P(X<30)=P(z<1.25)=**0.8944**.
(b) P(X< w)=0.90 → z=1.28 → w=μ+z·σ=25+1.28·4=**30.12 kg**.
> *Clave:* para percentil despejas x=μ+z·σ con z de la tabla.

**PREGUNTA 5 (exponencial)**
(a) λ=1/8. P(X>10)=e^(−10/8)=e^(−1.25)=**0.2865**.
(b) P(X<4)=1−e^(−0.5)=**0.3935**.
> *Clave:* No confundir μ con λ; siempre λ=1/μ. P(X>t)=e^(−λ t).

**PREGUNTA 6 (continua)**
(a) ∫₀² k x dx = k·[x²/2]₀² = k·2 = 1 → **k=1/2**.
(b) P(0.5<X<1.5)=(1/2)·∫₀.₅¹·⁵ x dx=(1/2)·[(1.5²−0.5²)/2]=(1/2)·(2/2)=**0.5**.
(c) E(X)=∫ x·f(x)dx=∫₀² x·(x/2)dx=∫₀²(x²/2)=[x³/6]₀²=8/6=**4/3**.

**PREGUNTA 7 (discreta)**
36 resultados equiprobables. Diferencia d:
d=0 → (1,1)...(6,6)=6
d=1 → 10; d=2 → 8; d=3 → 6; d=4 → 4; d=5 → 2.
Tabla: P(0)=6/36, P(1)=10/36, P(2)=8/36, P(3)=6/36, P(4)=4/36, P(5)=2/36; Σ=36/36=1 ✔.
E(X)=Σ x·p = (0 + 10·1 + 8·2 + 6·3 + 4·4 + 2·5)/36 = (0+10+16+18+16+10)/36 = 70/36 = **35/18 ≈ 1.944**.
E(X²)=(0 + 10·1 + 8·4 + 6·9 + 4·16 + 2·25)/36=(0+10+32+54+64+50)/36=210/36=35/6.
Var=E(X²)−[E(X)]² = 35/6 − (35/18)² ≈ 5.8333 − 3.7839 = **≈2.05**.
**PREGUNTA 8 (condicional / sin reemplazo)**
(a) Si la primera NO fue un as, quedan 51 cartas con los 4 ases: P(A₂|no A₁)=4/51=**≈0.0784**.
(b) P(A₁ y A₂)=P(A₁)·P(A₂|A₁)=(4/52)·(3/51)=12/2652=**1/221≈0.00452**.
> *Clave:* sin reposición, el denominador disminuye en 1 en cada extracción.

**PREGUNTA 9 (Poisson)**
λ=6 llamadas/min.
(a) P(X=4)=e^(−6)·6⁴/4! = e^(−6)·(1296/24)=e^(−6)·54 = **≈0.1339**.
(b) P(X≥2)=1−[P(0)+P(1)]=1−[e^(−6)+e^(−6)·6]=1−e^(−6)·7=**≈0.9826**.
> *Clave:* en Poisson E(X)=Var(X)=λ; usa e^(−λ)·λ^r/r!.

**PREGUNTA 10 (Bayes con dos cajas)**
"Se elige la caja al azar" → P(CAJA1)=P(CAJA2)=1/2.
P(azul) total = (1/2)·(3/5) + (1/2)·(2/7) = 3/10 + 1/7 = 21/70 + 10/70 = 31/70.
P(caja1|azul)=P(caja1)·P(azul|caja1)/P(azul) = (1/2·3/5)/(31/70) = (3/10)/(31/70) = (3/10)·(70/31) = 21/31 = **≈0.6774**.
> *Clave:* como la caja se elige al azar, P(caja)=1/2 entra en el denominador de Bayes.

---

## 🏁 Criterio de autoevaluación (orientativo)
- 10 aciertos → listo para el examen.
- 8–9 → repasa el tema fallado con la sección correspondiente de la guía.
- 6–7 → repasa Prioridad Alta (Bayes, Normal, Binomial, Exponencial) y vuelve a intentar.
- < 6 → estudia de nuevo la guía completa y repite el examen.

*Respuestas breves para autoevaluación rápida:*
1(b) 0.2703 · 2) 0.2541 y 0.7447 · 3) ≈0.459 y ≈0.852 · 4) 0.8944 y 30.12 kg · 5) 0.2865 y 0.3935 · 6) k=1/2, 0.5 y 4/3 · 7) E=35/18≈1.944; Var≈2.05 · 8) 0.0784 y 1/221 · 9) 0.1339 y 0.9826 · 10) 21/31