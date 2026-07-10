/* ==========================================================
   AI CAREER PREDICTOR
   result.js
   Parte 1
========================================================== */

let prediction = null;

let predictionChart = null;

/* ==========================================================
   REFERENCIAS
========================================================== */

const title = document.getElementById("reportTitle");

const subtitle = document.getElementById("reportIntro");

const profileInfo = document.getElementById("profileInfo");

const kpiContainer = document.getElementById("kpiContainer");

const probabilityContainer = document.getElementById("probabilitiesContainer");

const chartCanvas = document.getElementById("predictionChart");

/* ==========================================================
   INICIO
========================================================== */

document.addEventListener("DOMContentLoaded", async () => {

    await loadPrediction();

    renderHeader();

    renderProfile();

    renderKPIs();

    renderProbabilityBars();

    renderChart();

    renderExecutiveSummary();

    renderCareerSummary();

    renderFutureDemand();

    renderAutomation();

    renderCareerGrowth();

    renderSalary();

    renderMarket();

    renderAdvices();

    renderModelInformation();

    renderDisclaimer();

});

/* ==========================================================
   HEADER
========================================================== */

function renderHeader() {

    title.innerText = prediction.feedback.title;

    subtitle.innerText = prediction.feedback.intro;

}

/* ==========================================================
   PERFIL
========================================================== */

function renderProfile() {

    const p = prediction.input_profile;

    profileInfo.innerHTML = `

        <div class="profile-grid">

            <div><strong>Nombre: </strong><span>${p.nombre_usuario}</span></div>

            <div><strong>País: </strong><span>${p.country}</span></div>

            <div><strong>Rol: </strong><span>${p.job_role}</span></div>

            <div><strong>Especialización: </strong><span>${p.ai_specialization}</span></div>

            <div><strong>Experiencia: </strong><span>${p.experience_years} años</span></div>

            <div><strong>Nivel: </strong><span>${p.experience_level}</span></div>

            <div><strong>Industria: </strong><span>${p.industry}</span></div>

            <div><strong>Empresa: </strong><span>${p.company_size}</span></div>

        </div>

    `;

}

/* ==========================================================
   KPIs
========================================================== */

function renderKPIs() {

    kpiContainer.innerHTML = `

        <div class="kpi-card">

            <h3>Demanda</h3>

            <span>${prediction.future_demand.level}</span>

        </div>

        <div class="kpi-card">

            <h3>Automatización</h3>

            <span>${prediction.automation_risk.score.toFixed(2)}%</span>

        </div>

        <div class="kpi-card">

            <h3>Crecimiento</h3>

            <span>${prediction.career_growth.score.toFixed(2)}%</span>

        </div>

        <div class="kpi-card">

            <h3>Salario</h3>

            <span>

                USD ${prediction.salary_projection.average_salary_usd.toLocaleString("en-US",
        {
            maximumFractionDigits: 0
        })}

            </span>

        </div>

    `;

}

/* ==========================================================
   PROBABILIDADES
========================================================== */

function renderProbabilityBars() {

    const probs = prediction.future_demand.probabilities;

    probabilityContainer.innerHTML = "";

    Object.entries(probs).forEach(([name, value]) => {

        probabilityContainer.innerHTML += `

            <div class="probability-item">

                <div class="probability-header">

                    <span>${name}</span>

                    <span>${value.toFixed(2)}%</span>

                </div>

                <div class="probability-bar">

                    <div
                        class="probability-fill"
                        style="width:${value}%">
                    </div>

                </div>

            </div>

        `;

    });

}

/* ==========================================================
   CHART
========================================================== */

function renderChart() {

    if (predictionChart) {

        predictionChart.destroy();

    }

    predictionChart = new Chart(chartCanvas, {

        type: "bar",

        data: {

            labels: [

                "Demanda",

                "Automatización",

                "Crecimiento",

                "Seguridad",

                "IA"

            ],

            datasets: [{

                label: "Score",

                data: [

                    prediction.future_demand.confidence,

                    prediction.automation_risk.score,

                    prediction.career_growth.score,

                    prediction.market_indicators.job_security_score,

                    prediction.market_indicators.ai_adoption_score

                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                y: {

                    beginAtZero: true,

                    max: 100

                }

            }

        }

    });

}

/* ==========================================================
   RESUMEN PROFESIONAL
========================================================== */

function renderCareerSummary() {

    document.getElementById("careerSummary").innerText =
        prediction.feedback.career_summary;

}

function renderExecutiveSummary() {

    document.getElementById("executiveSummary").innerHTML = `

        <p>${prediction.feedback.intro}</p>

    `;

}

/* ==========================================================
   DEMANDA FUTURA
========================================================== */

function renderFutureDemand() {

    document.getElementById("futureDemandDescription").innerText =
        prediction.feedback.future_demand.description;

    document.getElementById("futureDemandRecommendation").innerText =
        prediction.feedback.future_demand.recommendation;

}

/* ==========================================================
   AUTOMATIZACIÓN
========================================================== */

function renderAutomation() {

    document.getElementById("automationDescription").innerText =
        prediction.feedback.automation_risk.description;

    document.getElementById("automationRecommendation").innerText =
        prediction.feedback.automation_risk.recommendation;

}

/* ==========================================================
   CRECIMIENTO
========================================================== */

function renderCareerGrowth() {

    document.getElementById("growthDescription").innerText =
        prediction.feedback.career_growth.description;

    document.getElementById("growthRecommendation").innerText =
        prediction.feedback.career_growth.recommendation;

}

/* ==========================================================
   SALARIO
========================================================== */

function renderSalary() {

    document.getElementById("salaryDescription").innerText =
        prediction.feedback.salary_projection.description;

}

/* ==========================================================
   MERCADO
========================================================== */

function renderMarket() {

    const market = prediction.market_indicators;

    document.getElementById("skillDemand").innerText =
        market.skill_demand_score.toFixed(2) + "%";

    document.getElementById("jobOpenings").innerText =
        market.job_openings.toFixed(2) + "%";

    document.getElementById("jobSecurity").innerText =
        market.job_security_score.toFixed(2) + "%";

    document.getElementById("aiAdoption").innerText =
        market.ai_adoption_score.toFixed(2) + "%";

    document.getElementById("similarProfiles").innerText =
        prediction.similar_profiles_found;

    document.getElementById("marketDescription").innerText =
        prediction.feedback.market_analysis.description;

}

/* ==========================================================
   RECOMENDACIONES IA
========================================================== */

function renderAdvices() {

    document.getElementById("githubAdvice").innerText =
        prediction.feedback.github_advice;

    document.getElementById("englishAdvice").innerText =
        prediction.feedback.english_advice;

    document.getElementById("certificationAdvice").innerText =
        prediction.feedback.certification_advice;

}

/* ==========================================================
   MODELO
========================================================== */

function renderModelInformation() {

    const model = prediction.model_information;

    document.getElementById("accuracy").innerText =
        model.accuracy + "%";

    document.getElementById("precision").innerText =
        model.precision + "%";

    document.getElementById("recall").innerText =
        model.recall + "%";

    document.getElementById("f1Score").innerText =
        model.f1_score + "%";

    document.getElementById("modelDescription").innerText =
        prediction.feedback.model_information.description;

}

/* ==========================================================
   DISCLAIMER
========================================================== */

function renderDisclaimer() {

    document.getElementById("disclaimer").innerText =
        prediction.feedback.disclaimer;

}

/* ==========================================================
   BOTONES
========================================================== */

const historyBtn = document.getElementById("historyBtn");

const pdfBtn = document.getElementById("pdfBtn");

historyBtn.addEventListener("click", () => {

    window.location.href = "/history";

});

pdfBtn.addEventListener("click", exportPDF);

/* ==========================================================
   EXPORTAR PDF
========================================================== */

function exportPDF() {

    alert("La exportación en PDF será implementada en la siguiente fase.");

}

/* ==========================================================
   REFRESCAR GRÁFICO
========================================================== */

function destroyChart() {

    if (predictionChart) {

        predictionChart.destroy();

        predictionChart = null;

    }

}

/* ==========================================================
   CARGAR JSON DE PRUEBA
========================================================== */

async function loadPrediction() {

    try {

        const response = await fetch("/data/report.json");

        console.log(response);

        prediction = await response.json();

        console.log(prediction);

    } catch (error) {

        console.error(error);

    }

}