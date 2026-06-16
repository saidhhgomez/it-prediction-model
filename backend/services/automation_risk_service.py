class AutomationRiskService:

    def predict(self, similar_profiles):

        risk = (
            similar_profiles[
                'automation_risk'
            ].mean()
        )

        if risk >= 66:

            level = "Alto"

        elif risk >= 33:

            level = "Medio"

        else:

            level = "Bajo"

        return {

            "level": level,

            "score": round(
                float(risk),
                2
            )
        }