package exercise4and5;

/**
 * Author: Christina Chaniotaki
 */

public class Analytics extends Metrics {
	private String javaFile;

	public Analytics(int nol, int noc, int nom, String javaFile) {
		super(nol, noc, nom);
		this.setJavaFile(javaFile);

	}

	public String getJavaFile() {
		return javaFile;
	}

	public void setJavaFile(String javaFile) {
		this.javaFile = javaFile;
	}

	public String printMetrics() {
		String write = "Filename: " + this.javaFile + "\nNumber of lines: " + getNol() + "\nNumber of classes: "
				+ getNoc() + "\nNumber of methods: " + getNom();
		return write;
	}

}
