const blockedModal = document.getElementById("blockedModal");

const remainingTime = document.getElementById("remainingTime");

const nextEvaluationDate = document.getElementById("nextEvaluationDate");

const historyBtn = document.getElementById("historyBtn");

const backHomeBtn = document.getElementById("backHomeBtn");

historyBtn.addEventListener("click", () => {

    window.location = "/history";

});

backHomeBtn.addEventListener("click", closeBlockedModal);

function closeBlockedModal(){

    if(blockedModal.classList.contains("closing")){
        return;
    }

    blockedModal.classList.add("closing");

    setTimeout(()=>{

        blockedModal.classList.remove("closing");
        blockedModal.classList.add("hidden");

    },250);

}

function formatRemainingHours(hours) {

    const totalMinutes = Math.ceil(hours * 60);

    const h = Math.floor(totalMinutes / 60);

    const m = totalMinutes % 60;

    if (h === 0) {

        return `${m} minutos`;

    }

    if (m === 0) {

        return `${h} horas`;

    }

    return `${h} horas ${m} minutos`;

}

function formatDate(dateString) {

    return new Date(dateString)

        .toLocaleString("es-PE", {

            dateStyle: "long",

            timeStyle: "short"

        });

}

function openBlockedModal(data){

    remainingTime.textContent =
        formatRemainingHours(data.remaining_hours);

    nextEvaluationDate.textContent =
        formatDate(data.next_evaluation);

    blockedModal.classList.remove("closing");
    blockedModal.classList.remove("hidden");

}

function getUserUUID() {

    const KEY = "ai_predict_uuid";
    const TIME_KEY = "ai_predict_uuid_time";

    const now = Date.now();

    const saved = localStorage.getItem(KEY);

    const savedTime = localStorage.getItem(TIME_KEY);

    const EXPIRATION = 12 * 60 * 60 * 1000;

    if (saved && savedTime && (now - Number(savedTime) < EXPIRATION)) {

        return saved;

    }

    const uuid = crypto.randomUUID();

    localStorage.setItem(KEY, uuid);
    localStorage.setItem(TIME_KEY, now.toString());

    return uuid;

}

const startBtn = document.getElementById("startEvaluationBtn");

startBtn.addEventListener("click", checkPredictionStatus);

async function checkPredictionStatus() {

    const uuid = getUserUUID();

    try {

        const response = await fetch(

            `/predict/can-predict/${uuid}`

        );

        const data = await response.json();

        console.log(response.status);

        console.log(data);

        if (data.can_predict) {

            window.location.href = "/predict";

            return;

        }

        openBlockedModal(data);

    }

    catch (error) {

        console.error(error);

        alert("No fue posible validar la evaluación.");

    }

}