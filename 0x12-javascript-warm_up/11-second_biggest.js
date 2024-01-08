#!/usr/bin/node

const num = process.argv.slice(2).sort((a, b) => b - a)[1];

console.log(num || 0);
