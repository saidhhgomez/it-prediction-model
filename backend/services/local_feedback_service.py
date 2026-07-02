class LocalFeedbackService:
    
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

        github_advice = (
            "Excelente. Mantén tu portafolio de GitHub actualizado con proyectos relevantes."
            if request.github_profile
            else
            "Se recomienda crear un perfil de GitHub y publicar proyectos personales para fortalecer tu perfil profesional."
        )

        english_advice = (
            "Tu nivel de inglés representa una ventaja competitiva para acceder a oportunidades internacionales."
            if request.idioma_ingles == "Advanced"
            else
            "Fortalecer tu nivel de inglés incrementará significativamente tus oportunidades laborales en el sector tecnológico."
        )

        certification_advice = (
            "Continúa actualizando tus certificaciones para mantener un perfil competitivo."
            if request.certifications
            else
            "Obtener certificaciones reconocidas en Inteligencia Artificial o Ciencia de Datos fortalecerá tu perfil profesional."
        )

        automation_recommendation = (
            "Continúa especializándote en tecnologías emergentes para mantener una ventaja competitiva."
            if automation_risk["score"] >= 50
            else
            "El riesgo de automatización es relativamente controlado, aunque mantener una formación continua siempre será recomendable."
        )

        return {

            "title": "Informe Profesional de Predicción de Carrera",

            "intro": (
                "El asistente basado en Inteligencia Artificial no se encuentra disponible en este momento. "
                "Sin embargo, el análisis fue generado correctamente utilizando el modelo local de Machine Learning."
            ),

            "career_summary": (
                f"{request.job_role} es un perfil altamente relacionado con el desarrollo, análisis "
                f"e implementación de soluciones basadas en Inteligencia Artificial y Ciencia de Datos. "
                f"La especialización seleccionada corresponde a {request.ai_specialization}."
            ),

            "future_demand": {

                "title": "Demanda futura",

                "description": (
                    f"El modelo predice una demanda {future_demand['prediction']} "
                    f"con una confianza del {future_demand['confidence']:.2f}%."
                ),

                "recommendation": (
                    "Mantén una actualización constante de tus conocimientos para conservar tu competitividad."
                )

            },

            "automation_risk": {

                "title": "Riesgo de automatización",

                "description": (
                    f"El riesgo estimado es {automation_risk['level']} "
                    f"con un puntaje de {automation_risk['score']:.2f}%."
                ),

                "recommendation": automation_recommendation

            },

            "career_growth": {

                "title": "Crecimiento profesional",

                "description": (
                    f"El crecimiento esperado es {career_growth['level']} "
                    f"con un puntaje de {career_growth['score']:.2f}%."
                ),

                "recommendation": (
                    "La formación continua y la experiencia práctica incrementarán tus posibilidades de crecimiento."
                )

            },

            "salary_projection": {

                "title": "Proyección salarial",

                "description": (
                    f"El modelo clasifica la proyección salarial como "
                    f"{salary_projection['level']}. "
                    f"El salario promedio observado para perfiles similares fue de "
                    f"USD {salary_projection['average_salary_usd']:,.2f} anuales."
                )

            },

            "market_analysis": {

                "title": "Indicadores del mercado",

                "description": (
                    f"Se encontraron {similar_profiles_found} perfiles similares. "
                    f"La demanda de habilidades fue de {indicators['skill_demand_score']:.2f}%, "
                    f"la seguridad laboral alcanzó {indicators['job_security_score']:.2f}% "
                    f"y la adopción de Inteligencia Artificial fue de "
                    f"{indicators['ai_adoption_score']:.2f}%."
                )

            },

            "github_advice": github_advice,

            "english_advice": english_advice,

            "certification_advice": certification_advice,

            "model_information": {

                "title": "Información del modelo predictivo",

                "description": (
                    "Este resultado fue generado mediante un modelo de Machine Learning "
                    "entrenado con el dataset internacional "
                    "'Global AI and Data Jobs Salary Dataset'. "
                    "La predicción fue realizada comparando el perfil del usuario "
                    f"con {similar_profiles_found} perfiles similares encontrados en el dataset. "
                    "El modelo obtuvo un Accuracy de 98.21%, Precision de 98.21%, "
                    "Recall de 98.21% y F1 Score de 98.20%."
                )

            },

            "dataset": (
                "https://www.kaggle.com/datasets/"
                "mohankrishnathalla/global-ai-and-data-jobs-salary-dataset"
            ),

            "disclaimer": (
                "Este resultado corresponde a una predicción estadística obtenida mediante "
                "Machine Learning. Los resultados representan una estimación basada en datos "
                "históricos y perfiles similares, por lo que no constituyen una garantía "
                "absoluta sobre el comportamiento futuro del mercado laboral."
            )

        }