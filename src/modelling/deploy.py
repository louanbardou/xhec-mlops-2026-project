# Deployment: retrains the model every Monday at 3am. Needs the prefect server to be running.

from src.modelling.main import main

if __name__ == "__main__":
    main.serve(
        name="weekly-retraining",
        cron="0 3 * * 1",
        parameters={"trainset_path": "data/abalone.csv"},
    )
