#!/usr/bin/node

/*
 * StarWars API Counting Number of Movies Character Featured In
 */

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    return;
  }
  let count = 0;
  const films = JSON.parse(body).results;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
