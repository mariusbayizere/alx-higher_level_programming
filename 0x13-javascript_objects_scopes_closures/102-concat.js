#!/usr/bin/node
const fs = require('fs');

const pepq = fs.readFileSync(process.argv[2]).toString();
const qqxx = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], pepq + qqxx);
