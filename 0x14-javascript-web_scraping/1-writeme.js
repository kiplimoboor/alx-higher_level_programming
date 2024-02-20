#!/usr/bin/node

/*
 * Writes text to a file
 */

const fs = require('fs');
fs.writeFile(process.argv[2].toString(), process.argv[3], err => {
  if (err) {
    console.log(err);
  }
});
