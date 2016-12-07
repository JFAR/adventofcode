var count = 0;

fs = require('fs');
fs.readFile('/Users/jafar/Documents/workspace/adventofcode/day5.data', 'utf8', function (error, data) {
  if(error) {
    return console.log(error);
  }
  main(data);
})

function main(data) {
  linesOfData = data.split('\n');
  linesOfData = cleanSegments(linesOfData);
  console.log(linesOfData[0]);
  console.log(linesOfData[1251647]);
  console.log(linesOfData[1908]);
  for(var i = 0;i < 1908;i++) {
    sides = parseLine(linesOfData[i]);
    if (isTriangle(sides)) {
      ++count;
    }
  }
  console.log(count);
}

function parseLine(line) {
  segments = line.split(" ");
  segments = cleanSegments(segments);
  return [parseInt(segments[0]), parseInt(segments[1]), parseInt(segments[2])];
}

function isTriangle(sides) {
  return (sides[0] + sides[1] > sides[2]) &&
         (sides[1] + sides[2] > sides[0]) &&
         (sides[2] + sides[0] > sides[1]);
}

function cleanSegments(segments) {
  output = []
  for (var i = 0;i < segments.length;i++) {
    if(segments[i].length > 0) {
      output.push(segments[i]);
    }
  }
  return output;
}
