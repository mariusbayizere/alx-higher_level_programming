#!/usr/bin/node
exports.esrever = function (list) {
  let air = list.length - 1;
  let x = 0;
  while ((air - x) > 0) {
    const ape = list[air];
    list[air] = list[x];
    list[x] = ape;
    air;
    air--;
  }
  return list;
};
