import express from 'express';

const app = express();
app.use(express.json());

// Routes

app.get('/package', (req, res) => {

    const { name } = req.query;

    // Fetch the package
    try {
        
    } catch (err) {
        console.error('Error while fetching the package:', err);
        res.status(500).json({ message: 'Failed to fetch the package.' });
    }

});

// Listener
app.listen(3000, () => console.log('App running on http://localhost:3000'));