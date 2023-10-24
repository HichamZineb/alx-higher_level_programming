#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    function getIdFromUrl (url) {
      const regex = /\/(\d+)\/$/;
      const match = url.match(regex);
      return match ? match[1] : null;
    }

    charactersUrls.sort((a, b) => getIdFromUrl(a) - getIdFromUrl(b));

    charactersUrls.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
