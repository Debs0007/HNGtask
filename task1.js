const express = require("express");

const PORT = process.env.PORT || 3500;
const app = express();

app.get("/", (req, res) => {
  const data = {
    slackUsername: "Debs",
    backend: true,
    age: 22,
    bio: "My name is Abdulhamid Lawal, i'm a beginner in backend development with little knowledge on python and i hope in gaining tremendous knowledge from HNG9 internship.",
  };
  res.json(data);
});

app.listen(PORT, () => {
  console.log("server running on " + PORT);
});
