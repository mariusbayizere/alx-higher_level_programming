#!/usr/bin/node

// This script displays the status code of a GET request.
// The first argument is the URL to request (GET).

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
