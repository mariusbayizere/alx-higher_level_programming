#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      let s = '';
      for (let p = 0; p < this.width; p++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
