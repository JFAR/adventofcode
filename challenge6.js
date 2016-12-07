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
  for(var i = 0;i < 636;i++) {
    side = []
    for(var j = 0; j < 3; j++) {
      side.push(parseLine(linesOfData[3*i + j]));
    }
    for(var j=0;j < 3;j++) {
      sides = [side[0][j],side[1][j],side[2][j]];
      if(isTriangle(sides)) {
        count++;
      }
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
