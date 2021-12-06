express = require("express");
require("dotenv").config();

const app = express();

const PORT = process.env.NODEPORT || 9000;

// TEMPLATE ENGINE AND VIEW AND STATIC
app.set("view engine", "pug");
app.set("views", "./view");
app.use(express.static("static"));

// ROUTE
app.use("/", require("./route"));

app.listen(PORT, () => {
  console.log(`server running on http://127.0.0.1:${PORT}`);
});
