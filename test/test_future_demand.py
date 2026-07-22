from pathlib import Path
import joblib
import pandas as pd

# ======================================================
# CARGAR MODELO
# ======================================================

root_dir = Path(__file__).resolve().parent.parent

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

model = joblib.load(model_path)
target_encoder = joblib.load(encoder_path)


# ======================================================
# FUNCIÓN DE PRUEBA
# ======================================================

def test_prediction(name, indicators):
    sample_df = pd.DataFrame([indicators])
    
    prediction = model.predict(sample_df)
    predicted_label = target_encoder.inverse_transform(prediction)[0]
    probabilities = model.predict_proba(sample_df)[0]

    all_labels = target_encoder.inverse_transform(model.classes_)
    
    probability_dict = {
        label: round(float(prob) * 100, 2)
        for label, prob in zip(all_labels, probabilities)
    }

    confidence = round(max(probabilities) * 100, 2)

    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)

    print("\nIndicadores:")
    for k, v in indicators.items():
        print(f"{k:25}: {v}")

    print("\nResultado:")
    print("Predicción :", predicted_label)
    print("Confianza  :", confidence)
    print("Probabilidades:")
    print(probability_dict)


# ======================================================
# EJECUCIÓN DE LAS PRUEBAS
# ======================================================
if __name__ == "__main__":
    
    # PRUEBA 1 (Debe salir BAJA)
    test_prediction(
        "PRUEBA 1 - BAJA",
        {
            "skill_demand_score": 18,
            "career_growth_score": 22,
            "job_openings": 8,
            "job_security_score": 35,
            "automation_risk": 88,
            "ai_adoption_score": 20
        }
    )

    # PRUEBA 2 (Debe salir MEDIA)
    test_prediction(
        "PRUEBA 2 - MEDIA",
        {
            "skill_demand_score": 42,
            "career_growth_score": 45,
            "job_openings": 40,
            "job_security_score": 62,
            "automation_risk": 50,
            "ai_adoption_score": 65
        }
    )

    # PRUEBA 3 (Debe salir ALTA)
    test_prediction(
        "PRUEBA 3 - ALTA",
        {
            "skill_demand_score": 82,
            "career_growth_score": 78,
            "job_openings": 65,
            "job_security_score": 84,
            "automation_risk": 18,
            "ai_adoption_score": 92
        }
    )