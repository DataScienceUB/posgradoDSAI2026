# Clase de ETL: de datos crudos a datos útiles

Una **clase práctica de 2 horas** sobre **ETL** (Extract, Transform, Load: extraer, transformar, cargar) con datos reales de Eurostat sobre el gasto público en educación (% del PIB). Los estudiantes trabajan en un único **notebook de Jupyter** guiado: leen código, lo ejecutan, rellenan pequeños huecos y comprueban sus propias respuestas.

Pensada para estudiantes de ciencias (física, matemáticas…) **sin experiencia previa en Python**. Hay disponible un asistente de IA opcional (GitHub Copilot) para aprender por tu cuenta; la clase en sí no depende de él.

## Qué aprenden los estudiantes

- Qué es ETL y qué ocurre en cada fase.
- Qué es un DataFrame y las operaciones básicas de pandas: seleccionar, filtrar, melt, unión (join), agrupar, pivot, clasificar.
- Por qué los datos reales están "sucios", y que limpiarlos implica tomar **decisiones** (por ejemplo, con los valores ausentes).
- Cómo comprobar un resultado: comprobaciones cruzadas, comprobaciones de rango, duplicados, errores de conversión silenciosos.
- Cómo guardar resultados en distintos tipos de destino (CSV, Parquet, SQLite, la base de datos analítica DuckDB, documentos JSON como en una base de datos NoSQL) y representarlos en gráficos claros.
- (Parte 6, opcional) Cómo aplicarlo todo a un conjunto de datos nuevo: unir (merge) tres tablas, filtrar, hacer pivot, ordenar y escribir una pequeña función.

## Requisitos

- Ordenador con macOS, Windows o Linux y 4 GB de RAM.
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (instala Python y las bibliotecas).
- Solo necesitas conexión a internet para el paso opcional de descarga y para la **Parte 6**, que descarga MovieLens 1M (unos 6 MB) la primera vez. Las Partes 0–5 funcionan sin conexión con los archivos de `data/raw/`. Para usar la Parte 6 sin conexión, descarga [ml-1m.zip](https://grouplens.org/datasets/movielens/1m/) una vez y descomprímelo en `data/downloads/`, de modo que exista `data/downloads/ml-1m/ratings.dat`.

```bash
uv sync                           # instala las dependencias (una sola vez)
uv run jupyter lab notebooks/etl_class.ipynb
```

¿Prefieres VS Code? Abre `notebooks/etl_class.ipynb` y selecciona como kernel el `.venv` que ha creado `uv sync` (*Select Kernel → Python Environments → .venv*). El kernel debe ser **Python 3 (ipykernel)** o `.venv/bin/python`, no **Chatbook**: Chatbook es el kernel del asistente de IA, que envía cada celda al modelo de chat en lugar de ejecutarla como Python (y falla con "No chat model configured" si no has iniciado sesión).

## Asistente de IA (opcional)

JupyterLab incluye [Notebook Intelligence](https://github.com/notebook-intelligence/notebook-intelligence), que se conecta a **GitHub Copilot** (gratuito para estudiantes con [GitHub Education](https://education.github.com/)).

1. Haz clic en el icono de Notebook Intelligence de la barra lateral izquierda, abre **Settings** (icono del engranaje) y pulsa **Sign in** con tu cuenta de GitHub.
2. Haz preguntas en el panel de chat, o pulsa **Ctrl+G** (**Cmd+G** en macOS) dentro de una celda de código para generar código.

El asistente sigue las instrucciones de [`AGENTS.md`](AGENTS.md): explica el código que genera y enlaza a la documentación de las bibliotecas que usa. Inicia JupyterLab desde esta carpeta (como arriba) para que encuentre ese archivo. Lee las explicaciones: el objetivo es entender el código, no solo ejecutarlo.

## Horario (2 horas)

| Tiempo | Bloque | Contenido |
|---|---|---|
| 0–15 min | **Diapositivas** + Parte 0 | Concepto de ETL; los estudiantes escriben su predicción; se empieza el notebook |
| 15–30 min | Parte 1 | DataFrames en diez minutos |
| 30–50 min | Parte 2 · **Extract** | Mirar los archivos como texto, leer CSV y TSV, inspeccionar |
| 50–90 min | Parte 3 · **Transform** | Melt, separar value/flag, unión (join), agregados, **votación sobre los valores ausentes**, agrupar, pivot, clasificar, comprobaciones, **caza de errores** |
| 90–110 min | Parte 4 · **Load** | Guardar en CSV/Parquet/SQLite, DuckDB y documentos JSON, volver a leer, gráficos, pipeline con un solo comando |
| 110–120 min | Parte 5 | Reflexión y cierre |
| Extra (unos 45 min) | Parte 6 · **Manos a la obra** | Deberes opcionales: la hoja de ejercicios original sobre películas y valoraciones (MovieLens 1M), en pequeños pasos guiados |

## Estructura del proyecto

```
notebooks/etl_class.ipynb        Notebook del estudiante (ejercicios con huecos y comprobaciones)
etl/                             Paquete auxiliar: los mismos pasos como funciones reutilizables
  extract.py  transform.py  load.py  pipeline.py  movielens.py
data/raw/                        Archivos crudos de Eurostat (sin modificar)
data/reference/                  Tablas de consulta: códigos de país -> nombres, flags de Eurostat
data/exercises/                  Archivo con errores sembrados (caza de errores)
data/downloads/                  Donde van las descargas opcionales (Eurostat, MovieLens 1M)
data/processed/  output/         Generados por el notebook (ignorados por git)
slides/                          Las diapositivas de la clase: what_is_etl.html (ábrelo en un navegador) y what_is_etl.pdf
```

Ejecuta el pipeline completo sin el notebook:

```bash
uv run python -m etl.pipeline
```

## Datos

Fuente: [Eurostat](https://ec.europa.eu/eurostat), datos abiertos. Conjunto de datos [`educ_uoe_fine06`](https://ec.europa.eu/eurostat/databrowser/view/educ_uoe_fine06/default/table): gasto público en educación como % del PIB, todos los niveles desde educación infantil hasta educación superior (niveles CINE 2011 02–8), 2012–2023.

- `data/raw/educ_uoe_fine06.tsv`: el corte `A.PC_GDP.ED02-8` tal como lo sirve la API: <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/educ_uoe_fine06/A.PC_GDP.ED02-8.?format=TSV&compressed=false>
- `data/raw/educ_uoe_fine06_long.csv`: el mismo corte en formato SDMX-CSV con etiquetas: <https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/educ_uoe_fine06/1.0/A.PC_GDP.ED02-8.*?format=csvdata&formatVersion=2.0&labels=name>
- `data/reference/geo_codes.csv` y `data/reference/eurostat_flags.csv`: construidos a partir de las listas de códigos de Eurostat `GEO` y `OBS_FLAG`.

Descargados el 21 de octubre de 2026 (actualización de datos de Eurostat del 15 de septiembre de 2026).
