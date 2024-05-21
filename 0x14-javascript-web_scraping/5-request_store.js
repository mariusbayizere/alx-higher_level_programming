#!/usr/bin/node

// This script gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request.
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
