#!/usr/bin/node
/**
 * A script that prints all the characters of a Star Wars Movie.
 */
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    try {
      const fetchCharacterName = (characterUrl) => {
        return new Promise((resolve, reject) => {
          request.get(characterUrl, (error, response, body) => {
            if (!error && response.statusCode === 200) {
              resolve(JSON.parse(body).name);
            } else {
              reject(new Error('Character information request failed!'));
            }
          });
        });
      };
      for (const characterUrl of JSON.parse(body).characters) {
        console.log(await fetchCharacterName(characterUrl));
      }
    } catch (err) {
      console.log('Exception:', err);
    }
  } else {
    console.log('Movie information request failed!');
  }
});
