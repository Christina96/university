package exercise1;

/**
 * Author: Christina Chaniotaki
 */

import java.util.Observable;
import java.util.Observer;

public class Organizer implements Observer {

    public Organizer() {

    }

    @Override // enimeronei otan ginete kapoio update!
    public void update(Observable o, Object arg) {
        System.out.println("Time changed from Organizer");

    }
}
