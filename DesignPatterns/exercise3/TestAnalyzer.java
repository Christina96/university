package exercise3;

/**
 * Author: Christina Chaniotaki
 */

import java.util.ArrayList;

import exercise2.Utility;

public class TestAnalyzer {
    public static void main(String[] args) {
        Utility file = new Utility();
        String filename = "src/exercise3/Analyzer.java";
        ArrayList<String> text = file.readFile(filename);
        String fileText = "";
        for (String line : text) {
            fileText += line;
        }
        int loc = text.size();
        int noc = Analyzer.regex(fileText, "(public|protected|private|\\s) +class +[A-Z]");
        int nom = Analyzer.regex(fileText,
                "(public|protected|private|abstract|synchronized|volatile|static|final)+(\\s|)+(([\\w\\<\\" +
                        ">\\[\\]]){0}|([\\w\\<\\>\\[\\]]))+\\s+(\\w+)+(\\s|)*\\([^\\)]*\\)+(\\s|)*(\\{?|[^;])");
        String write = "Filename: " + filename + "\nLines of code: " + loc + "\nNumber of classes: " + noc
                + "\nNumber of methods: " + nom + "\nYou can find the result in results.txt";
        System.out.println(write);
        file.writeFile("results.txt", "Filename: " + filename);
        file.writeFile("results.txt", "Lines of code: " + loc);
        file.writeFile("results.txt", "Number of classes: " + noc);

    }
}
