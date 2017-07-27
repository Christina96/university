package exercise4and5;

/**
 * Author: Christina Chaniotaki
 */

import java.util.ArrayList;

public class SourceCodeAnalyzerFactory {
	public Analytics createSourceCodeAnalyzerFactory(String mode, String filename) {
		int nol = 0;
		int noc = 0;
		int nom = 0;
		Analytics ana = new Analytics(nol, noc, nom, filename);
		Utility x = new Utility();
		ArrayList<String> text = x.readFile(filename);
		if (mode.equals("regex")) {
			String codeString = "";
			for (String line : text) {
				codeString += line;
			}
			RegexBasedAnalyzer rba = new RegexBasedAnalyzer(codeString, text);
			nol = rba.calculateNol();
			noc = rba.calculateNoc();
			nom = rba.calculateNom();
			ana.setNol(nol);
			ana.setNoc(noc);
			ana.setNom(nom);
			return ana;

		} else {
			StringBasedAnalyzer sba = new StringBasedAnalyzer(text);
			nol = sba.calculateNol();
			noc = sba.calculateNoc();
			nom = sba.calculateNom();
			ana.setNol(nol);
			ana.setNoc(noc);
			ana.setNom(nom);
			return ana;
		}
	}
}
