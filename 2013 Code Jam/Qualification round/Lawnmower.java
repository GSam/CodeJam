import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;


public class Lawnmower {
	public static void main(String [] args){
		Lawnmower l = new Lawnmower();
		l.mow();
	}
	
	public void mow(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			int[][] matrix;
			//while(scan.hasNextLine()){p.println(scan.nextLine());}
			for(int i = 1; i <= num; i++){
				int length = scan.nextInt();
				int width = scan.nextInt();
				scan.nextLine();
				matrix = new int[length][width];
				for(int y = 0; y < length; y++){
					String line = scan.nextLine();
					Scanner s = new Scanner(line);
					for(int x = 0; x < width; x++){
						matrix[y][x] = s.nextInt();
					}
				}
				//process array
				boolean answer = true;
				for(int y = 0; y < length; y++){
					if(!answer) break;
					for(int x = 0; x < width; x++){
						if(!answer) break;
						int item = matrix[y][x];
						boolean canAcross = true;
						boolean canVertical = true;
						for(int xCheck = 0; xCheck < width; xCheck++){
							if(item < matrix[y][xCheck]){
								canAcross = false;
							}
						}
						for(int yCheck = 0; yCheck < length; yCheck++){
							if(item < matrix[yCheck][x]){
								canVertical = false;
							}
						}
						if(!canAcross && !canVertical){
							answer = false;
						}
					}
				}
				if(answer){
					p.println("Case #" + i +": YES");
					System.out.println("Case #" + i +": YES");
				} else {
					p.println("Case #" + i +": NO");
					System.out.println("Case #" + i +": NO");
				}
				//System.out.println(matrix);
			}
			p.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
	}
}
