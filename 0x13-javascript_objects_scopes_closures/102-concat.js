#!/usr/bin/node

const fs = require('fs');

const inputFiles = [process.argv[2], process.argv[3]];
const outputFile = process.argv[4];

for (let i = 0; i < inputFiles.length; i++) {
  fs.readFile(inputFiles[i], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.appendFile(outputFile, data, err => {
      if (err) {
        console.log(err);
      }
    });
  });
}
