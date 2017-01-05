package adventofcode.day8;

public class Rect implements Instruction {

    private Integer width;
    private Integer height;

    public Rect(String[] commandParts) {
        String AB = commandParts[1];
        width = Integer.valueOf(AB.split("x")[0]);
        height = Integer.valueOf(AB.split("x")[1]);
    }

    @Override
    public void transformScreen(Screen previousScreen) {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                previousScreen.switchOn(j, i);
            }
        }
    }

}
