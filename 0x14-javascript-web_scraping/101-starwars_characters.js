#!/usr/bin/node

// This script prints all characters of a Star Wars movie.
// The first argument is the Movie ID
// Display one character name per line in the same order of the list “characters” in the /films/ response
// The Star Wars API is used to fetch the characters
// The module 'request' is used to make the HTTP request.

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  // Function to fetch character names
  function fetchCharacterName (url) {
    return new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error(`Error: ${response.statusCode}`));
          return;
        }

        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  }

  // Fetch and print character names
  async function printCharacterNames () {
    for (const url of characterUrls) {
      try {
        const name = await fetchCharacterName(url);
        console.log(name);
      } catch (error) {
        console.error(error);
      }
    }
  }

  // Invoke the function to print character names
  printCharacterNames();
});
