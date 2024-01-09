#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const prop in dict) {
  if (newDict[dict[prop]]) {
    newDict[dict[prop]].push(prop);
  } else {
    newDict[dict[prop]] = [prop];
  }
}

console.log(newDict);
