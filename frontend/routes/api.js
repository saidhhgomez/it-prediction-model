const express = require("express");
const axios = require("axios");

const router = express.Router();

/*
===========================================================
CONFIGURACIÓN
===========================================================
*/

const FASTAPI_URL = "http://127.0.0.1:8000";

/*
===========================================================
GET /predict/can-predict
Valida si el usuario puede realizar una evaluación.
===========================================================
*/

router.get("/predict/can-predict/:uuid", async (req, res) => {

    try {

        const { uuid } = req.params;

        const response = await axios.get(
            `${FASTAPI_URL}/predict/can-predict`,
            {
                params: {
                    uuid_usuario: uuid
                }
            }
        );

        return res.status(response.status).json(response.data);

    }

    catch (error) {

        if (error.response) {

            return res
                .status(error.response.status)
                .json(error.response.data);

        }

        return res.status(500).json({

            success: false,
            message: "No fue posible comunicarse con FastAPI."

        });

    }

});

/*
===========================================================
POST /predict
Recibe la petición del Frontend y la reenvía a FastAPI.
===========================================================
*/

router.post("/predict", async (req, res) => {

    try {

        console.log("\n===============================================");
        console.log(" PETICIÓN RECIBIDA DESDE EL FRONTEND ");
        console.log("===============================================\n");

        console.log(req.body);

        console.log("\n===============================================");
        console.log(" ENVIANDO PETICIÓN A FASTAPI ");
        console.log("===============================================\n");

        const response = await axios.post(

            `${FASTAPI_URL}/predict`,

            req.body,

            {

                headers: {

                    "Content-Type": "application/json"

                }

            }

        );

        console.log("\n===============================================");
        console.log(" RESPUESTA RECIBIDA DESDE FASTAPI ");
        console.log("===============================================\n");

        console.log(response.data);

        /*
        Se devuelve exactamente la respuesta de FastAPI
        al frontend.
        */

        return res.status(response.status).json(response.data);

    }

    catch (error) {

        console.log("\n===============================================");
        console.log(" ERROR AL CONECTAR CON FASTAPI ");
        console.log("===============================================\n");

        if (error.response) {

            console.error(error.response.data);

            return res.status(error.response.status).json(error.response.data);

        }

        console.error(error.message);

        return res.status(500).json({

            detail: "No fue posible comunicarse con FastAPI.",

            error: error.message

        });

    }

});

module.exports = router;