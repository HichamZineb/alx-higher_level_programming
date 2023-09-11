#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const integers = process.argv.slice(2).map(arg => parseInt(arg));
  integers.sort((a, b) => b - a);
  console.log(integers[1]);
}
