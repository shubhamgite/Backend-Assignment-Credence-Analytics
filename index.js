const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

mongoose.connect('mongodb://localhost:27017/bookdb', { useNewUrlParser: true, useUnifiedTopology: true });

const bookSchema = new mongoose.Schema({
    name: String,
    img: String,
    summary: String
});

const Book = mongoose.model('Book', bookSchema);

// CRUD Routes
app.post('/books', async (req, res) => {
    const book = new Book(req.body);
    await book.save();
    res.send(book);
});

app.get('/books', async (req, res) => {
    const books = await Book.find();
    res.send(books);
});

app.get('/books/:id', async (req, res) => {
    const book = await Book.findById(req.params.id);
    res.send(book);
});

app.put('/books/:id', async (req, res) => {
    const book = await Book.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.send(book);
});

app.delete('/books/:id', async (req, res) => {
    await Book.findByIdAndDelete(req.params.id);
    res.send({ message: 'Book deleted' });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
