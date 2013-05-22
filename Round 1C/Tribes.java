import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Scanner;


public class Tribes {
	public static void main(String[] args){
		Tribes t = new Tribes();
		t.readInput();
	}
	
	public void readInput(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			for(int i = 1; i <= num; i++){
				scan.nextLine();
				int tribes = scan.nextInt();
				ArrayList<Tribe> list = new ArrayList<Tribe>();
				for(int j = 0; j < tribes; j++){
					Tribe t = new Tribe(scan.nextInt(),scan.nextInt(),scan.nextInt(),scan.nextInt(),scan.nextInt(),scan.nextInt(),scan.nextInt(),scan.nextInt());
					list.add(t);
				}
				for(int time = 0; time < 676061; time++){
					
				}
				p.println("Case #" + i + ": " );			
			}
			p.close();
			//p.println("Case #" + i + ": " + j/2);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		System.out.println("DONE");
		
	}
	
	private class Tribe{
		int di;
		int numAtt;
		int west;
		int east;
		int str;
		int deltad;
		int deltap;
		int deltastr;
		int time = 0;
		int position = 0;
		public Tribe(int di, int numAtt, int west, int east, int str, int deltad, int deltap, int deltastr){
			this.di = di;
			this.numAtt = numAtt;
			this.west = west;
			this.east = east;
			this.str = str;
			this.deltad = deltad;
			this.deltap = deltap;
			this.deltastr = deltastr;
		}
		
		public void add(){
			time += deltad;
			position += deltap;
			str += deltastr;
		}
		
	}
}

