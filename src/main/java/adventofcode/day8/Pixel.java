package adventofcode.day8;

public enum Pixel {
    on("#"), off(".");

    private String representation;

    private Pixel(String representation) {
        this.representation = representation;
    }

    @Override
    public String toString() {
        return this.representation;
    }
}
