#!/usr/bin/node

const n = process.argv[2];
const x = parseInt(n);
let i = 0;
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  while (i < x) {
	    console.log('C is fun');
	    i++;
  }
}
