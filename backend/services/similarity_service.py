import pandas as pd


class SimilarityService:

    def find_similar_profiles(
        self,
        df: pd.DataFrame,
        request
    ):

        if df.empty:

            raise ValueError(
                "Dataset is empty"
            )

        dataset = df.copy()

        # ==========================================================
        # SCORE DE SIMILITUD
        # ==========================================================

        dataset["similarity_score"] = 0

        # Cargo (muy importante)

        dataset.loc[
            dataset["job_role"] == request.job_role,
            "similarity_score"
        ] += 50

        # Nivel

        dataset.loc[
            dataset["experience_level"] == request.experience_level,
            "similarity_score"
        ] += 20

        # Educación

        dataset.loc[
            dataset["education_required"] == request.education_required,
            "similarity_score"
        ] += 10

        # Industria

        dataset.loc[
            dataset["industry"] == request.industry,
            "similarity_score"
        ] += 10

        # Tamaño empresa

        dataset.loc[
            dataset["company_size"] == request.company_size,
            "similarity_score"
        ] += 5

        # Modalidad

        dataset.loc[
            dataset["work_mode"] == request.work_mode,
            "similarity_score"
        ] += 5

        # Experiencia (más flexible)

        dataset.loc[
            (
                dataset["experience_years"]
                .sub(request.experience_years)
                .abs()
                <= 1
            ),
            "similarity_score"
        ] += 5

        dataset.loc[
            (
                dataset["experience_years"]
                .sub(request.experience_years)
                .abs()
                <= 2
            )
            &
            (
                dataset["experience_years"]
                .sub(request.experience_years)
                .abs()
                > 1
            ),
            "similarity_score"
        ] += 3

        # ==========================================================
        # ELIMINAMOS PERFILES MUY DIFERENTES
        # ==========================================================

        dataset = dataset[
            dataset["similarity_score"] >= 50
        ]

        if dataset.empty:

            raise ValueError(
                "No se encontraron perfiles similares"
            )

        # ==========================================================
        # ORDENAMOS
        # ==========================================================

        dataset = dataset.sort_values(

            by=[
                "similarity_score",
                "skill_demand_score",
                "career_growth_score"
            ],

            ascending=False

        )

        # ==========================================================
        # TOP 50
        # ==========================================================

        dataset = dataset.head(50)

        return dataset.drop(
            columns=["similarity_score"]
        )