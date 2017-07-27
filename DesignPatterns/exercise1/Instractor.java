package exercise1;

/**
 * Author: Christina Chaniotaki
 */

import java.util.Observable;
import java.util.Observer;

public class Instractor implements Observer {

    public Instractor() {

    }

    @Override
    public void update(Observable o, Object arg) {
        System.out.println("Time changed from Instractor");

    }

}