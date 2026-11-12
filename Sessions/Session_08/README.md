# Sesión 08 · Regresión I · Lineal e interpretación

**Bloque:** Estadística e inferencia · **Fecha:** 12.11.2026

En esta sesión introducimos la regresión lineal como herramienta de predicción sobre datos reales. Partimos de un problema concreto, **predecir el precio mediano de la vivienda en los bloques censales de California**, y construimos el modelo paso a paso: exploración y limpieza de los datos, ajuste de un modelo de mínimos cuadrados (OLS) múltiple, evaluación, diagnóstico de residuos y, por primera vez en el curso, **abrir la caja** para ver cómo calcula el modelo cada predicción. Terminamos con la regresión polinomial y el sobreajuste, que motivan la próxima sesión.

## Antes de la sesión

**Obligatorio: comprueba que el notebook carga los datos antes de venir a clase.**

```bash
git pull
uv sync
```

El conjunto *California Housing* viene con scikit-learn. La primera vez que ejecutas el notebook, `fetch_california_housing()` lo descarga de internet (menos de 1 MB) y lo guarda en `~/scikit_learn_data`; después funciona sin conexión.

Para el ejercicio extra, comprueba que tienes el fichero `SeaIce.txt` en la carpeta `notebooks/files/` de la sesión: mediciones mensuales de la extensión del hielo marino del Ártico, de 1979 a 2014, del [Centro Nacional de Datos de Nieve y Hielo](https://nsidc.org) (NSIDC) de EE. UU.

## Objetivos de aprendizaje

- **Explorar:** un conjunto de datos tabular real, detectar valores ausentes, duplicados, una variable objetivo censurada y valores atípicos en variables de cociente.
- **Decidir:** qué limpieza aplicar, justificarla antes de modelar y explicar cómo cambia el dominio en el que el modelo es válido.
- **Ajustar y evaluar:** modelos de regresión lineal simple y múltiple con scikit-learn, con R², MAE y RMSE en entrenamiento y test, y compararlos con una referencia.
- **Diagnosticar:** los residuos y el error por rango de precio para detectar no linealidad, heterocedasticidad y los segmentos en los que el modelo falla.
- **Explicar:** una predicción concreta como suma de contribuciones, y por qué los coeficientes en escala original no miden la importancia de las variables.
- **Detectar:** el sobreajuste al aumentar la complejidad del modelo con pocos datos.

## Qué haremos

1. Cargar el conjunto *California Housing* (20.640 bloques censales, 8 variables explicativas y la variable objetivo) y detectar la censura del precio en 500.000 USD.
2. Limpiar los datos: decidir qué hacer con los bloques censurados y eliminar los valores atípicos de `AveOccup` y `AveRooms`.
3. Dividir en entrenamiento (80 %) y test (20 %).
4. Ajustar una regresión simple por variable y comparar su R² y su MAE.
5. Ajustar el modelo OLS múltiple y evaluarlo con R², MAE y RMSE, frente a predecir siempre la media.
6. Comprobar a la IA: una métrica calculada con los argumentos al revés.
7. Diagnosticar los residuos y descomponer el error por deciles de precio.
8. Abrir la caja: descomponer una predicción en la contribución de cada variable y preguntarnos qué variable es más importante.
9. Ajustar regresiones polinomiales sobre `MedInc` y provocar el sobreajuste con una muestra pequeña.
10. Ejercicio extra: estimar la tendencia del hielo marino del Ártico con una regresión lineal simple.

## Herramientas

| Herramienta | Para qué la usamos |
|---|---|
| pandas | Cargar, explorar y limpiar los datos; `describe()`, `isnull()`, `qcut()` |
| NumPy | Calcular métricas y operar con vectores |
| Matplotlib | Diagramas de dispersión, histogramas, gráficos de residuos y de métricas |
| seaborn | `regplot`, para dibujar las regresiones simples con su IC del 95 % |
| scikit-learn | `fetch_california_housing`, `LinearRegression`, `PolynomialFeatures`, `Pipeline`, `train_test_split`, `StandardScaler` y las métricas |

## Laboratorio

1. [`notebooks/regresion_lineal_parte1.ipynb`](notebooks/regresion_lineal_parte1.ipynb): del conjunto de datos crudo a un modelo OLS múltiple evaluado, diagnosticado y explicado, con seis ejercicios y un ejercicio extra opcional.


## Para saber más

- [*An Introduction to Statistical Learning*](https://www.statlearning.com), de G. James, D. Witten, T. Hastie y R. Tibshirani: el capítulo 3 trata la regresión lineal simple y múltiple, el R², los coeficientes y la multicolinealidad; el capítulo 2, el equilibrio entre sesgo y varianza. Base teórica accesible y sin demasiadas matemáticas. PDF gratuito, en inglés.
- [*Introduction to Linear Regression Analysis*](https://www.wiley.com/en-jp/shop/general-introductory-statistics/introduction-to-linear-regression-analysis-6th-edition-p-9781119578727), de D. C. Montgomery, E. A. Peck y G. G. Vining (Wiley, en inglés): el libro clásico de regresión. Cubre en profundidad los supuestos del modelo, el diagnóstico de residuos, la homocedasticidad y la multicolinealidad. Más riguroso que el anterior.

## Para la próxima sesión

En la sesión 09 retomamos la pregunta que dejamos abierta: si `Population` tiene un coeficiente de 0,000036 y `Latitude`, de −0,44, ¿qué variable es más importante? Veremos que la respuesta requiere **estandarizar** las variables, y que esa misma estandarización es imprescindible antes de aplicar la **regularización** (Ridge y Lasso), la técnica que controla el sobreajuste que hemos provocado hoy con la regresión polinomial.
