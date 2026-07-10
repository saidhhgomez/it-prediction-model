/* ==========================================================
   AI CAREER PREDICTOR
   predict.js (Versión Optimizada y Sincronizada)
========================================================== */

/* ==========================================================
   CONFIGURACIÓN Y ESTADO GLOBAL
========================================================== */
const TOTAL_QUESTIONS = 15;
let currentQuestion = 0;
let answers = {}; // Cambiado a let para permitir reinicio en restartBtn
let predictionChart = null;
let isAnimating = false;
let titleTypingInterval = null; // controla el efecto de tipeo del título

/* ==========================================================
   REFERENCIAS DOM
========================================================== */
const introCard = document.getElementById("introCard");
const questionContainer = document.getElementById("questionContainer");
const resultSection = document.getElementById("resultSection");
const loading = document.getElementById("loading");
const startBtn = document.getElementById("startBtn");
const backBtn = document.getElementById("backBtn");
const nextBtn = document.getElementById("nextBtn");
const restartBtn = document.getElementById("restartBtn");
const pdfBtn = document.getElementById("pdfBtn");
const questionTitle = document.getElementById("questionTitle");
const questionDescription = document.getElementById("questionDescription");
const answerContainer = document.getElementById("answerContainer");
const questionNumber = document.getElementById("questionNumber");
const progressFill = document.getElementById("progressFill");
const progressPercent = document.getElementById("progressPercent");
const kpiContainer = document.getElementById("kpiContainer");
const iaResponse = document.getElementById("iaResponse");

/* ==========================================================
   UUID DEL USUARIO (localStorage cada 12h)
========================================================== */
function getUserUUID() {
    const KEY = "ai_predict_uuid";
    const TIME_KEY = "ai_predict_uuid_time";

    const now = Date.now();
    const saved = localStorage.getItem(KEY);
    const savedTime = localStorage.getItem(TIME_KEY);
    const EXPIRATION = 12 * 60 * 60 * 1000; // 12 horas

    if (saved && savedTime && (now - Number(savedTime) < EXPIRATION)) {
        return saved;
    }

    const uuid = crypto.randomUUID();
    localStorage.setItem(KEY, uuid);
    localStorage.setItem(TIME_KEY, now.toString());
    return uuid;
}

const state = {
    uuid_usuario: getUserUUID()
};

/* ==========================================================
   MAPEO DE TRADUCCIÓN (UI Española → Dataset API Inglés)
========================================================== */
const mapValues = {
    country: {
        "Canadá": "Canada",
        "Estados Unidos": "USA",
        "Alemania": "Germany",
        "Francia": "France",
        "España": "Spain",
        "Japón": "Japan",
        "Australia": "Australia",
        "India": "India",
        "Brasil": "Brazil",
        "Singapur": "Singapore",
        "Países Bajos": "Netherlands",
        "Emiratos Árabes Unidos": "UAE"
    },

    education_required: {
        "Bachiller": "Bachelor",
        "Maestría": "Master",
        "Doctorado": "PhD",
        "Bootcamp": "Bootcamp",
        "Diplomado": "Diploma"
    },

    industry: {
        "Tecnología": "Tech",
        "Finanzas": "Finance",
        "Salud": "Healthcare",
        "Videojuegos": "Gaming",
        "Educación": "Education",
        "Retail": "Retail",
        "Consultoría": "Consulting",
        "Energía": "Energy",
        "Telecomunicaciones": "Telecom",
        "Automotriz": "Automotive"
    },

    company_size: {
        "Startup": "Startup",
        "Pequeña": "Small",
        "Mediana": "Medium",
        "Grande": "Large",
        "Corporación": "Enterprise"
    },

    work_mode: {
        "Remoto": "Remote",
        "Híbrido": "Hybrid",
        "Presencial": "Onsite"
    },

    idioma_ingles: {
        "Básico": "Basic",
        "Intermedio": "Intermediate",
        "Avanzado": "Advanced"
    }
};

/* ==========================================================
   DATASET DE PREGUNTAS (Estructura Original Intacta)
========================================================== */
const questions = [
    {
        id: "nombre_usuario",
        title: "¿Cómo te llamas?",
        description: "Escribe tu nombre para personalizar el análisis generado por Inteligencia Artificial.",
        type: "text"
    },
    {
        id: "country",
        title: "¿En qué país te visualizas trabajando?",
        description: "Imagina tu futuro profesional y selecciona el país donde te gustaría desarrollarte.",
        type: "card",
        options: ["Canadá", "Estados Unidos", "Alemania", "Francia", "España", "Japón", "Brasil", "India", "Australia", "Singapur", "Países Bajos", "Emiratos Árabes Unidos"]
    },
    {
        id: "job_role",
        title: "¿En qué rol te visualizas?",
        description: "Selecciona el rol profesional que te gustaría desempeñar en el futuro.",
        type: "card",
        options: ["Machine Learning Engineer", "AI Engineer", "Research Scientist", "Software Engineer AI", "Data Analyst", "Computer Vision Engineer", "NLP Engineer", "Data Scientist"]
    },
    {
        id: "ai_specialization",
        title: "¿En qué especialización de IA quieres enfocarte?",
        description: "Elige el área de inteligencia artificial que te gustaría dominar.",
        type: "card",
        options: ["LLM", "Reinforcement Learning", "Computer Vision", "NLP", "MLOps", "Generative AI", "Analytics", "Forecasting"]
    },
    {
        id: "experience_level",
        title: "¿Qué nivel de experiencia te visualizas alcanzando?",
        description: "Selecciona el nivel profesional que aspiras lograr.",
        type: "card",
        options: ["Entry", "Mid", "Senior", "Lead"]
    },
    {
        id: "experience_years",
        title: "¿Cuántos años de experiencia te visualizas teniendo?",
        description: "Selecciona el número de años de experiencia que te gustaría alcanzar en tu carrera.",
        type: "slider",
        options: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    },
    {
        id: "education_required",
        title: "¿Qué nivel de educación te gustaría alcanzar?",
        description: "Selecciona el nivel educativo que consideras ideal para tu futuro profesional.",
        type: "card",
        options: ["Bachiller", "Maestría", "Doctorado", "Bootcamp", "Diplomado"]
    },
    {
        id: "industry",
        title: "¿En qué industria te gustaría trabajar?",
        description: "Elige el sector donde te visualizas desarrollando tu carrera profesional.",
        type: "card",
        options: ["Tecnología", "Finanzas", "Salud", "Videojuegos", "Educación", "Retail", "Consultoría", "Energía", "Telecomunicaciones", "Automotriz"]
    },
    {
        id: "company_size",
        title: "¿En qué tipo de empresa te gustaría trabajar?",
        description: "Selecciona el tamaño de organización donde te visualizas trabajando.",
        type: "card",
        options: ["Startup", "Pequeña", "Mediana", "Grande", "Corporación"]
    },
    {
        id: "work_mode",
        title: "¿Cómo te gustaría trabajar?",
        description: "Selecciona el modo de trabajo ideal para tu estilo de vida.",
        type: "card",
        options: ["Remoto", "Híbrido", "Presencial"]
    },
    {
        id: "weekly_hours",
        title: "¿Cuántas horas semanales te gustaría trabajar?",
        description: "Selecciona una carga horaria aproximada ideal.",
        type: "slider",
        options: [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
    },
    {
        id: "idioma_ingles",
        title: "¿Cuál es tu nivel de inglés?",
        description: "Selecciona tu nivel actual de inglés.",
        type: "card",
        options: ["Básico", "Intermedio", "Avanzado"]
    },
    {
        id: "github_profile",
        title: "¿Tienes cuenta de GitHub?",
        description: "Indica si actualmente tienes un perfil en GitHub activo.",
        type: "boolean",
        options: ["Sí", "No"]
    },
    {
        id: "programming_level",
        title: "¿Cuál es tu nivel de programación actual?",
        description: "Evalúa tu nivel de habilidades en programación.",
        type: "card",
        options: ["Entry", "Mid", "Senior"]
    },
    {
        id: "certifications",
        title: "¿Cuentas con certificaciones profesionales?",
        description: "Indica si tienes certificaciones relacionadas a tu carrera.",
        type: "boolean",
        options: ["Sí", "No"]
    }
];

/* ==========================================================
   INICIALIZACIÓN Y EVENTOS
========================================================== */
document.addEventListener("DOMContentLoaded", () => {
    initEvents();
});

function initEvents() {
    startBtn.addEventListener("click", startFlow);
    nextBtn.addEventListener("click", handleNext);
    backBtn.addEventListener("click", handleBack);
    restartBtn.addEventListener("click", handleRestart);
    pdfBtn.addEventListener("click", exportPDF);
}

/* ==========================================================
   FLUJO DE NAVEGACIÓN Y COMPORTAMIENTO
========================================================== */
function startFlow() {
    introCard.classList.add("hidden");
    questionContainer.classList.remove("hidden");
    renderQuestionContent();

    // Entrada de la primera pregunta: usamos el mismo sistema de
    // animación (slide-in) que las transiciones entre preguntas,
    // en vez de una clase "fade" estática, para que solo exista
    // UN sistema de animación controlando la tarjeta.
    const card = document.querySelector(".question-card");
    if (card) {
        card.classList.add("slide-in");
        setTimeout(() => {
            card.classList.remove("slide-in");
        }, 300);
    }
}

function handleNext() {
    if (isAnimating) return;
    if (!validateAnswer()) return;

    if (currentQuestion < questions.length - 1) {
        currentQuestion++;
        transitionQuestion("next");
    } else {
        finishForm();
    }
}

function handleBack() {
    if (isAnimating) return;
    if (currentQuestion > 0) {
        currentQuestion--;
        transitionQuestion("back");
    }
}

function handleRestart() {
    currentQuestion = 0;
    answers = {};
    resultSection.classList.add("hidden");
    questionContainer.classList.remove("hidden");
    renderQuestionContent();
}

/* ==========================================================
   VALIDACIONES (Totalmente aislada de renders o reinicios visuales)
========================================================== */
function validateAnswer() {

    const q = questions[currentQuestion];

    let valid = true;

    if (q.type === "text") {

        const value = (answers[q.id] || "").trim();

        if (value.length < 2) {
            valid = false;
        }
    } else {
        if (answers[q.id] === undefined) {

            valid = false;

        }
    }
    if (!valid) {
        const card = document.querySelector(".question-card");
        if (card) {

            addClassTemporarily(card, "shake", 400);
        }
        return false;
    }
    return true;
}

/* ==========================================================
   ANIMACIÓN DE TRANSICIÓN (Sincronizada y sin doble render)
========================================================== */
function transitionQuestion(direction = "next") {
    const card = document.querySelector(".question-card");
    if (!card) {
        renderQuestionContent();
        return;
    }

    isAnimating = true;

    // Aplicar dirección de salida física
    card.classList.add(direction === "next" ? "slide-out-left" : "slide-out-right");

    setTimeout(() => {
        // Renderizar nuevo contenido estructural mientras la tarjeta está invisible
        renderQuestionContent();

        // Quitar clases de salida y añadir la de entrada fluida
        card.classList.remove("slide-out-left", "slide-out-right");
        card.classList.add("slide-in");

        setTimeout(() => {
            card.classList.remove("slide-in");
            isAnimating = false;
        }, 300);

    }, 200); // 200ms exactos alineados con la animación CSS de salida
}

/* ==========================================================
   RENDER DE CONTENIDO DE PREGUNTA
========================================================== */
function renderQuestionContent() {
    const q = questions[currentQuestion];

    // Actualizar Progreso Visual
    const progress = Math.round(((currentQuestion + 1) / questions.length) * 100);
    questionNumber.innerText = `Pregunta ${currentQuestion + 1} de ${questions.length}`;
    progressPercent.innerText = `${progress}%`;
    progressFill.style.width = `${progress}%`;

    // Título con efecto de tipeo (solo la pregunta, no la descripción)
    typeTitle(questionTitle, q.title, 22);
    questionDescription.innerText = q.description;
    answerContainer.innerHTML = "";

    // Renderizado según tipo de Input
    if (q.type === "text") renderText(q);
    if (q.type === "card") renderCards(q);
    if (q.type === "slider") renderSlider(q);
    if (q.type === "boolean") renderBoolean(q);

    // Estado del botón de retroceso
    backBtn.style.opacity = currentQuestion === 0 ? "0.3" : "1";
    backBtn.disabled = currentQuestion === 0;
}

/* ==========================================================
   RENDERIZADORES DE INPUTS (Cards, Sliders, Booleans)
========================================================== */
function renderCards(q) {
    q.options.forEach(option => {
        const card = document.createElement("div");
        card.classList.add("option-card");
        card.innerHTML = `<span>${option}</span>`;

        if (answers[q.id] === option) {
            card.classList.add("selected");
        }

        card.addEventListener("click", () => {
            selectOption(option, q.id, card);
        });

        answerContainer.appendChild(card);
    });
}

function renderBoolean(q) {
    const wrapper = document.createElement("div");
    wrapper.classList.add("boolean-wrapper");

    q.options.forEach(option => {
        const btn = document.createElement("button");
        btn.classList.add("boolean-btn");
        btn.innerText = option;

        if (answers[q.id] === option) {
            btn.classList.add("selected");
        }

        btn.addEventListener("click", () => {
            answers[q.id] = option;
            wrapper.querySelectorAll("button").forEach(b => b.classList.remove("selected"));
            btn.classList.add("selected");
        });

        wrapper.appendChild(btn);
    });

    answerContainer.appendChild(wrapper);
}

function renderSlider(q) {
    const wrapper = document.createElement("div");
    wrapper.classList.add("slider-wrapper");

    const min = Math.min(...q.options);
    const max = Math.max(...q.options);

    const input = document.createElement("input");
    input.type = "range";
    input.min = min;
    input.max = max;
    input.value = answers[q.id] ?? min;

    // Guardar el valor inicial por defecto de forma automática
    if (answers[q.id] === undefined) {
        answers[q.id] = parseInt(input.value);
    }

    const valueDisplay = document.createElement("div");
    valueDisplay.classList.add("slider-value");
    valueDisplay.innerText = input.value;

    input.addEventListener("input", () => {
        valueDisplay.innerText = input.value;
        answers[q.id] = parseInt(input.value);
    });

    wrapper.appendChild(input);
    wrapper.appendChild(valueDisplay);
    answerContainer.appendChild(wrapper);
}

function renderText(q) {

    const wrapper = document.createElement("div");
    wrapper.classList.add("text-wrapper");

    const input = document.createElement("input");

    input.type = "text";
    input.classList.add("text-input");

    input.placeholder = "Escribe tu nombre...";

    input.maxLength = 80;

    input.autocomplete = "name";

    input.value = answers[q.id] || "";

    input.focus();

    input.addEventListener("input", () => {
        input.value = input.value
            .replace(/[^A-Za-zÁÉÍÓÚáéíóúÑñ ]/g, "")
            .replace(/\s{2,}/g, " ");
        answers[q.id] = input.value.trimStart();
    });

    wrapper.appendChild(input);

    answerContainer.appendChild(wrapper);

}

function selectOption(value, qId, element) {
    answers[qId] = value;
    document.querySelectorAll(".option-card").forEach(el => el.classList.remove("selected"));
    element.classList.add("selected");
    addClassTemporarily(element, "pulse", 250);
}

/* ==========================================================
   FINALIZACIÓN DEL FORMULARIO Y PROCESAMIENTO
========================================================== */
async function finishForm() {
    loading.classList.remove("hidden");
    progressFill.style.width = "100%";
    progressPercent.innerText = "100%";
    nextBtn.disabled = true;
    backBtn.disabled = true;
    restartBtn.disabled = true;
    const payload = buildPayload();
    console.log("ENVIANDO PAYLOAD:");
    console.log(payload);
    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });
        if (!response.ok) {
            throw new Error("El servidor respondió con un error.");
        }
        const result = await response.json();
        console.log("RESPUESTA DEL SERVIDOR:");
        console.log(result);
        loading.classList.add("hidden");
        showResults(payload);
    } catch (error) {
        console.error(error);
        loading.classList.add("hidden");
        nextBtn.disabled = false;
        backBtn.disabled = false;
        restartBtn.disabled = false;
        alert("No fue posible conectar con el servidor.");
    }
}

function showResults(payload) {
    questionContainer.classList.add("hidden");
    resultSection.classList.remove("hidden");

    // KPIs Estáticos de Interfaz
    kpiContainer.innerHTML = `
        <div class="kpi-card">🎯 Fit IA: 87%</div>
        <div class="kpi-card">📈 Demanda: Alta</div>
        <div class="kpi-card">💰 Salario: Premium</div>
    `;

    // Configuración Segura de Chart.js
    if (predictionChart) predictionChart.destroy();

    const ctx = document.getElementById("predictionChart");
    predictionChart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["AI Fit", "Market Demand", "Salary Potential"],
            datasets: [{
                label: "Score",
                data: [87, 79, 92],
                backgroundColor: "#f38c2c"
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });

    // Respuesta IA con Efecto de Máquina de Escribir
    const message = `Tu perfil tiene una alta proyección en el mercado de Inteligencia Artificial.

Se observa una fuerte compatibilidad con roles avanzados como Machine Learning Engineer y AI Research Scientist.

El mercado actual muestra una creciente demanda en tu especialización, especialmente en LLMs y Generative AI.`;

    typeText(iaResponse, message, 15);
}

/* ==========================================================
   UTILIDADES DE TEXTO Y ANIMACIONES COMPLEMENTARIAS
========================================================== */
function typeText(element, text, speed = 18) {
    element.innerHTML = "";
    let i = 0;
    const interval = setInterval(() => {
        element.innerHTML += text.charAt(i);
        i++;
        if (i >= text.length) {
            clearInterval(interval);
        }
    }, speed);
}

/* Efecto de tipeo dedicado al título de la pregunta.
   Cancela cualquier tipeo anterior en curso para que, si el usuario
   avanza/retrocede rápido entre preguntas, el texto no se mezcle.

   IMPORTANTE: se acumula el texto en la variable "current" (JS) y solo
   se escribe con textContent. Antes se hacía element.innerText += char,
   lo cual leía innerText del DOM en cada letra; innerText devuelve el
   texto ya "renderizado" y el navegador colapsa/recorta espacios en esas
   lecturas intermedias, por eso las palabras terminaban pegadas y, al no
   quedar espacios, el texto no tenía dónde saltar de línea y se salía
   de la tarjeta. textContent no tiene ese problema: es texto crudo. */
function typeTitle(element, text, speed = 22) {
    if (titleTypingInterval) {
        clearInterval(titleTypingInterval);
        titleTypingInterval = null;
    }

    element.textContent = "";
    let i = 0;
    let current = "";
    titleTypingInterval = setInterval(() => {
        current += text.charAt(i);
        element.textContent = current;
        i++;
        if (i >= text.length) {
            clearInterval(titleTypingInterval);
            titleTypingInterval = null;
        }
    }, speed);
}

function addClassTemporarily(el, className, time = 300) {
    el.classList.add(className);
    setTimeout(() => {
        el.classList.remove(className);
    }, time);
}

function exportPDF() {
    alert("PDF export ready (conectar jsPDF aquí)");
}

/* ==========================================================
   CONSTRUCCIÓN DEL PAYLOAD TRADUCIDO EN INGLÉS PARA TU API
========================================================== */
function buildPayload() {
    return {
        uuid_usuario: state.uuid_usuario,
        nombre_usuario: answers.nombre_usuario,
        country: mapValues.country[answers.country] || answers.country,
        job_role: answers.job_role,
        ai_specialization: answers.ai_specialization,
        experience_level: answers.experience_level,
        experience_years: answers.experience_years,
        education_required: mapValues.education_required[answers.education_required] || answers.education_required,
        industry: mapValues.industry[answers.industry] || answers.industry,
        company_size: mapValues.company_size[answers.company_size] || answers.company_size,
        work_mode: mapValues.work_mode[answers.work_mode] || answers.work_mode,
        weekly_hours: answers.weekly_hours,
        idioma_ingles: mapValues.idioma_ingles[answers.idioma_ingles] || answers.idioma_ingles,
        github_profile: answers.github_profile === "Sí",
        programming_level: answers.programming_level,
        certifications: answers.certifications === "Sí"
    };
}