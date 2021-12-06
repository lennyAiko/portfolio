const url = require("url");
const express = require("express");
const router = express.Router();
const needle = require("needle");
const apicache = require("apicache");

// Init cache
let cache = apicache.middleware;

router.get("/", cache("5 minutes"), async (req, res, next) => {
  const ApiRes = await needle("get", `${process.env.APILINK}`);
  const data = ApiRes.body;

  console.log(data);
});

module.exports = router;
