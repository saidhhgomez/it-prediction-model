/*
=========================================================
ELEMENTOS
=========================================================
*/

const historyGrid = document.getElementById("historyContainer");

const totalEvaluations = document.getElementById("totalEvaluations");

const emptyState = document.getElementById("emptyState");

const loadingSection = document.getElementById("loadingSection");

const historySection = document.getElementById("historySection");

/*
=========================================================
UUID
=========================================================
*/

function getUserUUID() {

    const KEY = "ai_predict_uuid";

    return localStorage.getItem(KEY);

}

/*
=========================================================
FORMATEAR FECHA
=========================================================
*/

function formatDate(date) {

    return new Date(date).toLocaleString("es-PE", {

        dateStyle: "long",

        timeStyle: "short"

    });

}

/*
=========================================================
COLOR SEGÚN DEMANDA
=========================================================
*/

function demandClass(level) {

    switch (level) {

        case "Alta":

            return "badge-high";

        case "Media":

            return "badge-medium";

        default:

            return "badge-low";

    }

}

/*
=========================================================
CREAR CARD
=========================================================
*/

const template = document.getElementById("historyCardTemplate");

function createCard(item) {

    const clone = template.content.cloneNode(true);

    clone.querySelector(".country").textContent =
        item.profile.country;

    clone.querySelector(".role").textContent =
        item.profile.job_role;

    clone.querySelector(".specialization").textContent =
        item.profile.ai_specialization;

    clone.querySelector(".badge-demand").textContent =
        item.summary.future_demand;

    clone.querySelector(".badge-growth").textContent =
        "📈 " + item.summary.career_growth;

    clone.querySelector(".badge-risk").textContent =
        "🤖 " + item.summary.automation_risk;

    clone.querySelector(".badge-salary").textContent =
        "💰 " + item.summary.salary_level;

    clone.querySelector(".evaluation-date").textContent =
        formatDate(item.evaluation_date);

    clone.querySelector(".view-report")
        .addEventListener("click", () => {

            loadReport(item.id_resultado);

        });

    historyGrid.appendChild(clone);

}
/*
=========================================================
CARGAR REPORTE
=========================================================
*/

async function loadReport(idResultado) {

    try {

        const response = await fetch(`/result/${idResultado}`);

        const data = await response.json();

        sessionStorage.setItem(

            "predictionResult",

            JSON.stringify(data)

        );

        window.location.href = "/result";

    }

    catch (error) {

        console.error(error);

        alert("No fue posible abrir el informe.");

    }

}

/*
=========================================================
CARGAR HISTORIAL
=========================================================
*/

async function loadHistory() {

    const uuid = getUserUUID();

    if (!uuid) {

        emptyState.style.display = "block";

        return;

    }

    try {

        const response = await fetch(

            `/history/${uuid}`

        );

        const data = await response.json();

        console.log("RESPONSE:", response);
        console.log("DATA:", data);
        console.log("EVALUATIONS:", data.evaluations);

        totalEvaluations.textContent = data.total_evaluations;

        if (data.total_evaluations === 0) {

            emptyState.style.display = "block";

            return;

        }

        emptyState.style.display = "none";

        console.log("historyGrid:", historyGrid);

        historyGrid.innerHTML = "";

        data.evaluations.forEach(item => {
            console.log("ITEM:", item);
            createCard(item);
        });

        // ─── NUEVO: OCULTAR CARGANDO Y MOSTRAR HISTORIAL ───
        loadingSection.classList.add("hidden");
        historySection.classList.remove("hidden");

    }

    catch (error) {

        console.error(error);

        alert("No fue posible cargar el historial.");

    }

}

/*
=========================================================
INIT
=========================================================
*/

loadHistory();