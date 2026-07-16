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

        # =====================================================
        # NIVEL 1
        # Coincidencia más específica
        # =====================================================

        filtered = df[

            (df["job_role"] == request.job_role)

            &

            (df["experience_level"] == request.experience_level)

            &

            (df["education_required"] == request.education_required)

            &

            (df["industry"] == request.industry)

            &

            (df["company_size"] == request.company_size)

        ]

        # =====================================================
        # NIVEL 2
        # Relajamos company_size
        # =====================================================

        if len(filtered) < 30:

            filtered = df[

                (df["job_role"] == request.job_role)

                &

                (df["experience_level"] == request.experience_level)

                &

                (df["education_required"] == request.education_required)

                &

                (df["industry"] == request.industry)

            ]

        # =====================================================
        # NIVEL 3
        # Relajamos industry
        # =====================================================

        if len(filtered) < 30:

            filtered = df[

                (df["job_role"] == request.job_role)

                &

                (df["experience_level"] == request.experience_level)

                &

                (df["education_required"] == request.education_required)

            ]

        # =====================================================
        # NIVEL 4
        # Sólo cargo
        # =====================================================

        if len(filtered) < 30:

            filtered = df[

                df["job_role"] == request.job_role

            ]

        if filtered.empty:

            raise ValueError(
                "No se encontraron perfiles similares"
            )

        return filtered