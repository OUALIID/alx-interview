#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2);
const url = `https://swapi-api.alx-tools.com/api/films/${id[0]}/`;
request(url, (err, response, body) => {
  if (err) {
    return;
  }
  const dates = JSON.parse(body).characters;
  dates.forEach(date => {
    request(date, (dateErr, dateResponse, dateBody) => {
      if (date) {
        console.log(JSON.parse(dateBody).name);
      }
    });
  });
});
