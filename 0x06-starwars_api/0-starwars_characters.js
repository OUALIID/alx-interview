#!/usr/bin/node
const request = require('request');
const id = process.argv[2]; // Changed to directly access the first argument
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => {
    request(characterUrl, (characterErr, characterResponse, characterBody) => {
      if (characterErr) {
        console.error(characterErr);
        return;
      }
      console.log(JSON.parse(characterBody).name);
    });
  });
});
