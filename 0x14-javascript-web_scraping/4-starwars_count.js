#!/usr/bin/node

/*
 * StarWars API Counting Number of Movies Character Featured In
 */

const request = require('request');
const url = process.argv[2];
const charId = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, (error, response, body) => {
  if (error) {
    return;
  }
  let count = 0;
  const films = JSON.parse(body).results;
  for (const film of films) {
    if (film.characters.includes(charId)) {
      count++;
    }
  }
  console.log(count);
});
