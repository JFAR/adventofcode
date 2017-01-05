package adventofcode.day8;

public class InstructionFactory {

    public static Instruction parse(String string) {
        String[] commandParts = string.split(" ");
        String command = commandParts[0];
        if ("rect".equals(command)) {
            return new Rect(commandParts);
        } else if ("rotate".equals(command)) {
            return new Rotate(commandParts);
        }
        throw new RuntimeException();
    }

}
