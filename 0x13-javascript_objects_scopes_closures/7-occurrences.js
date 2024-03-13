#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let couter = 0;
    for (let element of list) {
	if (element === searchElement) {
	    counter++;
	}
    }
    return counter;
}
	    
