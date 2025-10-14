import express from 'express';
import GithubContentFetcher from 'github-raw-fetcher';
import getPackageMeta from './lib/getPackageMeta.ts';
import getPackages from './lib/getPackages.ts';

const app = express();
app.use(express.json());

// Routes

// Get packages (with options)
app.get('/all', async (req, res) => {

    const limitQ = req.query.limit as string | undefined;
    const skipQ = req.query.skip as string | undefined;
    const queryQ = req.query.q as string | undefined;
    const keywordsQ = req.query.keywords as string | undefined;

    const packages = await getPackages({
        limit: limitQ && parseInt(limitQ) < 30 ? parseInt(limitQ) : 30,
        skip: skipQ ? parseInt(skipQ) : 0,
        query: queryQ ? queryQ.trim().toLowerCase() : '',
        keywords: keywordsQ ? keywordsQ.split(',').filter(k => k).slice(0, 10) : []
    });

    res.status(200).json({
        message: 'Successfully fetched the packages.',
        packages
    });
});

// Get package code
app.get('/code', async (req, res) => {

    const name = req.query.name as string;

    if (!name) return res.status(400).json({ message: 'No name provided.' });

    // Fetch the package
    try {
        // Fetch meta
        const meta = await getPackageMeta(name);
        if (!meta) return res.status(500).json({ message: 'Failed to fetch the package.' });

        // Fetch code
        const fetcher = new GithubContentFetcher(meta.github.username, meta.github.repository); // Fetches from 'main' - latest version

        const code = fetcher.getRawContent(`modules/${name}/__init__.py`);

        res.status(200).json({
            message: 'Successfully got the package',
            name,
            version: meta.version,
            code
        });

    } catch (err) {
        console.error('Error while fetching the package:', err);
        res.status(500).json({ message: 'Failed to fetch the package.' });
    }
});

// Publish package
app.post('/publish', async (req, res) => {

    const { name, dependencies, githubUser, githubRepo }: Record<string, string> = req.body;

    // Dependencies: foo@1.0.0,bar@1.2.1,bazz@6.3.8

});

// Listener
const PORT = 8080;
app.listen(PORT, () => console.log(`App running on http://localhost:${PORT}`));