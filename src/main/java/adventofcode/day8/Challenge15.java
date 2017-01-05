package adventofcode.day8;

import java.io.IOException;

import com.google.common.base.Charsets;
import com.google.common.io.Resources;

public class Challenge15 {

    public static void main(String[] args) throws IOException {
        String data = Resources.toString(Resources.getResource("day8.data"), Charsets.UTF_8);

        String[] rowsOfCommands = data.split("\n");

        Screen screen = new Screen(50, 6);

        for (String command : rowsOfCommands) {
            Instruction instruction = InstructionFactory.parse(command);
            instruction.transformScreen(screen);
        }

        System.out.println(screen.print());
        System.out.println(screen.count());

    }
}
