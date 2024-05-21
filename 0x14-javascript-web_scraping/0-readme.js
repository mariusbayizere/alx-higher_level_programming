#!/usr/bin/node

// This script reads and prints the content of a file.
// The first argument is the file path.

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
