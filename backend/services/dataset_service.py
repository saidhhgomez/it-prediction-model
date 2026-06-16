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

        self.df = pd.read_csv(
            dataset_path
        )

    def get_dataset(self):

        return self.df