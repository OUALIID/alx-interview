#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Failed to fetch movie information:', error || response.statusCode);
    return;
  }

  const characters = JSON.parse(body).characters;

  characters.forEach(characterUrl => {
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError || charResponse.statusCode !== 200) {
        console.error('Failed to fetch character information:', charError || charResponse.statusCode);
        return;
      }

      console.log(JSON.parse(charBody).name);
    });
  });
});
