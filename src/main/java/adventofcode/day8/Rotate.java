package adventofcode.day8;

public class Rotate implements Instruction {

    private Direction direction;
    private Integer xory;
    private Integer distance;

    public Rotate(String[] commandParts) {
        direction = Direction.fromString(commandParts[1]);
        xory = Integer.valueOf(commandParts[2].split("=")[1]);
        distance = Integer.valueOf(commandParts[4]);
    }

    @Override
    public void transformScreen(Screen previousScreen) {
        if (direction.equals(Direction.row)) {
            previousScreen.rotateRow(xory, distance);
        } else {
            previousScreen.rotateColumn(xory, distance);
        }
    }

}
