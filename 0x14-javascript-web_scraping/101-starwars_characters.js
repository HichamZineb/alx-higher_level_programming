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
    let charactersCount = 0;

    charactersUrls.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
          charactersCount++;

          if (charactersCount === charactersUrls.length) {
            charactersUrls.sort((a, b) => a.localeCompare(b));
            charactersUrls.forEach(sortedCharacterUrl => {
              request(sortedCharacterUrl, (sortedCharError, sortedCharResponse, sortedCharBody) => {
                if (sortedCharError) {
                  console.error(sortedCharError);
                } else {
                  const sortedCharacterData = JSON.parse(sortedCharBody);
                  console.log(sortedCharacterData.name);
                }
              });
            });
          }
        }
      });
    });
  }
});
