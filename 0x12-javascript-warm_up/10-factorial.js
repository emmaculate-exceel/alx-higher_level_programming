#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg);
function myfunc (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n < 0) {
    return 0;
  } else {
    return (n * myfunc(n - 1));
  }
}
console.log(myfunc(x));
