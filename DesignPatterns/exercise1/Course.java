package exercise1;

/**
 * Author: Christina Chaniotaki
 */

import java.util.Observable;

public class Course extends Observable {
    private int start;
    private int stop;

    public Course(int start, int stop) {
        this.start = start;
        this.stop = stop;
    }

    public void setStart(int start) {
        this.start = start;
    }

    public void setStop(int stop) {
        this.stop = stop;
    }

    public int getStart() {
        return this.start;
    }

    public int getStop() {
        return this.stop;
    }

    public void all() {
        setChanged();
        notifyObservers();
    }
}