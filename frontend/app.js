const express = require("express");

const path = require("path");

const routes = require("./routes/web.js");
const apiRoutes = require("./routes/api.js");

const app = express();

const PORT = 3000;

app.use(express.static(path.join(__dirname, "public")));

app.use(express.json());

app.use(express.urlencoded({
    extended: true
}));

app.use("/", routes);
app.use("/", apiRoutes);

app.listen(PORT, () => {

    console.log(`Frontend running on http://localhost:${PORT}`);

});