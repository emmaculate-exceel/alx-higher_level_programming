#!/usr/bin/node

const dict = require('./101-data.js').dict;
const new_dict = {};

for (let key in new_dict) {
	new_dict[key] = dict[key];
}

console.log(new_dict);
