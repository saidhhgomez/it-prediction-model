import os

from openai import OpenAI


class ChatGPTService:

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

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

        market_indicators,

        similar_profiles_found

    ):

        system_prompt = """
Eres un asesor profesional de carreras en Inteligencia Artificial.

Tu trabajo es interpretar resultados provenientes de un modelo de Machine Learning.

No inventes información.

No cambies valores numéricos.

Redacta un informe profesional, claro y amigable.

La respuesta debe contener:

1. Resumen del perfil del usuario.

2. Interpretación de la demanda futura.

3. Riesgo de automatización.

4. Crecimiento profesional esperado.

5. Proyección salarial.

6. Indicadores del mercado laboral.

7. Una recomendación personalizada.

8. Explica que las predicciones fueron obtenidas utilizando un modelo de Machine Learning entrenado con un dataset internacional de empleos relacionados con Inteligencia Artificial.

9. Explica que el análisis se realizó comparando perfiles similares encontrados en el dataset.

No utilices listas enormes.

Utiliza títulos y párrafos bien organizados.
"""

        user_prompt = f"""
Perfil del usuario

País: {request.country}

Cargo: {request.job_role}

Especialización IA: {request.ai_specialization}

Experiencia: {request.experience_level}

Años experiencia: {request.experience_years}

Educación: {request.education_required}

Industria: {request.industry}

Empresa: {request.company_size}

Modalidad: {request.work_mode}

Horas por semana: {request.weekly_hours}

Nivel de inglés: {request.idioma_ingles}

Github: {request.github_profile}

Nivel de programación: {request.programming_level}

Certificaciones: {request.certifications}


Resultados del modelo

Demanda futura:

{future_demand}

Riesgo automatización:

{automation_risk}

Crecimiento profesional:

{career_growth}

Proyección salarial:

{salary_projection}

Indicadores:

{market_indicators}

Perfiles similares encontrados:

{similar_profiles_found}
"""

        response = self.client.chat.completions.create(

            model="gpt-4.1-mini",

            temperature=0.4,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ]
        )

        return response.choices[0].message.content