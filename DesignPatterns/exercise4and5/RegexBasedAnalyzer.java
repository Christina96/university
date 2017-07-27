package exercise4and5;

/**
 * Author: Christina Chaniotaki
 */

import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexBasedAnalyzer implements SourceCodeAnalyzer {
    private String codeString;
    private ArrayList<String> text;

    public RegexBasedAnalyzer(String codeString, ArrayList<String> text) {
        this.codeString = codeString;
        this.text = text;
    }

    public ArrayList<String> getText() {
        return this.text;
    }

    public void setCodeString(String codeString) {
        this.codeString = codeString;
    }

    public void setText(ArrayList<String> text) {
        this.text = text;
    }

    @Override
    public int calculateNol() {
        return this.text.size();
    }

    @Override
    public int calculateNoc() {
        return regex(this.codeString, "(public|protected|private|\\s) +class +" +
                "[A-Z]");
    }

    @Override
    public int calculateNom() {
        return regex(this.codeString,
                "(public|protected|private|abstract|synchronized|volatile|static|final)+(\\s|)+(([\\w\\<\\" +
                        ">\\[\\]]){0}|([\\w\\<\\>\\[\\]]))+\\s+(\\w+)+(\\s|)*\\([^\\)]*\\)+(\\s|)*(\\{?|[^;])");
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
