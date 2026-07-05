const express = require("express");
const path = require("path");
const router = express.Router();

router.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "../public/index.html"));
});

router.get("/predict", (req, res) => {
    res.sendFile(path.join(__dirname, "../public/predict.html"));
});

router.get("/history", (req, res) => {
    res.sendFile(path.join(__dirname, "../public/history.html"));
});

module.exports = router;