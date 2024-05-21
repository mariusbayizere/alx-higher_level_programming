#!/usr/bin/node

// This script prints the number of movies where the character “Wedge Antilles” is present.
// The first argument is the API URL of the Star Wars API.

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.filter(film => {
      return film.characters.some(character => {
        return character.includes(`/api/people/${wedgeAntillesId}/`);
      });
    }).length;
    console.log(count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
