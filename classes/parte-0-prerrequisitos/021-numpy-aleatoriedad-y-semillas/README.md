# Clase 021 — NumPy: aleatoriedad y semillas

> Parte: **0 — Prerrequisitos** · Fuente: *Numerical Recipes* cap. 7 (Random Numbers) · NumPy `random.Generator` docs.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno genere números aleatorios **reproduciblemente** con el API moderno (`np.random.default_rng(seed)`), use las distribuciones más comunes (uniforme, normal, Bernoulli, Poisson, exponencial), y entienda por qué la reproducibilidad es no-negociable en ciencia de datos.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Crear un `Generator`** con `np.random.default_rng(seed)` y usarlo para reproducibilidad.
2. **Generar muestras** de uniforme, normal, integers, binomial, Poisson, exponencial.
3. **Permutar y muestrear** sin/con reemplazo con `permutation` y `choice`.
4. **Reproducir** un experimento exactamente con el mismo seed.
5. **Saber por qué** `np.random.seed()` (API legacy) es deprecated en favor de `Generator`.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `np.random.default_rng(seed)` | El API moderno (Generator-based, PCG64). |
| 2 | Distribuciones continuas: uniform, normal, exponential, gamma, beta | Las más usadas en simulación. |
| 3 | Distribuciones discretas: integers, binomial, poisson | Conteos y procesos. |
| 4 | `permutation` y `choice` | Mezclar y muestrear. |
| 5 | Reproducibilidad: por qué importa | Misma cosa con mismo seed. |
| 6 | Múltiples generadores independientes | Evita interferencia entre experimentos. |

## 📂 Dataset / recursos

Sintético: simulación Monte Carlo. Sin descarga.

## 🧪 Ejercicios

**1.** **Reproducibilidad.** Crea 2 rngs con `seed=42`, genera 1000 normales con cada uno. Verifica que son idénticos.

**2.** **Distribuciones.** Genera 10000 muestras de: uniforme [0,1], normal(5,2), exponential(λ=1/3), poisson(λ=4). Calcula media y std empírica y compara con teórica.

**3.** **Monte Carlo de π.** Estima π lanzando puntos en un cuadrado 2×2 y contando cuántos caen dentro del círculo unitario. Compara con π real.

**4.** **Bootstrap.** Dado un sample de 30 valores, estima la distribución de la media por bootstrap (1000 resamples con reemplazo).

**5.** **Permutación.** Mezcla un array de 100 elementos con `permutation`. Verifica que es la misma cuando usas el mismo seed.

## 📝 Homework verificable

Notebook con: (a) Monte Carlo de π con N=10k, 100k, 1M reportando error; (b) bootstrap de la media de un sample (95% CI vs CLT); (c) demo de reproducibilidad con dos rngs; (d) tabla comparando momento empírico vs teórico para 4 distribuciones.

**Criterio de aceptación:** MC converge a π. Bootstrap CI similar al CLT. Reproducibilidad exacta.

## 🔗 Referencias

- [NumPy `random.Generator`](https://numpy.org/doc/stable/reference/random/generator.html)
- [NEP 19 — Random number generator policy](https://numpy.org/neps/nep-0019-rng-policy.html)
- Press et al., *Numerical Recipes* 3e — cap. 7 *Random Numbers*.

## ➡️ Siguiente clase

[Clase 022 — Pandas: Series y DataFrame](../022-pandas-series-y-dataframe/README.md)
