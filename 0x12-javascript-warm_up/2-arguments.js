#!/usr/bin/node
const arg = process.argv.length;
if (arg == 2){
    console.log('No Argument');
}
else{
    console.log('Argument' + (arg > 3 ? 's': '') +' found');
}
//else{
//    console.log('No argument')}
