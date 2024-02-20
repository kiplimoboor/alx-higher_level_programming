#!/usr/bin/node

/*
 * Reads a file, and outputs its contents
 */

const fs = require('fs');
fs.readFile(process.argv[2].toString(), 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
