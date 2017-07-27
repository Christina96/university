package exercise4and5;

/**
 * Author: Christina Chaniotaki
 */

public class TestAnalyzer {
	public static void main(String[] args) {
		SourceCodeAnalysisFacade scaf = new SourceCodeAnalysisFacade();
		scaf.analyseJavaFile("src/exercise4and5/Utility.java", "resultsRegex.csv", "regex");
		scaf.analyseJavaFile("src/exercise4and5/Utility.java", "resultsString.csv", "string");
	}
}
