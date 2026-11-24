# Miniproyecto 2 · De CSV a modelo de tasación (Banc Avellaner)

Borrador · 19/11/2026 · @santi

## Contexto y encargo

En este miniproyecto, cada equipo analiza datos de ventas de viviendas de Barcelona y su área metropolitana, decide cómo prepararlos comprobando con cifras qué funciona, y construye un modelo que tasa viviendas y un cuadro de mando (*dashboard*) para entenderlo y validarlo.

**El banco.** Banc Avellaner es un banco ficticio con oficinas en Barcelona y en el área metropolitana. Cada mes concede cientos de hipotecas, y para cada una necesita saber cuánto vale la vivienda que queda como garantía. Hoy lo hace con tasadores humanos: es lento, caro y cada tasador decide a su manera.

**Qué es real y qué es simulado.** Los 73 barrios de Barcelona, sus límites y sus indicadores (viviendas, población, superficie media, años de construcción, valor catastral, renta) son **reales**, de Open Data BCN. El nivel de precios de cada municipio del área metropolitana se basa en precios publicados. Las direcciones y los códigos postales también son **reales** (ICGC). Las viviendas, las operaciones de 2023 a 2025 y sus precios son **simulados** para que se parezcan a ese mercado: a cada vivienda simulada se le ha dado la dirección real más cercana, así que una dirección de los datos no significa que allí se haya vendido nada. Las cifras que obtengáis no describen ventas reales.

**El encargo.** Este es el mensaje que la directora de riesgos, Núria Casals, ha enviado al equipo de datos:

> Queremos una primera tasación automática para cada hipoteca, y que un tasador solo revise los casos dudosos. Pero no voy a firmar nada que no entienda. Necesito saber qué habéis hecho con los datos y por qué, cuánto se equivoca el modelo y con qué seguridad lo sabemos, en qué viviendas falla más y por qué tasa lo que tasa: si un cliente o un auditor me pregunta por qué su piso vale 400.000 euros, tengo que poder contestarle. Y al final, decidme si lo usaríais y para qué viviendas.

Los datos vienen tal cual los exportan los sistemas del banco y de las agencias. No están limpios, y muchas decisiones no tienen una respuesta obvia: ¿qué se hace con una planta que pone "Entlo"? ¿Es un precio de venta el de un anuncio que se retiró sin venderse? Este miniproyecto va de **tomar esas decisiones con datos**, no por intuición.

## Preguntas de negocio

El trabajo tiene que responder, como mínimo, a estas cinco preguntas. Las subpreguntas son orientativas.

1. **¿Qué habéis hecho con los datos y por qué?** Problemas encontrados, estrategias que habéis probado, cuánto ha cambiado el error con cada una y qué habéis decidido. Incluye al menos una característica nueva creada por vosotros, y si ha servido o no.
2. **¿Cuánto se equivoca?** Error medio en euros y en porcentaje, comparado con una tasación ingenua (el *baseline*), y con su intervalo de confianza: ¿la mejora es real o puede ser ruido?
3. **¿Dónde falla?** Error por tipo de vivienda, por zona (distrito o municipio) y por rango de precio, y en el mapa. ¿Hay zonas o viviendas que tasa sistemáticamente de más o de menos?
4. **¿Por qué tasa lo que tasa?** Qué variables pesan más y cómo se construye la tasación de una vivienda concreta, variable a variable.
5. **¿Qué no podemos afirmar?** Qué dicen los coeficientes y qué no (un coeficiente no es el efecto de reformar el piso o de instalar un ascensor).

Y una sexta que no es un gráfico: **¿lo pondríais en producción?** Vuestra defensa oral termina con una recomendación: para qué viviendas sí, para cuáles no y qué haría falta para fiarse más.

## Analizar, decidir y validar

La primera sesión es para entender los datos y decidir cómo prepararlos. Cada decisión se valida con el mismo procedimiento, para que las cifras se puedan comparar.

**1. Encontrad los problemas.** Explorad los datos y documentad en `SPECS.md` al menos seis problemas de calidad, con cifras: qué columna, qué valor raro y cuántas veces aparece. Para cada uno, decid en qué fase lo trataréis.

**2. Trabajad por fases.** Las estrategias se prueban en cuatro fases, en este orden. Lo que aceptáis en una fase es el punto de partida de la siguiente, y así sabréis qué ha aportado cada tipo de decisión. Algunos ejemplos de lo que tendréis que decidir en cada una:

| Fase | Qué se decide | Por ejemplo |
| --- | --- | --- |
| 1 · Limpieza | Qué filas y qué valores son errores | Qué precios son de verdad precios de venta y qué hacer con los imposibles. Qué significa un cero en una superficie o en una terraza. Qué hacer con los valores extremos |
| 2 · Transformaciones | Cómo se pasa cada variable a una forma que el modelo entienda | Si el precio se modela tal cual o en logaritmo. Cómo se representa la ubicación: barrio, distrito, municipio o coordenadas. Cómo convertir en números columnas de texto como la planta o el ascensor. Qué hacer con los nulos: eliminar la columna, imputarla (¿con qué valor?) o imputarla y marcar que faltaba |
| 3 · Variables nuevas | Qué variables creáis a partir de las que hay | Al menos una: algo que el tasador tendría en cuenta y que no está directamente en los datos. Decid antes de probarla por qué creéis que ayudará |
| 4 · Modelo | Qué estimador lineal y con qué parámetro | Ridge en lugar de la regresión lineal, **ajustando λ** (`alpha` en scikit-learn) con al menos cuatro valores, de muy pequeño a grande |

**3. Primero la hipótesis.** Cada estrategia se escribe en `SPECS.md` antes de ejecutarla: qué cambia respecto a su referencia (una sola cosa) y qué esperáis que pase.

**4. Comparad con validación cruzada.** Cada estrategia se evalúa con las **mismas cinco particiones**, que vienen fijadas en el fichero `particiones.csv` (valores del 1 al 5; el resto de filas son `validacion`). La plantilla ya las añade como columna `particion` al cargar los datos. Para cada estrategia se guarda el MAE de cada partición, su media y su desviación. Para decidir si una estrategia es mejor que su referencia, **comparad partición a partición**: hay particiones más difíciles que otras para todas las estrategias a la vez, así que la desviación de cada una no sirve para compararlas (es la idea de las muestras pareadas de la sesión 07). Escribid en `SPECS.md` vuestra regla antes de mirar los resultados; por ejemplo, "mejora en al menos 4 de las 5 particiones y en al menos 1.000 € de media".

**5. Decidid y anotadlo.** Al acabar cada fase, lo que aceptáis va a "Decisiones" de `SPECS.md` con las cifras que lo justifican. El λ también se elige así, con las cinco particiones y nunca con `validacion`. Una característica que no mejora el error también es un resultado: se anota y se descarta.

**Ojo con mirar demasiado.** Las filas con `particion = validacion` no se usan para comparar estrategias. Solo se usan **una vez**, al final, para medir el modelo elegido. Si las usáis para decidir, el error que contéis será optimista (es el mismo problema que las comparaciones múltiples de la sesión 07).

## Reglas del modelo

- **Solo modelos lineales**: regresión lineal, Ridge, Lasso o ElasticNet de scikit-learn. Podéis transformar variables y crear las que queráis, pero el estimador final es lineal. Los árboles y los *ensembles* llegan en las sesiones 14 y 15.
- **Todo el preprocesado va dentro del *pipeline*** del modelo, para que funcione con filas crudas y para que, en la validación cruzada, nada se calcule con datos de la partición que se evalúa (fuga de datos o *leakage*).
- **La limpieza del precio va en `limpiar_objetivo()`** y decide **fila a fila**, con reglas fijas: por ejemplo, quitar una fila según su `estado_operacion` o corregir un precio imposible. Se aplica a todo el entrenamiento antes de separar las particiones, así que no puede usar medianas, percentiles ni nada calculado con otras filas; lo que aprenda de los datos va dentro del *pipeline*. Así, todas las estrategias se miden con las mismas viviendas.
- **Solo variables que el banco conoce cuando tasa**, antes de la venta.
- **El conjunto de test no tiene precio.** Solo se usa para enviar predicciones a Kaggle.

## Cómo se trabaja y qué se entrega

Como en el miniproyecto 1, **el código lo genera un agente de IA** y vuestro trabajo es analizar, especificar, verificar y decidir. Cada equipo de 3 o 4 personas trabaja en un repositorio creado desde la plantilla `mp2-plantilla`, con los mismos seis ficheros:

| Fichero | Qué es | Quién lo escribe |
| --- | --- | --- |
| `AGENTS.md` | Reglas y comandos para el agente, con el contrato mínimo del profesorado (CM1–CM7) | Viene completo; podéis añadir reglas |
| `SPECS.md` | **Qué** construimos: objetivo, problemas de los datos, estrategias y experimentos en cuatro fases, decisiones de modelado, requisitos y criterios de aceptación | Equipo |
| `DESIGN.md` | **Cómo se ve y se comporta** el cuadro de mando: pantallas, gráficos, formatos | Equipo |
| `ARCHITECTURE.md` | **Cómo está construido**: carpetas, módulos, flujo de datos y del modelo | Equipo (el agente puede proponer) |
| `TASKS.md` | Tareas pequeñas, con la verificación de cada una | El agente propone, el equipo aprueba y verifica |
| `README.md` | Para personas: cómo ejecutarlo, uso de IA y resumen para la dirección | Equipo |

**Qué cambia respecto al miniproyecto 1.** Ahora en `SPECS.md` también se especifican los experimentos y el modelo, no solo los datos, y se hace por fases: limpieza, transformaciones, variables nuevas y modelo. Cada estrategia que queráis probar se escribe antes de pedirla al agente, con lo que esperáis que pase. Si el agente elige una variable, una transformación o un `alpha` que no está en `SPECS.md`, se para y se decide.

**La plantilla trae un ejemplo resuelto**: la carga de datos, el baseline (lo que haría un tasador con prisa: el €/m² mediano del barrio × la superficie) y un modelo mínimo (regresión lineal con las variables numéricas que no tienen nulos), los dos evaluados con las cinco particiones, con sus requisitos, sus criterios y sus tests. Es el punto de partida contra el que mediréis cada mejora, y ya veréis que el modelo mínimo es mucho peor que el baseline: ganarle no es fácil. También trae el esqueleto del cuadro de mando: la navegación entre pantallas y la lectura de los resultados.

**El ciclo de cada fase**

1. Escribís en `SPECS.md` los problemas, las estrategias con su hipótesis, los requisitos y los criterios de la fase.
2. Pedís al agente que **revise** lo escrito y señale ambigüedades. Corregís.
3. El agente propone las tareas de la fase en `TASKS.md` y vosotros las aprobáis. La primera es siempre la de los tests.
4. El agente escribe los tests de aceptación de la fase en `tests/acceptance/`, uno o más por criterio, marcados con `@pytest.mark.criterio("CA…")`. Los revisáis (¿el ejemplo es el de `SPECS.md`?, ¿el resultado esperado está calculado a mano?) y los aprobáis.
5. El agente implementa **una** tarea cada vez. Verificáis (tests, lectura del *diff*, una cifra a mano) y completáis `Verificado por:`.
6. Ejecutáis `src.experimentos`, aplicáis vuestra regla de decisión y anotáis el resultado y la decisión en `SPECS.md`. Si algo cambia, se cambia primero `SPECS.md` y después el código.

**Contrato mínimo del profesorado.** Está en `AGENTS.md` y se comprueba con `tests/acceptance/test_contrato_modelo.py`, que no se modifica.

| Criterio | Qué comprueba |
| --- | --- |
| CM1 | El modelo guardado predice sobre filas crudas del test (con nulos y barrios que no aparecen en el entrenamiento) sin errores, sin valores vacíos y con precios positivos |
| CM2 | El fichero de envío tiene el formato de `sampleSubmission.csv`: columnas `index` y `precio`, una fila por vivienda del test |
| CM3 | `reports/metricas.json` da el MAE y el RMSE del baseline y del modelo final en la partición de validación (tras `limpiar_objetivo()`), cada uno con su intervalo de confianza del 95 % por *bootstrap* |
| CM4 | Entrenar dos veces da exactamente las mismas predicciones |
| CM5 | El estimador final es lineal y `explicar(modelo, X)` devuelve el intercepto y la contribución de cada variable para cada fila de `X`: sumados, dan la predicción del modelo, en la escala en la que trabaja |
| CM6 | `reports/experimentos.csv` tiene una fila por estrategia probada, con el MAE de cada una de las cinco particiones, su media y su desviación. Incluye como mínimo el baseline, el modelo mínimo, tres estrategias y una característica nueva |
| CM7 | `limpiar_objetivo()` decide fila a fila: limpiar una parte de los datos da lo mismo que limpiarlos todos y quedarse con esa parte |

Los criterios CA de vuestro `SPECS.md` van más allá. Por ejemplo, en la fase 2: "CA… (R…). '3ª planta', '3º' y 'Planta 3' se convierten en la planta 3"; o en la fase 4: "CA… (R…). Para la vivienda de ejemplo, la contribución de `habitaciones` calculada a mano coincide con la de `explicar()`".

**El cuadro de mando** tiene, como mínimo, cuatro pantallas:

| Pantalla | Responde a |
| --- | --- |
| Experimentos | Pregunta 1: qué estrategias se han probado, cuánto ha cambiado el error con cada una y cuál se ha elegido |
| Rendimiento | Pregunta 2: error del modelo final frente al baseline con intervalos de confianza, y precio real frente a predicho |
| Dónde falla | Pregunta 3: error por tipo, zona y rango de precio, y mapa de residuos |
| Abrir la caja | Preguntas 4 y 5: coeficientes comparables entre sí y desglose de la tasación de una vivienda elegida |

**Kaggle.** Cada equipo se une a la competición del curso ([[ENLACE KAGGLE]]) con el nombre de su repositorio (`mp2-equipo-XX`) y envía las predicciones del modelo final. Los precios del test solo los tiene el profesorado. La métrica es el MAE (error absoluto medio), se admiten [[N]] envíos al día y la competición cierra el [[FECHA Y HORA DE CIERRE]]. La posición en la clasificación no cuenta para la nota. Lo que cuenta es que sepáis predecir vuestro propio error: en la defensa compararéis el error que estimasteis en validación, con su intervalo, con el que da Kaggle.

**Qué se entrega** (el último *commit* antes del final de la sesión 13)

| Entregable | Se comprueba con |
| --- | --- |
| Los seis ficheros completos | Lectura del profesorado |
| Experimentos reproducibles | `uv run python -m src.experimentos` |
| Modelo final y envío | `uv run python -m src.entrenar` y `uv run python -m src.predecir` |
| Cuadro de mando | `uv run streamlit run src/app.py` |
| Tests de aceptación de todos vuestros criterios | `uv run pytest` en verde |
| Trazabilidad completa | `uv run python scripts/trazabilidad.py` en verde |
| Al menos un envío a Kaggle | Clasificación de la competición |
| Resumen para la dirección (una página) | Sección final de `README.md`, con la respuesta a "¿lo pondríais en producción?" |
| Defensa oral | 5 minutos en directo, con el cuadro de mando, en la sesión 13 |

## Calendario

| Sesión | Tramo | Min | Qué hacéis |
| --- | --- | --- | --- |
| 12 | Encargo | 15 | Presentación del caso y de la rúbrica. Equipos, repositorio desde la plantilla y alta en Kaggle. |
| 12 | Concepto | 20 | Cómo comparar estrategias sin engañarse: particiones fijas, comparar sobre las mismas particiones y no gastar la validación. Recorrido por el ejemplo resuelto. |
| 12 | Análisis de datos | 40 | Explorar, documentar los problemas en `SPECS.md`, escribir la regla de decisión y las estrategias de las fases 1 y 2, con lo que esperáis de cada una. |
| 12 | Experimentos | 45 | Fases 1 (limpieza) y 2 (transformaciones): comparar cada estrategia con su referencia con validación cruzada y decidir. |
| Entre sesiones | — | — | Fase 3 (variables nuevas) y `DESIGN.md`. |
| 13 | Iteración | 70 | Fase 4 (Ridge y λ), modelo final, `explicar()`, cuadro de mando y envío a Kaggle. |
| 13 | Preparación | 10 | Ensayar la defensa de 5 minutos. |
| 13 | Puesta en común | 20 | 4 minutos por equipo y 2 minutos de preguntas. |
| 13 | Cierre | 10 | Puesta en común y puente con la sesión 14: ¿cuánto ganaríamos con un modelo más complejo y cuánto perderíamos al explicarlo? |

**Hito de control al final de la sesión 12:** `SPECS.md` documenta al menos seis problemas de calidad y vuestra regla de decisión, y las fases 1 y 2 están ejecutadas, con sus cifras y sus decisiones. Al final del miniproyecto, `reports/experimentos.csv` cumple CM6.

## Normas de trabajo

El agente escribe el código, pero sois responsables de todo lo que entregáis.

- **Cualquier agente vale**, siempre que siga `AGENTS.md`. Si vuestro agente no lo lee solo, pedidle al empezar que lo lea.
- **Una tarea cada vez.** Nada se marca como hecho en `TASKS.md` sin la línea `Verificado por:` de una persona que diga cómo lo comprobó.
- **No escribís en `src/` ni en `tests/`.** Todo ese código lo escribe el agente. Vosotros escribís los `.md`, exploráis en `notebooks/` (ahí sí escribís código) y verificáis. Si algo del código está mal, se corrige la especificación y se pide el cambio al agente.
- **El agente no toca `SPECS.md` ni `DESIGN.md`, ni `ARCHITECTURE.md` sin vuestra aprobación.** Los tests de `tests/acceptance/` los escribe el agente, en su propia tarea y antes de implementar lo que comprueban. Los valida una persona del equipo, que lo anota en `Verificado por:`.
- **Nunca se cambia un test para que pase.** Si un test falla, primero se decide si el error está en el código o en la especificación.
- **Primero la hipótesis, después el experimento.** Cada estrategia se escribe en `SPECS.md`, con lo que esperáis que pase, antes de ejecutarla.
- **Defensa individual.** En la sesión 13, el profesorado elige al azar a un miembro del equipo, que debe explicar cualquier función de `src/`, cualquier cifra del cuadro de mando y cualquier decisión de `SPECS.md`, aunque el código lo haya escrito el agente. También puede elegir una vivienda rara del test y pedir que expliquéis qué hace vuestro modelo con ella.
- **Los datos originales no se tocan:** `data/raw/` es de solo lectura.
- **Ojo con Kaggle.** La clasificación de Kaggle no sirve para elegir estrategias: elegir mirando el test es lo mismo que mirar la validación demasiadas veces.


## Materiales

| Material | Para qué | Cuándo |
| --- | --- | --- |
| Datos y diccionario | Ficheros, columnas y particiones | Antes de empezar |
| Guía: comparar estrategias con validación cruzada | Cómo diseñar un experimento y leer sus resultados | Sesión 12 |
| Sesión 13 · Cierre y defensa | Checklist de calidad, guía de la defensa y plantilla del resumen | Sesión 13 |

**Repositorio plantilla** (`mp2-plantilla`): `AGENTS.md` completo; `SPECS.md` organizado en las cuatro fases y, como `DESIGN.md`, `ARCHITECTURE.md` y `TASKS.md`, con sus secciones e indicaciones; el ejemplo resuelto (carga, baseline y modelo mínimo con validación cruzada); el esqueleto del cuadro de mando; los tests del contrato mínimo (CM1–CM7); el script de trazabilidad y un notebook de exploración. Los datos se descargan con `uv run python scripts/descargar_datos.py`.

**Fuentes de los datos reales:** límites e indicadores de los barrios de Open Data BCN y CartoBCN (Ajuntament de Barcelona, CC-BY 4.0): catastro y padrón de 2026, renta de 2024 y precio de oferta por barrio de 2015. Nivel de precios de los municipios del área metropolitana a partir de precios de oferta publicados (octubre de 2026). Direcciones y códigos postales del Institut Cartogràfic i Geològic de Catalunya, «Adreces simplificat» v1r0 de 09/10/2026 (CC BY 4.0). Las viviendas, las operaciones y los precios son simulados.
