#!/usr/bin/node

const arg = process.argv[2];
const n = parseInt(arg);
let i = 0;
if (isNaN(n)) {
  console.log('Missing size');
} else {
  while (i < n) {
    console.log('X'.repeat(n));
    i++;
  }
}
