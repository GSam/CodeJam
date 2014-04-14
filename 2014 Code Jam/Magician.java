import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;


public class Magician {
	public static void main(String [] args){
		Magician l = new Magician();
		l.magic();
	}
	
	public void magic(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			
			for(int i = 1; i <= num; i++){
				// for each test case
				int row1 = scan.nextInt();
				Set<Integer> rowSet1 = new HashSet<Integer>();
				for (int row = 0; row < 4; row++) {
					if (row1 == row + 1) {
						rowSet1.add(scan.nextInt());
						rowSet1.add(scan.nextInt());
						rowSet1.add(scan.nextInt());
						rowSet1.add(scan.nextInt());
					} else {
						scan.nextInt();
						scan.nextInt();
						scan.nextInt();
						scan.nextInt();
					}
				}
				
				int row2 = scan.nextInt();
				Set<Integer> rowSet2 = new HashSet<Integer>();
				for (int row = 0; row < 4; row++) {
					if (row2 == row + 1) {
						rowSet2.add(scan.nextInt());
						rowSet2.add(scan.nextInt());
						rowSet2.add(scan.nextInt());
						rowSet2.add(scan.nextInt());
					} else {
						scan.nextInt();
						scan.nextInt();
						scan.nextInt();
						scan.nextInt();
					}
				}
				
				rowSet1.retainAll(rowSet2);
				switch(rowSet1.size()) {
				case 1:
					System.out.println("Case #" + i + ": " + rowSet1.iterator().next());
					break;
				case 0:
					System.out.println("Case #" + i +": Volunteer cheated!");
					break;
				default:
					System.out.println("Case #" + i + ": Bad magician!");
				
				}
				
			}
			p.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
	}
}
