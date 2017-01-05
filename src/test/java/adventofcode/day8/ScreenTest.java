package adventofcode.day8;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

import org.junit.Test;

public class ScreenTest {

    @Test
    public void printTest() {
        Screen screen = new Screen(7, 3);
        String output = screen.print();

        System.out.println(output);
        assertThat(output, is(".......\n.......\n.......\n"));
    }

    @Test
    public void printTestAfterSwitchingOnAPixel() {
        Screen screen = new Screen(7, 3);
        screen.switchOn(3, 1);
        String output = screen.print();

        System.out.println(output);
        assertThat(output, is(".......\n...#...\n.......\n"));
    }

    @Test
    public void printTestAfterSwitchingOnAPixelAndRotatingColumn() {
        Screen screen = new Screen(7, 3);
        screen.switchOn(3, 1);
        screen.rotateColumn(3, 1);
        String output = screen.print();

        System.out.println(output);
        assertThat(output, is(".......\n.......\n...#...\n"));
    }

    @Test
    public void printTestAfterSwitchingOnAPixelAndRotatingRow() {
        Screen screen = new Screen(7, 3);
        screen.switchOn(3, 1);
        screen.rotateRow(1, 1);
        String output = screen.print();

        System.out.println(output);
        assertThat(output, is(".......\n....#..\n.......\n"));
    }

}
