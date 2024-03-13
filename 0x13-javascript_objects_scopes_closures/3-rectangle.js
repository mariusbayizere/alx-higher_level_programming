#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 0; y < this.height; y++) {
      let g = '';
      for (let p = 0; p < this.width; p++) {
        g += 'X';
      }
      console.log(g);
    }
  }
}

module.exports = Rectangle;
