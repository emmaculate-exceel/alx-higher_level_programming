#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && !isNaN(w) && w > 0 && !isNaN(w)) {
      this.width = w;
      this.height = h;
    }
  }
      Print () {
	  for (let i = 0; i < this.height; i++) {
	      console.log('X'.repeat(this.width);
    }
  }
}

module.exports = Rectangle;
