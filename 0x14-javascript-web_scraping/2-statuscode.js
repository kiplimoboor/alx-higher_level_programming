#!/usr/bin/node

/*
 * Simple request to get status code
 */

request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    return;
  }
  console.log(`code: ${response && response.statusCode}`);
});
