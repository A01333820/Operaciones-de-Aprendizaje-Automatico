from pathlib import Path
import tempfile
import mlflow


def main():
    # Configurar SQLite como almacenamiento
    mlflow.set_tracking_uri("sqlite:///mlflow.db")

    # Crear o seleccionar experimento
    mlflow.set_experiment("hello_mlflow_experiment")

    with mlflow.start_run(run_name="experimento_trivial"):

        # Registrar parámetro
        multiplicador = 2
        mlflow.log_param("multiplicador", multiplicador)

        # Registrar métrica
        resultado = 5 * multiplicador
        mlflow.log_metric("resultado", resultado)

        # Crear y registrar artefacto
        with tempfile.TemporaryDirectory() as temp_dir:
            ruta = Path(temp_dir) / "resultado.txt"
            ruta.write_text(
                f"5 x {multiplicador} = {resultado}\n",
                encoding="utf-8"
            )
            mlflow.log_artifact(str(ruta))

        print("Experimento registrado correctamente")
        print(f"Run ID: {mlflow.active_run().info.run_id}")


if __name__ == "__main__":
    main()