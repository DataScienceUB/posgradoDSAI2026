# Sesión 07 · Estadística II · Inferencia bayesiana

**Bloque:** Estadística e inferencia **Fecha:** 10.11.2026

En el notebook anterior trabajamos con el paradigma frecuentista: los parámetros son valores fijos, aunque desconocidos. La estadística bayesiana interpreta la probabilidad como un **grado de creencia** y permite actualizarlo a medida que observamos datos. En esta sesión aplicamos el teorema de Bayes a problemas de diagnóstico, estimación y comparación de hipótesis, y damos los primeros pasos en programación probabilística.

## Antes de la sesión

Prepara el entorno y las dependencias del proyecto:

```bash
uv sync
```

El notebook utiliza estos ficheros, incluidos en `files/`:

- `2002FemPreg.dat`: datos de embarazos de la *National Survey of Family Growth* (NSFG), usados para comparar la duración media de los embarazos de primeros hijos y de los demás.
- `txtdata.csv`: serie de recuentos de mensajes, usada para modelar la tasa de actividad de un usuario.

## Objetivos de aprendizaje

- **Interpretar:** la probabilidad como grado de creencia y expresar el teorema de Bayes como actualización de una distribución *a priori* mediante la verosimilitud.
- **Calcular:** probabilidades *a posteriori* en problemas de diagnóstico y en ejemplos como el de Monty Hall.
- **Estimar:** un parámetro desconocido a partir de una distribución *a priori*, una verosimilitud y los datos observados; comprender cómo influyen los datos y la elección de la distribución *a priori*.
- **Resumir:** una distribución *a posteriori* con estimaciones puntuales e intervalos de credibilidad, y distinguir estos últimos de los intervalos de confianza frecuentistas.
- **Comparar:** hipótesis con probabilidades *a posteriori* y entender cómo responde el enfoque bayesiano a la pregunta de si un efecto observado es real.
- **Modelar:** una moneda sesgada y una regresión lineal bayesiana, e introducir la programación probabilística con PyMC y el análisis de resultados con ArviZ.
- **Aplicar:** distribuciones de Poisson y exponencial a datos de recuentos y al cambio de comportamiento de un usuario.

## Qué haremos

1. Contrastar las interpretaciones frecuentista y bayesiana de la probabilidad.
2. Enunciar el teorema de Bayes y aplicarlo a una prueba diagnóstica y al problema de Monty Hall.
3. Resolver un ejercicio de cribado de cáncer de mama y examinar cómo se actualizan las creencias.
4. Estimar la ubicación de una locomotora desconocida y estudiar el efecto de la distribución *a priori*, la verosimilitud y la incorporación secuencial de datos.
5. Resumir distribuciones *a posteriori* con estimaciones puntuales e intervalos de credibilidad, y compararlos con los intervalos de confianza.
6. Comparar bayesianamente las hipótesis sobre la diferencia en la duración de los embarazos de primeros hijos y los demás.
7. Modelar el posible sesgo de una moneda con una distribución beta y observar cómo cambia la distribución *a posteriori* al acumular lanzamientos.
8. Construir y ajustar con PyMC un modelo de regresión lineal bayesiana, y analizar su distribución *a posteriori* con ArviZ.
9. Usar distribuciones de Poisson y exponencial para modelar recuentos y explorar si ha cambiado la actividad de un usuario.

## Herramientas

| Herramienta | Para qué la usamos |
| --- | --- |
| pandas | Leer los datos de embarazos y preparar las observaciones |
| NumPy | Trabajar con arrays y realizar cálculos numéricos |
| Matplotlib | Visualizar distribuciones y resultados de los modelos |
| SciPy | Utilizar distribuciones y cálculos estadísticos |
| PyMC | Especificar y ajustar modelos probabilísticos bayesianos |
| ArviZ | Resumir y visualizar los resultados de la inferencia bayesiana |

## Para saber más

- [*Think Bayes*](https://greenteapress.com/wp/think-bayes/), de Allen B. Downey: introducción práctica a la estadística bayesiana con Python.
- [*Bayesian Data Analysis*](http://www.stat.columbia.edu/~gelman/book/), de Andrew Gelman y colaboradores: referencia sobre modelización e inferencia bayesianas.
- [PyMC](https://www.pymc.io/): documentación del lenguaje de programación probabilística utilizado en el notebook.
- [ArviZ](https://www.arviz.org/): herramientas para explorar y comunicar resultados de modelos bayesianos.
