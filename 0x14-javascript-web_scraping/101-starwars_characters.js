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
    const characters = [];

    // Fetch characters and their appearance order in the movie
    charactersUrls.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const characterData = JSON.parse(charBody);
          characters.push({
            name: characterData.name,
            appearanceOrder: movieData.characters.indexOf(characterUrl)
          });

          // Check if all characters have been fetched
          if (characters.length === charactersUrls.length) {
            // Sort characters based on their appearance order
            characters.sort((a, b) => a.appearanceOrder - b.appearanceOrder);
            characters.forEach(character => {
              console.log(character.name);
            });
          }
        }
      });
    });
  }
});
