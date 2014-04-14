import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;


public class War {
	public static void main(String [] args){
		War l = new War();
		l.war();
	}
	
	public void war(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			
			for(int i = 1; i <= num; i++){
				// for each test case
				int blocksEach = scan.nextInt();
				TreeSet<Double> p1 = new TreeSet<Double>();
				TreeSet<Double> p2 = new TreeSet<Double>();
				// Initialise player sets into a sorted set
				for (int b = 0; b < blocksEach; b++) {
					p1.add(scan.nextDouble());
				}
				for (int b = 0; b < blocksEach; b++) {
					p2.add(scan.nextDouble());
				}

				TreeSet<Double> p11 = new TreeSet<Double>(p1);
				TreeSet<Double> p21 = new TreeSet<Double>(p2);
				// rounds of the game
				int points = 0;
				for (int s = 0; s < blocksEach; s++) {
					if (p1.first() < p2.first()) {
						// if you have the lowest, concede the point
						// steal their highest by bluffing
						p1.pollFirst();
						p2.pollLast();
					} else {
						// you can win a point
						p1.pollFirst();
						p2.pollFirst();
						points += 1;
					}
				}
				
				int points2 = 0;
				for (int s = 0; s < blocksEach; s++) {
					double proposed = p11.pollFirst();
					Double prop = p21.ceiling(proposed);
					if (prop == null) {
						// if you are greater than all theirs
						p21.pollFirst();
						points2 +=1;
					} else {
						// if they have something greater
						p21.remove(prop);
					}
					
				}
				System.out.println("Case #" + i + ": " + points + " " + points2);
			}
			p.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		

	}

}
