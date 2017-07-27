package exercise4and5;

/**
 * Author: Christina Chaniotaki
 */

import java.util.ArrayList;

public class StringBasedAnalyzer implements SourceCodeAnalyzer {
	private ArrayList<String> text;

	public StringBasedAnalyzer(ArrayList<String> text) {
		this.text = text;
	}

	public ArrayList<String> getText() {
		return this.text;
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
		int noc = 0;
		for (String line : this.text) {
			if ((line.startsWith("public") || line.startsWith("private") || line.startsWith("protected"))
					&& (line.endsWith("{")) && (line.contains("class"))) {
				noc++;
			}
		}
		return noc;
	}

	@Override
	public int calculateNom() {
		int nom = 0;
		for (String line : this.text) {
			if ((line.contains("public") || line.contains("private") || line.contains("protected")
					|| line.contains("static") || line.contains("abstract") || line.contains("synchronized")
					|| line.contains("volatile") || line.contains("final")) && (line.endsWith("{"))
					&& (line.contains("(") && line.contains(")"))) {
				nom++;
			}
		}
		return nom;
	}

}
