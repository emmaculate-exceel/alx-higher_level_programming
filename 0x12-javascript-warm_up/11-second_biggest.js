#!/usr/bin/node

const arg = process.argv;
let x = arg.map(Number)
    .slice(2,process.argv.length)
    .sort((a, b) => a - b);
if (x <= 2){
    console.log('0');
}
if (x === 3){
    console.log('0');
}
else{
    console.log(x[x.length -2]);
}
