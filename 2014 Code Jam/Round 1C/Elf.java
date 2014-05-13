import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;


public class Elf {
	public static void main(String [] args){
		Elf l = new Elf();
		l.start();
	}
	
	public void start(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();

		outer: for(int i = 1; i <= num; i++){
				String fraction = scan.next();
				long nums = Long.parseLong(fraction.split("/")[0]);
				long denom = Long.parseLong(fraction.split("/")[1]);
				
				long count = 0;
				long minCount = Long.MAX_VALUE;
				while (count < 40) {
					count++;
					if (nums * 2 > denom) {
						nums = nums * 2 - denom;
						minCount = Math.min(minCount, count);
						continue;
					} else if (nums * 2 == denom) {
						System.out.println("Case #" + i +": " + Math.min(count, minCount));
						continue outer;
					}
					nums *= 2;
				}
				if (count >= 40) {
					System.out.println("Case #" + i +": impossible");
				}
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
	}
}
