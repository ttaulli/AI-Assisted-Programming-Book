const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello, welcome to the Simple Web Server!');
});

app.get('/about', (req, res) => {
    res.send('This is a simple web server created with Express.');
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
