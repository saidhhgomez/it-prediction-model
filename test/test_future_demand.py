import joblib
import pandas as pd

# ==========================
# CARGAR MODELO
# ==========================

model = joblib.load(
    r'D:\Universidad\Proyecto\Big Data\it_project\models\future_demand_final\future_demand_model.pkl'
)

target_encoder = joblib.load(
    r'D:\Universidad\Proyecto\Big Data\it_project\models\future_demand_final\future_demand_encoder.pkl'
)


# ==========================
# INDICADORES DE EJEMPLO
# ==========================

sample = {
    'skill_demand_score': 20,
    'career_growth_score': 25,
    'job_openings': 5,
    'job_security_score': 40,
    'automation_risk': 90,
    'ai_adoption_score': 20
}

# ==========================
# DATAFRAME
# ==========================

sample_df = pd.DataFrame([sample])

# ==========================
# PREDICCIÓN
# ==========================

prediction = model.predict(
    sample_df
)

predicted_label = (
    target_encoder
    .inverse_transform(prediction)[0]
)

# ==========================
# PROBABILIDADES
# ==========================

probabilities = model.predict_proba(
    sample_df
)[0]

classes = model.classes_

probability_dict = {}

for i, class_num in enumerate(classes):

    label_text = (
        target_encoder
        .inverse_transform([class_num])[0]
    )

    probability_dict[label_text] = round(
    float(probabilities[i]) * 100, 2
)

# ==========================
# CONFIANZA
# ==========================

confidence = round(
    float(max(probabilities)) * 100, 2
)

# ==========================
# RESPONSE
# ==========================

response = {

    "prediction": predicted_label,

    "confidence": confidence,

    "probabilities": probability_dict,

    "indicators": {

        "skill_demand_score":
            sample['skill_demand_score'],

        "career_growth_score":
            sample['career_growth_score'],

        "job_openings":
            sample['job_openings'],

        "job_security_score":
            sample['job_security_score'],

        "automation_risk":
            sample['automation_risk'],

        "ai_adoption_score":
            sample['ai_adoption_score']
    }
}

print(response)