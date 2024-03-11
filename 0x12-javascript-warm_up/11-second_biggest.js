#!/usr/bin/node

const arg = process.argv;
let x = arg.map(Number).slice(2,process.argv.length).sort((a, b) => a - b);
if (x == 0){
    return (1);
}
else{
    console.log(x[x.length -2]);
}
