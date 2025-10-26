const express = require('express');
const app = express();
const path = require('path');

const PORT = 3000;

// Serve static files from "public" folder
app.use(express.static(path.join(__dirname, 'public')));

// Main route to send index.html
app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, function () {
  console.log(`Ares listening on port ${PORT}!!`);
});
