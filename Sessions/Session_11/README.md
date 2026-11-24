# Tasación de viviendas para Banc Avellaner

**Equipo:** <!-- nombres y usuarios de GitHub -->

Miniproyecto 2 del posgrado. Modelo lineal que tasa viviendas de Barcelona y su área metropolitana, y cuadro de mando para entenderlo y validarlo.

> **Barrios y direcciones reales, ventas simuladas.** Los barrios y sus indicadores (viviendas, población, superficie media, años de construcción, valor catastral, renta) son reales, de Open Data BCN, y las direcciones y los códigos postales, del ICGC. Las viviendas, las ventas y los precios de 2023 a 2025 son simulados: que una dirección aparezca en los datos no significa que allí se haya vendido nada. Banc Avellaner y su directora de riesgos son inventados.

## Cómo se trabaja en este proyecto

El código lo genera un agente de IA a partir de lo que escribe el equipo. Vuestro trabajo es **analizar, especificar, verificar y decidir**: no escribís en `src/` ni en `tests/`; el código propio, solo en `notebooks/`.

| Fichero | Qué es | Quién lo escribe |
| --- | --- | --- |
| `AGENTS.md` | Reglas para el agente, con los tests del profesorado (CM1-CM7) | Profesorado |
| `SPECS.md` | Qué construimos, en cuatro fases: limpieza, transformaciones, variables nuevas y modelo | Equipo |
| `DESIGN.md` | Cómo se ve y se comporta el cuadro de mando | Equipo |
| `ARCHITECTURE.md` | Dónde va cada cosa en el código | Equipo (el agente puede proponer) |
| `TASKS.md` | Las tareas, en pasos pequeños | El agente propone, el equipo aprueba |
| `README.md` | Este fichero, para personas | Equipo |
| `DATOS.md` | Qué significa cada columna | Profesorado |

Las fases se hacen en orden, y en cada una:

1. Escribid en `SPECS.md` los problemas, las estrategias **con su hipótesis**, los requisitos y los criterios de la fase.
2. Pedid al agente que **revise** lo escrito y diga qué no se entiende. Corregid.
3. El agente propone las tareas de la fase en `TASKS.md`. Aprobadlas. La primera es siempre la de los tests.
4. El agente escribe los tests de los criterios de la fase en `tests/acceptance/`. Revisadlos (¿el ejemplo es el de `SPECS.md`?, ¿el resultado esperado está calculado a mano?) y aprobadlos.
5. El agente implementa **una** tarea cada vez. Verificáis y completáis `Verificado por:`.
6. Ejecutad `src.experimentos`, aplicad vuestra regla de decisión y anotad en `SPECS.md` el resultado y la decisión, con cifras.

## Repositorio
https://github.com/DataScienceUB/mp2-plantilla

## Puesta en marcha

```bash
uv sync
uv run python scripts/descargar_datos.py    # datos a data/raw/
uv run python -m src.experimentos           # compara las estrategias → reports/experimentos.csv
uv run python -m src.entrenar               # modelo final → models/ y reports/metricas.json
uv run python -m src.predecir               # envío a Kaggle → entregables/envio_kaggle.csv
uv run pytest                               # tests
uv run python scripts/trazabilidad.py       # ¿cada criterio tiene su test y cada estrategia de SPECS.md está en el código?
uv run streamlit run src/app.py             # cuadro de mando
```

Al empezar, la plantilla ya trae resueltos la carga de datos, el baseline, la validación cruzada y un modelo mínimo. Pasan los tests del ejemplo resuelto (CA1–CA4) y los del contrato CM2, CM3, CM4 y CM7. **CM1, CM5 y CM6 fallan, y es lo esperado:** el modelo mínimo tasa algunas viviendas en negativo, falta `src/explicar.py` y todavía no hay estrategias vuestras.

## Uso de IA

<!-- Qué agente habéis usado, cómo lo habéis guiado y qué habéis tenido que corregir. -->

## Resumen para la dirección de riesgos

<!--
Una página, para Núria Casals. Sin jerga técnica y con cifras.

**Qué hemos hecho con los datos.** Las dos o tres decisiones que más han cambiado el error, con cifras.

**Cuánto se equivoca.** Error medio del modelo y del baseline, con su intervalo, y qué significa para una hipoteca típica.

**Dónde falla.** Los segmentos en los que no os fiaríais del modelo.

**Por qué tasa lo que tasa.** Las variables que más pesan y qué NO se puede concluir de ellas.

**Recomendación.** ¿Lo pondríais en producción? Para qué viviendas sí, para cuáles no, y qué haría falta para fiarse más.

**Kaggle.** Error estimado en validación (con su intervalo) frente al error en Kaggle. ¿Acertasteis?
-->
