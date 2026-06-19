class CareerGrowthService:
    
    def predict(self, similar_profiles):

        growth = (
            similar_profiles[
                "career_growth_score"
            ].mean()
        )

        if growth >= 63:

            level = "Alto"

        elif growth >= 51:

            level = "Medio"

        else:

            level = "Bajo"

        return {

            "level":
                level,

            "score":
                round(
                    float(growth),
                    2
                )
        }