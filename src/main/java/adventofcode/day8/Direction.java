package adventofcode.day8;

public enum Direction {
    row, column;

    public static Direction fromString(String string) {
        if (string.equals("row")) {
            return row;
        } else if (string.equals("column")) {
            return column;
        }
        throw new RuntimeException();
    }

}
