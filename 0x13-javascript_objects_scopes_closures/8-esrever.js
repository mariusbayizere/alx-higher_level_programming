#!/usr/bin/node
exports.esrever = function (list) {
  const xxx = [];
  for (const x of list) {
    xxx.unshift(x);
  }
  return xxx;
};
