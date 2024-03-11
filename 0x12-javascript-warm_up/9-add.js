#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];
const n = parseInt(arg1);
const x = parseInt(arg2);
function add (a, b) {
  if (isNaN(a) || isNaN(a)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(x, n);
