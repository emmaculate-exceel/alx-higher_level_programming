#!/usr/bin/node

const { occurrences } = require('./101-data.js');

// Compute the dictionary of user ids by occurrence
const usersByOccurrence = Object.entries(occurrences).reduce((acc, [userId, occurrence]) => {
    acc[occurrence] = acc[occurrence] || [];
    acc[occurrence].push(userId);
    return acc;
}, {});

// Print the new dictionary
console.log(usersByOccurrence);
