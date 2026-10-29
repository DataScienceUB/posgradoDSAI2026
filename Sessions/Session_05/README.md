# Sesión 06 · Estadística I · Estadística descriptiva y distribuciones

**Bloque:** Estadística e inferencia · **Fecha:** 3 de Noviembre, 2026

Antes de hacer afirmaciones sobre una población hay que saber describir bien la muestra. En esta sesión resumimos distribuciones, comparamos grupos, estudiamos valores atípicos, calculamos probabilidades con distribuciones teóricas y medimos la relación entre variables. Lo hacemos a partir de una pregunta concreta: **¿los primeros hijos nacen más tarde que los demás?**


## Antes de la sesión

**Obligatorio: sin los datos no podrás hacer el laboratorio.**

```bash
git pull
uv sync
```

Comprueba que tienes los dos ficheros de datos en la carpeta `notebooks/files/` de la sesión:

- `2002FemPreg.dat`: embarazos del ciclo de 2002 de la *National Survey of Family Growth* (NSFG), con un registro por embarazo. Es un fichero de ancho fijo.
- `run10.txt`: tiempos y sexo de los 16.924 corredores que terminaron la carrera Cherry Blossom de 10 millas de 2012, en Washington D. C.

## Objetivos de aprendizaje

- **Resumir:** una variable con la media, la mediana, la desviación estándar y los percentiles, y elegir el resumen según la forma de la distribución.
- **Comparar:** dos grupos con la PMF, la CDF y el riesgo relativo, en lugar de quedarte solo con la diferencia de medias.
- **Detectar:** los valores atípicos y la asimetría, y explicar cómo una decisión de limpieza cambia las cifras que comunicas.
- **Calcular:** probabilidades con las distribuciones binomial, exponencial y normal, y por simulación de Monte Carlo cuando no hay fórmula.
- **Medir:** la relación entre dos variables con la covarianza y las correlaciones de Pearson y Spearman, y explicar por qué no coinciden.

## Qué haremos

1. Plantear la pregunta sobre la duración del embarazo y conocer los datos de la NSFG.
2. Resumir la duración de los embarazos con medidas de centro y dispersión, y comparar media y mediana.
3. Dibujar histogramas, PMF y CDF para comprender la forma de la distribución.
4. Investigar valores atípicos y asimetría, y repetir el análisis con decisiones de limpieza justificadas.
5. Explorar los tiempos de la carrera Cherry Blossom y comparar grupos.
6. Comparar la proporción de nacimientos prematuros, a término y tardíos mediante el riesgo relativo.
7. Calcular probabilidades con distribuciones binomial, exponencial y normal, y experimentar con Monte Carlo.
8. Estudiar la relación entre duración del embarazo y peso al nacer con covarianza y correlaciones; comprobar por qué conviene mirar los datos además de los estadísticos.

## Herramientas

| Herramienta | Para qué la usamos |
| --- | --- |
| pandas | Leer el fichero de ancho fijo de la encuesta (`read_fwf`), resumir por grupos, calcular cuantiles y correlaciones |
| NumPy | Calcular estadísticos, trabajar con arrays y generar simulaciones reproducibles mediante `np.random.default_rng` |
| Matplotlib | Dibujar histogramas, PMF, CDF y diagramas de dispersión |
| SciPy | Calcular estadísticos y probabilidades con distribuciones teóricas, además de covarianzas y correlaciones |


## Para saber más

- [*Think Stats*, 3.ª edición](https://allendowney.github.io/ThinkStats), de Allen B. Downey: libro gratuito, en inglés, que enseña estadística programando en Python. El caso de los primeros hijos sale de aquí.
- [*Same Stats, Different Graphs*](https://www.research.autodesk.com/publications/same-stats-different-graphs/), de Justin Matejka y George Fitzmaurice (Autodesk Research, 2017, en inglés): el «Datasaurus», una versión moderna del cuarteto de Anscombe con doce conjuntos que tienen los mismos estadísticos y formas muy distintas.

## Para la próxima sesión

En la sesión 07 retomamos los efectos aparentes de hoy y nos preguntamos si pueden deberse al azar: si el orden de nacimiento no influyera, ¿con qué frecuencia veríamos una diferencia como esta?
