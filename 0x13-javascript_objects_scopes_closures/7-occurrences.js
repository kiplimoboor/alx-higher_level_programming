#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;

  for (const el of list) {
    if (el === searchElement) {
      occur++;
    }
  }

  return occur;
};
