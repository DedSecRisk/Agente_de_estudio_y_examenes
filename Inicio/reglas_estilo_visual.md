# Reglas Estrictas de Estilo Visual y Contenido

> Obligatorio para toda guía visual generada por ParetoTutor Visual en el Directorio de Salida (`...\Guias terminadas\`).

---

## 1. Fondo y Contraste

- Usa un fondo base mate **oscuro** `#0F172A` (todo el documento sobre fondo oscuro, texto claro para alto contraste).
- Para cada bloque decorativo, aplica SIEMPRE la regla de **3 capas** (fondo, borde y color de texto):

| Bloque | Uso | background | border | color |
|---|---|---|---|---|
| 🔵 **Azul** | Conceptos / definiciones | `rgba(56,189,248,.10)` | `2px solid #38bdf8` | `#bae6fd` |
| 🔴 **Rojo** | Trampas / advertencias | `rgba(248,113,113,.10)` | `2px solid #ef4444` | `#fecaca` |
| 🟢 **Verde** | Ejemplos y solución | `rgba(34,197,94,.10)` | `2px solid #22c55e` | `#bbf7d0` |
| 🟠 **Naranja** | Fórmulas / reglas de oro | `rgba(245,158,11,.10)` | `2px solid #f59e0b` | `#fef3c7` |
| 🗺️ **Mapa/Flujo** | Diagramas / flujos | `#1e293b` | `2px dashed #475569` | `#cbd5e1` |
| 🧠 **Recall** | Repaso activo | `#0f1729` | `2px solid #6366f1` | `#e0e0ff` |

Ejemplo de implementación CSS para un bloque Azul (Conceptos):

```css
.bloque-azul {
    background: rgba(56,189,248,.10);   /* capa 1: fondo */
    border: 2px solid #38bdf8;         /* capa 2: borde */
    color: #bae6fd;                    /* capa 3: texto */
}
```

> **Regla de oro:** las 4 reglas de color semánticas (azul/rojo/verde/naranja) se aplican en TODOS los bloques, sin excepción. El fondo base del documento es siempre `#0F172A` (modo oscuro) y el texto se mantiene claro para alto contraste.

---

## 2. Estructura Extendida

Toda guía debe incluir obligatoriamente estos 3 elementos adicionales:

### Árbol de Decisión (inicio de la guía)
Incluye un **Árbol de Decisión en Diagrama ASCII o Tabla** al inicio de la guía para **elegir la fórmula según el enunciado** (p. ej.: ¿n fijo? → Binomial; ¿primer éxito? → Geométrica; ¿sucesos raros en intervalo? → Poisson; ¿sin reemplazo y población finita? → Hipergeométrica; ¿tiempos/vida útil? → Exponencial; ¿campana continua? → Normal; ¿"de qué causa proviene"? → Bayes).

### Tabla de Notación de Símbolos
Agrega una **Tabla de Notación de Símbolos** previa a los temas (símbolo → significado), por ejemplo: `P(A|B)`, `μ`, `σ`, `σ²`, `λ`, `n`, `p`, `q`, `C(n,r)`, `Φ(z)`, `E(X)`, `Var(X)`, `∫`...

### Repaso Activo (Active Recall)
Añade **2 preguntas de Repaso Activo (Active Recall)** al cierre de cada módulo/tema, para que el estudiante recupere la información de memoria ante de revisar la respuesta.

---

*(Reglas base para la generación visual: ver `agent.md`, `flujo_trabajo.md` y `plantilla_salida.md`.)*