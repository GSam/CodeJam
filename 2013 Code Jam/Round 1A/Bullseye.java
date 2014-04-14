import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;


public class Bullseye {
	public static void main(String[] args){
		Bullseye t = new Bullseye();
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
				long radius = scan.nextLong();
				long paint = scan.nextLong();
				long usedPaint = 0;
				for(int j = 1;;j += 2){
					long first = radius + j;
					long second = radius + j - 1;
					long newRing = first * first  - second * second;
					if(usedPaint + newRing <= paint){
						usedPaint += newRing;
					} else {
						p.println("Case #" + i + ": " + j/2);
						break;
					}
				}

				
			}
			p.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}

