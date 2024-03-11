#!/usr/bin/node

const arg = process.argv[2];
let n = parseInt(arg);
let i = 0;
let a = 'X';
if (isNaN(n)){
    console.log('Missing size');
}
else{
    while (i < n){
	for (let a = 0; a < n; a++){
		console.log(a);
	    }
	i++;
    }
}
