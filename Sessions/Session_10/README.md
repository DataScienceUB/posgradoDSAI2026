# Sesión 10 · Ciencia de datos causal · Inferencia causal para Machine Learning

**Fecha:** 19.11.2026

Una buena predicción no basta para decidir qué intervención funcionará ni garantiza que un modelo mantenga su rendimiento en otro entorno. En esta sesión usamos la historia de un hospital para distinguir asociación, intervención y contrafactual; representamos las relaciones causales con grafos y mecanismos estructurales; y estimamos y ponemos a prueba efectos causales con DoWhy.

## Antes de la sesión

Prepara el entorno y las dependencias del proyecto:

```bash
uv sync
uv run jupyter lab
```

Abre `introduccion_causalidad_ml_con_dowhy.ipynb`. El notebook genera sus datos de ejemplo; no requiere ficheros de datos externos.

## Objetivos de aprendizaje

- **Distinguir:** asociación, intervención y contrafactual, y reconocer por qué una relación predictiva no implica una relación causal.
- **Representar:** un sistema mediante un grafo causal dirigido acíclico (DAG) y un modelo causal estructural (SCM) compuesto por mecanismos.
- **Interpretar:** el efecto de intervenir sobre una variable y cómo una intervención sustituye su mecanismo generador.
- **Estimar:** el efecto causal de una política de ingreso en UCI mediante comparación de grupos, ajuste por confusión e intervención simulada.
- **Analizar:** cómo cambian los mecanismos entre entornos y por qué las asociaciones predictivas pueden dejar de ser fiables en otro hospital.
- **Aplicar:** DoWhy para modelar un problema causal, identificar el efecto, estimarlo y refutar la estimación con pruebas de robustez.
- **Reconocer:** los límites de lo que puede identificarse a partir de datos observacionales y la importancia de los supuestos causales.

## Qué haremos

1. Examinar la paradoja del asma en un hospital y plantear por qué una asociación observada puede llevar a conclusiones erróneas.
2. Construir un modelo del hospital como un conjunto de mecanismos y representar sus relaciones mediante un DAG.
3. Expresar el grafo con ecuaciones estructurales e interpretar qué cambia al intervenir sobre una variable.
4. Comparar observación e intervención: estimar el efecto de la política de UCI con distintas estrategias y estudiar el papel de la confusión.
5. Explorar la autonomía de los mecanismos y cómo un cambio de entorno puede alterar las asociaciones aprendidas por un modelo.
6. Comparar predictores y analizar cuáles podrían resistir mejor el traslado a otro hospital.
7. Completar con DoWhy el flujo de inferencia causal: modelar, identificar, estimar y refutar un efecto.
8. Revisar los supuestos y límites de las conclusiones causales obtenidas de datos observacionales.

## Herramientas

| Herramienta | Para qué la usamos |
| --- | --- |
| pandas | Organizar los datos simulados del hospital |
| NumPy | Generar datos y realizar cálculos numéricos |
| Matplotlib | Visualizar distribuciones, comparaciones y resultados |
| NetworkX | Construir y dibujar grafos causales |
| scikit-learn | Ajustar modelos predictivos y evaluar sus resultados |
| DoWhy | Modelar, identificar, estimar y refutar efectos causales |
| JupyterLab | Ejecutar y explorar el notebook de forma interactiva |
| uv  | Instalar y mantener el entorno reproducible del proyecto |

## Para saber más

- [DoWhy](https://www.pywhy.org/dowhy/): documentación y ejemplos de modelado e inferencia causal.
- [Causal inference with DoWhy](https://www.pywhy.org/dowhy/v0.13/user_guide/causal_tasks/estimating_causal_effects/index.html): guía para identificar, estimar y refutar efectos causales.
- [The Book of Why](https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097616/), de Judea Pearl y Dana Mackenzie: introducción al razonamiento causal y a los diagramas causales.
- [Causal Inference: What If](https://miguelhernan.org/whatifbook), de Miguel A. Hernán y James M. Robins: referencia sobre inferencia causal en estudios observacionales.
