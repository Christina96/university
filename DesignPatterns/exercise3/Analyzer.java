package exercise3;

/**
 * Author: Christina Chaniotaki
 */

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Analyzer {

    public Analyzer() {

    }

    public static int regex(String text, String expression) {
        Pattern pattern = Pattern.compile(expression);
        Matcher matcher = pattern.matcher(text);
        return countMatches(matcher);
    }

    public static int countMatches(Matcher matcher) {
        int count = 0;
        while (matcher.find()) {
            count++;
        }
        return count;
    }

}
