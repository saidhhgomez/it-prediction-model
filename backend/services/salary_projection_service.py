class SalaryProjectionService:
    
    def predict(self, similar_profiles):

        salary = (
            similar_profiles[
                "salary_usd"
            ].mean()
        )

        if salary >= 180000:

            level = "Muy Alto"

        elif salary >= 120000:

            level = "Alto"

        elif salary >= 80000:

            level = "Medio"

        else:

            level = "Bajo"

        return {

            "level":
                level,

            "average_salary_usd":
                round(
                    float(salary),
                    2
                )
        }