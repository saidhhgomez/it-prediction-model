import json
import os

from openai import OpenAI


class ChatGPTService:

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")
        
        print(api_key[:10])

        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY no configurada."
            )

        self.client = OpenAI(
            api_key=api_key
        )

    def generate_feedback(

        self,

        request,

        future_demand,

        automation_risk,

        career_growth,

        salary_projection,

        indicators,

        similar_profiles_found

    ):

        system_prompt = """
Eres un asesor profesional especializado en carreras de Inteligencia Artificial.

IMPORTANTE

Nunca inventes información.

Nunca modifiques números.

Nunca cambies porcentajes.

Nunca contradigas los resultados del modelo de Machine Learning.

Tu trabajo consiste únicamente en interpretar los resultados y explicarlos al usuario.

La respuesta DEBE SER ÚNICAMENTE un objeto JSON válido.

No escribas markdown.

No escribas ```json.

No escribas texto antes ni después del JSON.

La estructura debe ser exactamente la siguiente:

{
  "title":"",
  "intro":"",
  "career_summary":"",
  "future_demand":{
      "title":"",
      "description":"",
      "recommendation":""
  },
  "automation_risk":{
      "title":"",
      "description":"",
      "recommendation":""
  },
  "career_growth":{
      "title":"",
      "description":"",
      "recommendation":""
  },
  "salary_projection":{
      "title":"",
      "description":""
  },
  "market_analysis":{
      "title":"",
      "description":""
  },
  "github_advice":"",
  "english_advice":"",
  "certification_advice":"",
  "model_information":{
      "title":"",
      "description":""
  },
  "dataset":"",
  "disclaimer":""
}

No agregues campos adicionales.
"""

        user_prompt = f"""
INFORMACIÓN DEL PERFIL

País:
{request.country}

Cargo:
{request.job_role}

Especialización:
{request.ai_specialization}

Experiencia:
{request.experience_level}

Años de experiencia:
{request.experience_years}

Educación:
{request.education_required}

Industria:
{request.industry}

Empresa:
{request.company_size}

Modalidad:
{request.work_mode}

Horas semanales:
{request.weekly_hours}

Nivel de inglés:
{request.idioma_ingles}

Github:
{"Sí" if request.github_profile else "No"}

Nivel de programación:
{request.programming_level}

Certificaciones:
{"Sí" if request.certifications else "No"}


RESULTADOS DEL MODELO

Demanda futura:
{future_demand["prediction"]}

Confianza:
{future_demand["confidence"]:.2f}%

Probabilidad Alta:
{future_demand["probabilities"]["Alta"]:.2f}%

Probabilidad Media:
{future_demand["probabilities"]["Media"]:.2f}%

Probabilidad Baja:
{future_demand["probabilities"]["Baja"]:.2f}%


Riesgo de automatización:
{automation_risk["level"]}

Puntaje:
{automation_risk["score"]:.2f}%


Crecimiento profesional:
{career_growth["level"]}

Puntaje:
{career_growth["score"]:.2f}%


Nivel salarial:
{salary_projection["level"]}

Salario promedio:
USD {salary_projection["average_salary_usd"]:,.2f}


Indicadores del mercado

Demanda de habilidades:
{indicators["skill_demand_score"]:.2f}

Seguridad laboral:
{indicators["job_security_score"]:.2f}

Adopción de IA:
{indicators["ai_adoption_score"]:.2f}

Ofertas laborales:
{indicators["job_openings"]:.2f}


Perfiles similares encontrados:
{similar_profiles_found}


INFORMACIÓN DEL MODELO

Accuracy:
98.21%

Precision:
98.21%

Recall:
98.21%

F1 Score:
98.20%

Dataset:
Global AI and Data Jobs Salary Dataset (Kaggle)

El análisis fue realizado comparando el perfil del usuario con perfiles similares encontrados en dicho dataset.

Recomendaciones:

- Explica brevemente qué hace la profesión elegida.
- Explica los resultados obtenidos.
- Si el usuario no tiene GitHub, recomienda crear uno.
- Si el nivel de inglés es bajo o intermedio, incentiva a mejorarlo.
- Si no posee certificaciones, recomienda obtenerlas.
- Da consejos relacionados con la especialización seleccionada.
- Mantén un tono profesional y cercano.
"""

        response = self.client.chat.completions.create(

            model="gpt-4.1-mini",

            temperature=0.35,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ],

            response_format={
                "type": "json_object"
            }

        )

        return json.loads(
            response.choices[0].message.content
        )