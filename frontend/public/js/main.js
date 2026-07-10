function getUserUUID(){

    const KEY="ai_predict_uuid";
    const TIME_KEY="ai_predict_uuid_time";

    const now=Date.now();

    const saved=localStorage.getItem(KEY);

    const savedTime=localStorage.getItem(TIME_KEY);

    const EXPIRATION=12*60*60*1000;

    if(saved && savedTime && (now-Number(savedTime)<EXPIRATION)){

        return saved;

    }

    const uuid=crypto.randomUUID();

    localStorage.setItem(KEY,uuid);
    localStorage.setItem(TIME_KEY,now.toString());

    return uuid;

}

const startBtn=document.getElementById("startEvaluationBtn");

startBtn.addEventListener("click",checkPredictionStatus);

async function checkPredictionStatus(){

    const uuid=getUserUUID();

    try{

        const response=await fetch(

            `/predict/can-predict/${uuid}`

        );

        const data=await response.json();

        if(data.can_predict){

            window.location.href="/predict";

            return;

        }

        openBlockedModal(data);

    }

    catch(error){

        console.error(error);

        alert("No fue posible validar la evaluación.");

    }

}