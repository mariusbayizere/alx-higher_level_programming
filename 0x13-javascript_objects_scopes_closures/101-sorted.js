#!/usr/bin/node
const dict = require('./101-data').dict;

const jackson = Object.entries(dict);
const pain1 = Object.values(dict);
const bisuma = [...new Set(pain1)];
const newDict = {};
for (const y in bisuma) {
  const list = [];
  for (const x in jackson) {
    if (jackson[x][1] === bisuma[j]) {
      list.unshift(jackson[x][0]);
    }
  }
  newDict[bisuma[y]] = list;
}
console.log(newDict);
