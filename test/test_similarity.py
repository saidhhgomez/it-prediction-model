import sys
from pathlib import Path

# 1. Detectar la raíz del proyecto y añadirla a las rutas de Python
root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

# 2. Ahora sí puedes importar de backend sin errores
from types import SimpleNamespace
import pandas as pd
from backend.services.similarity_service import SimilarityService


# ==========================================================
# DATASET
# ==========================================================

root_dir = Path(__file__).resolve().parents[1]

dataset_path = (
    root_dir
    / "datasets"
    / "ai_job_dataset.csv"
)

df = pd.read_csv(dataset_path)

service = SimilarityService()


# ==========================================================
# FUNCIÓN
# ==========================================================

def run_test(title, request):

    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)

    result = service.find_similar_profiles(
        df,
        request
    )

    print()

    print("Perfiles encontrados :",
          len(result))

    print()

    print("Promedios utilizados por el modelo")

    print("--------------------------------")

    print(
        "skill_demand_score :",
        round(
            result["skill_demand_score"].mean(),
            2
        )
    )

    print(
        "career_growth_score:",
        round(
            result["career_growth_score"].mean(),
            2
        )
    )

    print(
        "job_openings       :",
        round(
            result["job_openings"].mean(),
            2
        )
    )

    print(
        "job_security_score :",
        round(
            result["job_security_score"].mean(),
            2
        )
    )

    print(
        "automation_risk    :",
        round(
            result["automation_risk"].mean(),
            2
        )
    )

    print(
        "ai_adoption_score  :",
        round(
            result["ai_adoption_score"].mean(),
            2
        )
    )

    print()

    print("Primeros perfiles")

    print("-----------------")

    print(

        result[
            [
                "country",
                "job_role",
                "experience_level",
                "education_required",
                "industry",
                "company_size",
                "work_mode",
                "experience_years"
            ]
        ].head(10)

    )


# ==========================================================
# BAJA
# ==========================================================

request_low = SimpleNamespace(

    country="Brazil",

    job_role="Data Analyst",

    ai_specialization="Analytics",

    experience_level="Entry",

    experience_years=0,

    education_required="Diploma",

    industry="Retail",

    company_size="Small",

    work_mode="Onsite"

)

run_test(
    "PRUEBA BAJA",
    request_low
)


# ==========================================================
# MEDIA
# ==========================================================

request_medium = SimpleNamespace(

    country="Canada",

    job_role="Data Scientist",

    ai_specialization="LLM",

    experience_level="Mid",

    experience_years=3,

    education_required="Bachelor",

    industry="Tech",

    company_size="Medium",

    work_mode="Hybrid"

)

run_test(
    "PRUEBA MEDIA",
    request_medium
)


# ==========================================================
# ALTA
# ==========================================================

request_high = SimpleNamespace(

    country="USA",

    job_role="AI Engineer",

    ai_specialization="LLM",

    experience_level="Senior",

    experience_years=8,

    education_required="Master",

    industry="Tech",

    company_size="Enterprise",

    work_mode="Remote"

)

run_test(
    "PRUEBA ALTA",
    request_high
)