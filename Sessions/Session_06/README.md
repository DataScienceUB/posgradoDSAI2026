# Sesión 06 · Estadística II · Inferencia estadística

**Bloque:** Estadística e inferencia · **Fecha:** 5.11.2026

En la sesión anterior vimos que los primeros hijos parecen nacer algo más tarde que los demás. Pero una muestra distinta habría dado una cifra distinta: ¿cuánto podemos fiarnos de lo que observamos? En esta sesión pasamos de describir la muestra a hacer afirmaciones sobre la población, cuantificando su incertidumbre con errores estándar, *bootstrap*, intervalos de confianza y contrastes de hipótesis. Lo hacemos a partir de tres preguntas concretas sobre el efecto aparente: **¿puede deberse al azar?, ¿es estadísticamente significativo?, ¿es relevante?**

## Antes de la sesión

**Obligatorio: sin los datos no podrás hacer el laboratorio.**

```bash
git pull
uv sync
```

Comprueba que tienes los dos ficheros de datos en la carpeta `notebooks/files/` de la sesión:

- `2002FemPreg.dat`: embarazos del ciclo de 2002 de la *National Survey of Family Growth* (NSFG), con un registro por embarazo. Es un fichero de ancho fijo y es el mismo de la sesión 06.
- `ACCIDENTS_GU_BCN_2013.csv`: accidentes de tráfico gestionados por la Guardia Urbana de Barcelona en 2013, publicado en [Open Data BCN](https://opendata-ajuntament.barcelona.cat/). Cada fila es un accidente, con la fecha, la hora, la calle y el número de víctimas. Está codificado en `latin-1`.

## Objetivos de aprendizaje

- **Distinguir:** población y muestra, parámetro y estadístico, y explicar qué es la distribución muestral de un estimador.
- **Cuantificar:** la precisión de una estimación con el error estándar, tanto con la fórmula $\sigma/\sqrt{n}$ como por simulación, y explicar qué garantiza el teorema central del límite.
- **Remuestrear:** con *bootstrap* para estimar el error estándar y el intervalo de confianza de cualquier estadístico, también de los que no tienen fórmula, como la desviación estándar.
- **Construir e interpretar:** intervalos de confianza del 95 %, y explicar por qué el 95 % es una propiedad del procedimiento y no de un intervalo concreto.
- **Contrastar:** una hipótesis con un test de permutaciones y con la aproximación normal, interpretar correctamente el valor *p* y distinguir entre significación estadística y relevancia práctica.

## Qué haremos

1. Retomar el efecto aparente de la NSFG: la diferencia de duración media del embarazo entre primeros hijos y demás hijos.
2. Repasar los conceptos de población, muestra, parámetro, estadístico y estimador.
3. Simular la distribución muestral de la media, calcular el error estándar y comprobar el teorema central del límite con una población asimétrica.
4. Estimar la variabilidad de la media y de la desviación estándar mediante *bootstrap*, usando solo una muestra.
5. Ejercicio: estimar la tasa media de accidentes diarios en Barcelona y su error estándar a partir de una muestra de 200 días.
6. Construir intervalos de confianza con la fórmula y con el método de los percentiles *bootstrap*, y simular 100 intervalos para ver qué significa «95 % de confianza».
7. Plantear contrastes de hipótesis: el caso de la moneda belga de *The Guardian* y un test de permutaciones para la NSFG; compararlos con el error estándar de la diferencia y repasar los errores de tipo I y II.
8. Responder a las tres preguntas iniciales y reflexionar sobre las comparaciones múltiples y la postura escéptica ante los datos.

## Herramientas

| Herramienta | Para qué la usamos                                                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| pandas      | Leer los ficheros de datos (`read_fwf`, `read_csv`), construir fechas, agrupar por día y extraer muestras con `sample`              |
| NumPy       | Calcular estadísticos y generar simulaciones, remuestras *bootstrap* y permutaciones reproducibles mediante `np.random.default_rng` |
| Matplotlib  | Dibujar distribuciones muestrales y *bootstrap*, intervalos de confianza y distribuciones bajo $H_0$                                |
| SciPy       | Comprobar los resultados simulados con la distribución binomial y la normal (`scipy.stats`)                                         |

## Para saber más

- [*Think Stats*, 3.ª edición](https://allendowney.github.io/ThinkStats), de Allen B. Downey: libro gratuito, en inglés, que enseña estadística programando en Python. El caso de los primeros hijos y el enfoque computacional de los contrastes salen de aquí.
- [«Scientific method: Statistical errors»](https://www.nature.com/articles/506150a), de Regina Nuzzo (*Nature*, 2014, en inglés): por qué el valor *p* no es tan fiable como muchos científicos suponen, y cómo evitar sus malas interpretaciones.
- B. Efron, «Bootstrap methods: another look at the jackknife», *The Annals of Statistics* 7(1), 1979 (en inglés): el artículo original del *bootstrap*.

## Para la próxima sesión

En la sesión 08 cambiamos de paradigma con la **estadística bayesiana**. Hoy hemos insistido en que el valor *p* es $P(\text{datos} \mid H_0)$ y no la probabilidad de que la hipótesis sea cierta. El enfoque bayesiano responde precisamente a esa otra pregunta: trata los parámetros como inciertos y actualiza lo que creemos sobre ellos a medida que llegan los datos.
