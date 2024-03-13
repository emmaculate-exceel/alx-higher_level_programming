#!/usr/bin/node

const dict = require('./101-data.js').dict;
const new_dict = Object.getOwnPropertyNames(dict);

for (let key in dict) {
	if (new_dict[dict[key]] == undefined) {
		new_dict[dict[key]] = [key];
	}
	else {
		new_dict[dict[key]].push[];
}

console.log(new_dict);
