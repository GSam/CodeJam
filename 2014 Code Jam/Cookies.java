import java.io.File;
	import java.io.FileNotFoundException;
	import java.io.PrintStream;
	import java.util.HashSet;
	import java.util.Scanner;
	import java.util.Set;
	
public class Cookies {
	
		public static void main(String [] args){
			Cookies l = new Cookies();
			l.cookie();
		}
		
		public void cookie(){
			Scanner scan;
			try {
				scan = new Scanner(new File("input.txt"));
				PrintStream p = new PrintStream("output.txt");
				int num = scan.nextInt();
				
				for(int i = 1; i <= num; i++){
					// for each test case
					double cost = scan.nextDouble();
					double bonusPerFarm = scan.nextDouble();
					double goal = scan.nextDouble();
					
					double time = 0;
					double cookies = 0;
					double cookiesPerSec = 2;
					while(true) {
						// if you can buy a farm
						if (cookies >= cost) {
							double timeToMakeUp = cost / bonusPerFarm;
							if (timeToMakeUp * cookiesPerSec + cookies >= goal) {
								// if you can finish in the time it takes to make up the cookies
								// done
								time += (goal - cookies) / cookiesPerSec;
								break;
							} else {
								// buy a farm
								cookies -= cost;
								cookiesPerSec += bonusPerFarm;
							}
						} else {
							// cannot buy
							if (cost / cookiesPerSec > (goal - cookies) / cookiesPerSec) {
								// finished, couldn't reach another cookie checkpoint
								time += (goal - cookies) / cookiesPerSec;
								break;
							}
							// wait at next junction to buy cookies
							time += (cost / cookiesPerSec);
							cookies += cost;
							
						}	
					}
					
					System.out.printf("Case #%d: %4.7f\n", i, time);
					p.printf("Case #%d: %4.7f\n", i, time);
					
				}
				p.close();
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
			

		}
}
