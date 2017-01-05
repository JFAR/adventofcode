package adventofcode.day8;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class Challenge15Test {

    @Test
    public void rectIntructionCountsCorrectly() {
        Screen screen = new Screen(7, 4);
        Instruction instruction = InstructionFactory.parse("rect 3x4");
        instruction.transformScreen(screen);
        assertThat(screen.count(), is(12));
    }

    @Test
    public void workedExample() {
        Screen screen = new Screen(7, 3);
        List<Instruction> instructions = new ArrayList<Instruction>();
        instructions.add(InstructionFactory.parse("rect 3x2"));
        instructions.add(InstructionFactory.parse("rotate column x=1 by 1"));
        instructions.add(InstructionFactory.parse("rotate row y=0 by 4"));
        instructions.add(InstructionFactory.parse("rotate column x=1 by 1"));
        instructions.add(InstructionFactory.parse("rect 1x1"));

        for (Instruction instruction : instructions) {
            instruction.transformScreen(screen);
        }

        System.out.println(screen.print());
        assertThat(screen.count(), is(7));
    }
}
