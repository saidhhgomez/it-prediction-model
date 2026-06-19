from pathlib import Path

import pandas as pd


class DatasetService:

    def __init__(self):

        root_dir = Path(__file__).resolve().parents[2]

        dataset_path = (
            root_dir
            / "datasets"
            / "ai_job_dataset.csv"
        )

        if not dataset_path.exists():

            raise FileNotFoundError(
                f"Dataset no encontrado: {dataset_path}"
            )

        self.df = pd.read_csv(
            dataset_path
        )

        if self.df.empty:

            raise ValueError(
                "El dataset está vacío"
            )

    def get_dataset(self):

        return self.df.copy()