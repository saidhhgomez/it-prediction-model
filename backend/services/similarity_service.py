import pandas as pd


class SimilarityService:

    def find_similar_profiles(
        self,
        df: pd.DataFrame,
        request
    ):

        filtered = df[

            (df['job_role'] == request.job_role)

            &

            (df['experience_level']
             == request.experience_level)

            &

            (df['education_required']
             == request.education_required)

        ]

        if len(filtered) < 30:

            filtered = df[
                df['job_role']
                == request.job_role
            ]

        return filtered