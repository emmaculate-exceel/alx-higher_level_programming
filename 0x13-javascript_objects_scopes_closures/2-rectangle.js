#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && !isNaN(w) && w > 0 && !isNaN(w)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
