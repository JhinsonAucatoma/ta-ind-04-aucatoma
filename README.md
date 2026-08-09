# TA-IND-04 — Informe Técnico Individual

**Universidad:** Universidad Técnica Estatal de Quevedo
**Facultad:** Facultad de Ciencias de la Computación
**Carrera:** Ingeniería de Software
**Asignatura:** Aplicaciones Distribuidas (ISR-701) — Unidad 4
**Período académico:** 2026–2027 PPA
**Docente:** Ing. Guerrero-Ulloa

## Identificación del estudiante

- **Estudiante:** Jhinson Stalyn Aucatoma Celorio
- **Correo:** jaucatomac@uteq.edu.ec
- **Equipo de PE-U4:** ACC — Soporte Técnico ISP
- **Integrantes del equipo:** Alvarez Parraga Jeremy Alexis, Aucatoma Celorio Jhinson Stalyn, Carpio Mendoza Carlos Jose
- **PFC de referencia:** AGLS — TiendaTech
- **Repositorio del PFC:** https://github.com/JoseLozanoMorales/PFC-AppsDistribuidas
- **Transformación declarada como foco individual:** T3 — Join de dos DataFrames

## Trazabilidad de los datos base (PE-U4)

- **Repositorio de origen:** https://github.com/carlospatroner-boop/pe-u4-spark-Soporte-Tecnico-ISP
- **Commit exacto:** `c5fd274`
- **Plataforma de ejecución:** contenedor Docker local (`eclipse-temurin:21-jdk-jammy`), PySpark 4.1.2, modo `local[N]` con N ∈ {1, 2, 4}

Los datos de las Secciones 3 y 4 del informe provienen directamente de ese commit.
Los datos de la Sección 6 (mediciones a distinto volumen) fueron generados de forma
individual mediante el script `volumen_t3.py`, ejecutado sobre Google Colab.
## Estructura del repositorio

- `README.md`
- `LICENSE`
- `docs/`
    - `TA_IND_04_Informe.tex`
    - `TA_IND_04_Informe.pdf`
    - `references.bib`
- `datos/`
    - `tiempos_resumen.csv`
    - `tiempos_crudos.csv`
- `volumen_t3.py`
- `figuras/`
    - `fig_speedup_amdahl_t3.png`


## Instrucciones exactas de compilación

Requisitos: distribución LaTeX con `pdflatex` y `biber` (p. ej. TeX Live o MiKTeX).

Desde la carpeta `docs/`, ejecutar en este orden exacto:

```bash
pdflatex TA_IND_04_Informe.tex
biber TA_IND_04_Informe
pdflatex TA_IND_04_Informe.tex
pdflatex TA_IND_04_Informe.tex
```

El PDF resultante (`TA_IND_04_Informe.pdf`) se genera en la misma carpeta `docs/`.
Esta secuencia fue verificada en una carpeta limpia antes de la entrega.

## Declaración de uso de inteligencia artificial generativa

Se utilizó Claude (Anthropic) como herramienta de apoyo durante la elaboración del
documento, incluyendo mejora de redacción y generación del script instrumental
`volumen_t3.py`. El detalle completo está en la Sección 9 del informe
(`docs/TA_IND_04_Informe.tex`).