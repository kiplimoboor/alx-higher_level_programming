#!/usr/bin/node

/*
 * Get contents of a web page
 */

const request = require('request');
const url = process.argv[2];
const fs = require('fs');
const filename = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    return;
  }
  fs.writeFile(filename, body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
