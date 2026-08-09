"""volumen_t3.py — Mide T3 (join) con N=4 fijo, variando el VOLUMEN de datos
(10%, 50%, 100% del dataset), para poder ajustar alpha (costo secuencial/registro),
beta (overhead fijo de arranque) y gamma (costo distribuido/registro) de la Ec. 4
(umbral de rentabilidad). Coherente con el protocolo de medicion.py y
transformaciones_spark.py ya usados por el equipo en PE-U4.

Uso (desde la raíz del repo, mismo patrón de volúmenes que docker run del README):
    docker run --rm -v "$(pwd)/src:/app/src" -v "$(pwd)/data:/app/data" \
      -v "$(pwd)/resultados:/app/resultados" \
      pe-u4-acc-spark volumen_t3.py
"""

import argparse
import json
import os

from pyspark.sql import SparkSession

import referencia
from medicion import medir
from transformaciones_spark import cargar_dataset, cargar_regiones, t3_join


def crear_sesion_n4(app_name: str) -> SparkSession:
    return (
        SparkSession.builder.appName(app_name)
        .master("local[4]")
        .config("spark.executor.instances", "4")
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="../data/raw/fcc_consumer_complaints.csv")
    parser.add_argument("--resultados-dir", default="../resultados")
    parser.add_argument(
        "--fracciones", default="0.10,0.50,1.00",
        help="Fracciones del dataset a probar, separadas por coma"
    )
    args = parser.parse_args()

    os.makedirs(args.resultados_dir, exist_ok=True)
    fracciones = [float(f) for f in args.fracciones.split(",")]

    resultados = []
    for frac in fracciones:
        print(f"\n>>> T3_join con N=4 fijo, fraccion={frac:.2f} del dataset ...")
        spark = crear_sesion_n4(app_name=f"pe-u4-acc-spark-vol-{int(frac*100)}pct")

        df_full = cargar_dataset(spark, args.data)
        n_total = df_full.count()

        if frac < 1.0:
            df = df_full.sample(withReplacement=False, fraction=frac, seed=42)
        else:
            df = df_full

        regiones = cargar_regiones(spark)
        n_filas = df.count()

        r = medir(
            "T3_join_volumen",
            lambda: t3_join(df, regiones),
            reps=5,
            warmup=1,
            materialize=lambda d: d.count(),
        )

        print(f"  fraccion={frac:.2f}  n_filas={n_filas}  mediana={r.mediana_s:.4f}s "
              f"(tiempos: {[round(t, 4) for t in r.tiempos_s]})")

        resultados.append({
            "fraccion": frac,
            "n_filas": n_filas,
            "n_total_dataset": n_total,
            "mediana_s": r.mediana_s,
            "tiempos_s": r.tiempos_s,
        })

        spark.stop()

    out_path = os.path.join(args.resultados_dir, "t3_escalado_volumen.json")
    with open(out_path, "w") as f:
        json.dump({"N_executors_fijo": 4, "mediciones": resultados}, f, indent=2)

    print(f"\nGuardado: {out_path}")
    print("Con esto (n, T(n)) para 3 volúmenes distintos, ya se puede ajustar")
    print("alpha, beta y gamma de la Ec. 4 por mínimos cuadrados.")


if __name__ == "__main__":
    main()
