package exercise4and5;

/**
 * Author: Christina Chaniotaki
 */

import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileWriter;

public class Utility {
	public Utility() {

	}

	public ArrayList<String> readFile(String Filename) {
		BufferedReader br = null;
		FileReader fr = null;
		ArrayList<String> x = new ArrayList<String>();
		try {
			fr = new FileReader(Filename);
			br = new BufferedReader(fr);
			String sCurrentLine;
			br = new BufferedReader(new FileReader(Filename));
			while ((sCurrentLine = br.readLine()) != null) {
				x.add(sCurrentLine);
			}
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if (br != null)
					br.close();
				if (fr != null)
					fr.close();
			} catch (IOException ex) {
				System.out.println(ex.getMessage());
			}
		}
		return x;
	}

	public void writeCSVFile(String filename, String text) {
		try {
			FileWriter writer = new FileWriter(filename, false);
			writer.append(text);
			writer.flush();
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}