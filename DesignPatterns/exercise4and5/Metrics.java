package exercise4and5;

/**
 * Author: Christina Chaniotaki
 */

public class Metrics {

	private int nol;
	private int noc;
	private int nom;

	public Metrics(int nol, int noc, int nom) {
		this.nol = nol;
		this.noc = noc;
		this.nom = nom;
	}

	public int getNol() {
		return this.nol;
	}

	public int getNoc() {
		return this.noc;
	}

	public int getNom() {
		return this.nom;
	}

	public void setNol(int nol) {
		this.nol = nol;
	}

	public void setNoc(int noc) {
		this.noc = noc;
	}

	public void setNom(int nom) {
		this.nom = nom;
	}
}
