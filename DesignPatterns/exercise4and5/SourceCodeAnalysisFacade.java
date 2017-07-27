package exercise4and5;

/**
 * Author: Christina Chaniotaki
 */

public class SourceCodeAnalysisFacade {
	public SourceCodeAnalysisFacade() {

	}

	private void writeCsvFile(String path, String outputText) {
		Utility write = new Utility();
		write.writeCSVFile(path, outputText);
	}

	private String calculateMetrics(String inputFile, String mode) {
		SourceCodeAnalyzerFactory scaf = new SourceCodeAnalyzerFactory();
		Analytics results = scaf.createSourceCodeAnalyzerFactory(mode, inputFile);
		return results.printMetrics();
	}

	public void analyseJavaFile(String inputFile, String outputFile, String mode) {
		String outputText = calculateMetrics(inputFile, mode);
		writeCsvFile(outputFile, outputText);
	}
}
