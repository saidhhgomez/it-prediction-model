from pathlib import Path

import joblib
import pandas as pd


class PredictionService:

    def __init__(self):

        root_dir = Path(__file__).resolve().parents[2]

        model_path = (
            root_dir
            / "models"
            / "future_demand"
            / "future_demand_model.pkl"
        )

        encoder_path = (
            root_dir
            / "models"
            / "future_demand"
            / "future_demand_encoder.pkl"
        )

        self.model = joblib.load(
            model_path
        )

        self.encoder = joblib.load(
            encoder_path
        )

    def predict(self, indicators):

        sample_df = pd.DataFrame(
            [indicators]
        )

        prediction = self.model.predict(
            sample_df
        )

        predicted_label = (
            self.encoder
            .inverse_transform(prediction)[0]
        )

        probabilities = (
            self.model
            .predict_proba(sample_df)[0]
        )

        probability_dict = {}

        for i, class_num in enumerate(
            self.model.classes_
        ):

            label = (
                self.encoder
                .inverse_transform(
                    [class_num]
                )[0]
            )

            probability_dict[label] = round(
                float(probabilities[i]) * 100,
                2
            )

        confidence = round(
            float(max(probabilities)) * 100,
            2
        )

        return {
            "prediction": predicted_label,
            "confidence": confidence,
            "probabilities": probability_dict
        }