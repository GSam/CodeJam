/*
* Vida says she's part Elf: that at least one of her ancestors was an Elf. But she doesn't know if it was a parent (1 generation ago), a grandparent (2 generations ago), or someone from even more generations ago. Help her out!
*
* Being part Elf works the way you probably expect. People who are Elves, Humans and part-Elves are all created in the same way: two parents get together and have a baby. If one parent is A/B Elf, and the other parent is C/D Elf, then their baby will be (A/B + C/D) / 2 Elf. For example, if someone who is 0/1 Elf and someone who is 1/2 Elf have a baby, that baby will be 1/4 Elf.
*
* Vida is certain about one thing: 40 generations ago, she had 240 different ancestors, and each one of them was 1/1 Elf or 0/1 Elf.
* 
* Vida says she's P/Q Elf. Tell her what is the minimum number of generations ago that there could have been a 1/1 Elf in her family. If it is not possible for her to be P/Q Elf, tell her that she must be wrong!
*/
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
