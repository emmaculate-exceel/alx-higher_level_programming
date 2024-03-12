#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && !isNaN(w) && w > 0 && !isNaN(w)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    for (let i = 0; i < this.height * 2; i++) {
      console.log('X'.repeat(this.width * 2));
    }
  }

  rotate () {
    for (let i = 0; i < this.width * 2; i++) {
      console.log('X'.repeat(this.height * 2));
    }
  }
}

module.exports = Rectangle;
