#!/usr/bin/node

const { occurrences } = require('./101-data.js');

// Initialize a new dictionary to store user ids by occurrence
const usersByOccurrence = {};

// Iterate over the occurrences dictionary
for (const userId in occurrences) {
    const occurrence = occurrences[userId];
    
    // Check if the occurrence count is already present as a key in the usersByOccurrence dictionary
    if (usersByOccurrence[occurrence] === undefined) {
        // If not present, initialize an array with the current user id as the first element
        usersByOccurrence[occurrence] = [userId];
    } else {
        // If present, push the current user id to the array associated with the occurrence count
        usersByOccurrence[occurrence].push(userId);
    }
}

// Print the new dictionary
console.log(usersByOccurrence);
