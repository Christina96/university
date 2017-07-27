package exercise1;

/**
 * Author: Christina Chaniotaki
 */

public class Test {

	public static void main(String[] args) {
		Course course = new Course(0, 0);

		course.addObserver(new Student());
		course.addObserver(new Instractor());
		course.addObserver(new Organizer());

		course.setStart(5);
		course.setStop(6);
		course.all();

	}

}