#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let couter = 0;
    for (searchElement of list) {
	if (searchElement == list[searchElement]) {
	    counter++;
	}
    }
    return counter;
}
	    
