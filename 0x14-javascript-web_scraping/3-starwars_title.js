#!/usr/bin/node

/*
 * Prints No. Of Movies Where Wedge Antilles is present
 */

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    return;
  }
  const obj = JSON.parse(body);
  console.log(obj.title);
});
