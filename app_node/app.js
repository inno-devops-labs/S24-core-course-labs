const express = require('express');
const axios = require('axios');
const path = require('path');


const app = express();
const PORT = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'public/views'));

app.use(express.static('public'));

app.get('/', async (req, res) => {
    try {
        const pokemonData = await getRandomPokemon();
        res.render('index', { pokemonData });
    } catch (error) {
        console.error('Error fetching Pokemon data:', error.message);
        res.status(500).send('Internal Server Error');
    }
});

async function getRandomPokemon() {
    const randomPokemonId = Math.floor(Math.random() * 898) + 1;
    const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${randomPokemonId}`);
    return response.data;
}

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
