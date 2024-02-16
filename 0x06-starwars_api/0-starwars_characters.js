#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, async (err, response, body) => {
  if (err) {
    return;
  }

  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    const characterData = await new Promise((resolve, reject) => {
      request(character, (err, response, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
    console.log(characterData);
  }
});
