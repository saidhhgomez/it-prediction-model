const express = require("express");

const router = express.Router();

/*
===========================================================
POST /predict
Endpoint temporal para verificar que el frontend envía
correctamente el formulario.
===========================================================
*/

router.post("/predict", (req, res) => {

    console.log("\n===============================================");
    console.log(" NUEVA PREDICCIÓN RECIBIDA ");
    console.log("===============================================\n");

    console.log(JSON.stringify(req.body, null, 2));

    console.log("\n===============================================\n");

    res.status(200).json({
        success: true,
        message: "Datos recibidos correctamente."
    });

});

module.exports = router;