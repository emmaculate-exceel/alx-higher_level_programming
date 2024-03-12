#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof h > 0 && !isNaN(w) && typeof w > 0 && !isNaN(w)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
