const { default: axios } = require("axios");
const express = require("express");
const app = express();

app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("index");
});

app.post("/", (req, res) => {
  const { sepal_length, sepal_width, petal_length, petal_width } = req.body;

  //console.log({ sepal_length, sepal_width, petal_length, petal_width });

  axios
    .post("http://backend:5000/", {
      sepal_length: sepal_length,
      sepal_width: sepal_width,
      petal_length: petal_length,
      petal_width: petal_width,
    })
    .then((response) =>
      res.render("index-pred", {
        prediction: response.data.prediction,
        accuracy: response.data.accuracy,
        description: response.data.description,
        sepal_length: sepal_length,
        sepal_width: sepal_width,
        petal_length: petal_length,
        petal_width: petal_width,
      })
    )
    .catch((error) => console.error(error));
});

app.listen(80);
