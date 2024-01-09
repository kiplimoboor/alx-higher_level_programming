#!/usr/bin/node

let list = require('./100-data').list;

list = list.map((el, index) => el * index);

console.log(list);
