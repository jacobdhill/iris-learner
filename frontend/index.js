const express = require("express");
const app = express();

app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  const p = 80;
  const c = "iris setosa";
  const d =
    "Variable in stature, Iris setosa (Bristle-Pointed Iris) is a rhizomatous perennial forming a clump of stiff, narrow, sword-like, mid-green leaves, 1-2 ft. long (30-60 cm), with a prominent midrib and a purplish tinged base. The foliage arises from shallowly rooted, large, branching rhizomes forming clumps.";

  res.render("index", { percentage: p, classification: c, description: d });
});

app.post("/", (req, res) => {
  console.log(req.body);
  res.redirect("/");
});

app.listen(80);
