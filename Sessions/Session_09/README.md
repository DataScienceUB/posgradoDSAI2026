# Sesión 9 · Regresión II · Estandarización y regularización

**Bloque:** Estadística e inferencia · **Fecha:** 17.11.2026

En la sesión anterior ajustamos un modelo OLS y dejamos una pregunta abierta: si `Population` tiene un coeficiente de 0,000036 y `Latitude`, de −0,44, ¿qué variable es más importante? En esta sesión la respondemos **estandarizando** las variables, usamos los coeficientes estandarizados para explicar una predicción concreta y vemos qué problemas crea la **multicolinealidad**. Después aplicamos la **regularización** (Ridge y Lasso), que penaliza los coeficientes grandes para controlar la inestabilidad y el sobreajuste, y comprobamos cuándo ayuda de verdad y cuándo no hace falta.

## Antes de la sesión

```bash
git pull
uv sync
```

Usamos el mismo conjunto *California Housing* de la sesión 08, que scikit-learn guarda en `~/scikit_learn_data` la primera vez que lo descarga. Si no ejecutaste el notebook de la sesión 08, la primera ejecución necesita conexión a internet.

Repasa en el notebook de la sesión 08 la pregunta abierta de la sección 9 (abrir la caja) y el ejercicio 6 (sobreajuste con un polinomio de grado 10): hoy volvemos a los dos.

## Objetivos de aprendizaje

- **Explicar:** por qué los coeficientes OLS no son comparables cuando las variables tienen escalas distintas.
- **Estandarizar:** correctamente, ajustando el `StandardScaler` solo con el entrenamiento y dentro de un *pipeline* en la validación cruzada, para evitar fugas de datos.
- **Interpretar:** los coeficientes estandarizados y la descomposición de una predicción respecto a un bloque medio, y detectar cuándo la multicolinealidad hace que engañen.
- **Aplicar:** Ridge (L2) y Lasso (L1), leer sus caminos de regularización y elegir el hiperparámetro alpha por validación cruzada.
- **Decidir:** cuándo la regularización aporta algo y cuándo OLS es suficiente.

## Qué haremos

1. Repetir la carga, la limpieza y la división de la sesión 08, para trabajar con el mismo modelo.
2. Ver el problema de las escalas en los coeficientes OLS en escala original.
3. Estandarizar las variables, reajustar el modelo y comprobar que las predicciones y las métricas no cambian.
4. Abrir la caja: descomponer una predicción en contribuciones respecto a un bloque medio y calcular una importancia global de las variables.
5. Detectar la multicolinealidad (latitud y longitud) y medir la estabilidad de los coeficientes en submuestras.
6. Trazar el camino de regularización de Ridge y elegir alpha por validación cruzada.
7. Trazar el camino de Lasso, ver en qué orden anula las variables y elegir alpha.
8. Comprobar a la IA: un Lasso sin estandarizar que elimina las variables equivocadas.
9. Comparar OLS, Ridge y Lasso, y rescatar con Ridge el polinomio sobreajustado de la sesión 08.

## Herramientas

| Herramienta | Para qué la usamos |
|---|---|
| pandas | Tablas de coeficientes, correlaciones y comparaciones de métricas |
| NumPy | Submuestras aleatorias para el análisis de estabilidad y operaciones vectoriales |
| Matplotlib | Caminos de regularización, curvas de validación cruzada y comparación de coeficientes |
| seaborn | Mapa de calor de la matriz de correlaciones |
| scikit-learn | `StandardScaler`, `LinearRegression`, `Ridge`, `RidgeCV`, `Lasso`, `make_pipeline`, `cross_val_score`, `PolynomialFeatures` y las métricas |

## Laboratorio

1. [`notebooks/regresion_lineal_parte2.ipynb`](notebooks/regresion_lineal_parte2.ipynb): de los coeficientes en escala original a un modelo estandarizado, explicado y regularizado, con cinco ejercicios.

Dónde trabajar: copia el notebook a la carpeta `s09/` de tu repositorio personal.


## Para saber más

- [*An Introduction to Statistical Learning*](https://www.statlearning.com), de G. James, D. Witten, T. Hastie y R. Tibshirani: el capítulo 6 (*Linear Model Selection and Regularization*) explica Ridge, Lasso, la elección de alpha por validación cruzada y la intuición geométrica de las dos penalizaciones. PDF gratuito, en inglés.
- [*Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125974/), de A. Géron (O'Reilly, 3.ª edición, en inglés): el capítulo 4 (*Training Models*) implementa Ridge, Lasso y Elastic Net con scikit-learn, con *pipelines* y validación cruzada.

## Para la próxima sesión

El coeficiente de `MedInc` es positivo y grande: los bloques con más ingresos tienen viviendas más caras. Pero ¿podemos decir que, si subieran los ingresos de un barrio, subiría el precio de sus viviendas? El modelo mide asociaciones, no causas. En la sesión 10, **inferencia causal**, veremos cuándo y cómo se puede pasar de una cosa a la otra.
