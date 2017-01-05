package adventofcode.day8;

import java.util.ArrayList;
import java.util.List;

public class Screen {

    private Pixel[] pixels;
    private int rows;
    private int columns;

    public Screen(int rows, int columns) {
        this.rows = columns;
        this.columns = rows;
        pixels = new Pixel[columns * rows];

        for (int i = 0; i < columns * rows; i++) {
            pixels[i] = Pixel.off;
        }
    }

    public String print() {
        String output = "";
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                output += pixels[pixelIndex(j, i)].toString();
            }
            output += "\n";
        }
        return output;
    }

    public Integer count() {
        int count = 0;
        for (Pixel pixel : pixels) {
            if (pixel.equals(Pixel.on)) {
                count++;
            }
        }
        return count;
    }

    public void switchOn(int x, int y) {
        pixels[pixelIndex(x, y)] = Pixel.on;
    }

    private int pixelIndex(int x, int y) {
        return x + columns * y;
    }

    public void rotateColumn(Integer column, Integer distance) {
        List<Pixel> columnOfPixels = new ArrayList<Pixel>();
        for (int i = 0; i < rows; i++) {
            columnOfPixels.add(pixels[pixelIndex(column, i)]);
        }

        for (int i = 0; i < rows; i++) {
            pixels[pixelIndex(column, (i + distance) % rows)] = columnOfPixels.get(i);
        }
    }

    public void rotateRow(Integer row, Integer distance) {
        List<Pixel> rowOfPixels = new ArrayList<Pixel>();
        for (int i = 0; i < columns; i++) {
            rowOfPixels.add(pixels[pixelIndex(i, row)]);
        }

        for (int i = 0; i < columns; i++) {
            pixels[pixelIndex((i + distance) % columns, row)] = rowOfPixels.get(i);
        }
    }

}
