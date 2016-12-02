var instructions = "L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1";
var instructionList = instructions.split(", ");

var direction = [0, 1];
var position = [0, 0];

for (var i=0; i< instructionList.length; i++) {
  var instruction = instructionList[i];
  direction = turn(direction, instruction);
  var displacement = parseInt(instruction.substring(1));
  position = updatePosition(position, direction, displacement);
}

console.log(abs(position[0]) + abs(position[1]));

function turn(dir, instruction) {
  if (instruction[0] === 'L') {
    return turnLeft(dir);
  }
  return turnRight(dir);
}

function turnLeft(dir) {
  return [-dir[1], dir[0]];
}

function turnRight(dir) {
  return turnLeft(turnLeft(turnLeft(dir)));
}

function updatePosition(position, dir, displacement) {
  return [position[0] + displacement * dir[0], position[1] + displacement * dir[1]];
}

function abs(number) {
  if (number < 0) {
    return -number;
  }
  return number;
}
