import mlflow
import mlflow.sklearn

mlflow.set_experiment("industrial-maintenance")

with mlflow.start_run():

    n_estimators = 200

    mlflow.log_param("model", "RandomForest")
    mlflow.log_param("n_estimators", n_estimators)

    # Train model here

    # mlflow.log_metric("accuracy", accuracy)
    # mlflow.sklearn.log_model(model, "model")
