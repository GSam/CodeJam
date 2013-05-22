import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Scanner;


public class Pogo {
	public static void main(String[] args){
		Pogo t = new Pogo();
		t.readInput();
	}
	
	public enum Direction {N, W, E, S};
	
	public void readInput(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			for(int i = 1; i <= num; i++){
				scan.nextLine();
				int x = scan.nextInt();
				int y = scan.nextInt();
				int count = 1;
				int xPos = 0;
				int yPos = 0;
				String ans = recurse("", xPos, yPos, count, x, y);
				p.println("Case #" + i + ": " + ans);	
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		System.out.println("DONE");
		
	}
	
	private String recurse(String ans, int xPos, int yPos, int count, int x, int y) {
		if(count > 20){
			return null;
		}
		if(xPos == x && yPos == y){
			return ans;
		}
		String a = recurse(ans + "N", xPos, yPos + 1, count+1, x,y);
		if(a != null) return a;
		a = recurse(ans + "E", xPos + 1, yPos, count+1, x,y);
		if(a != null) return a;
		a = recurse(ans + "S", xPos, yPos -1, count+1, x,y);
		if(a != null) return a;
		a = recurse(ans + "W", xPos-1, yPos, count+1, x,y);
		if(a != null) return a;
		return null;
	}

	public boolean countCon(String s, long n){
		long count = 0;
		for(int i = 0; i < s.length(); i++){
			if(isConsonant(s.charAt(i))){
				count++;
				if(count >= n){
					return true;
				}
			} else {
				count = 0;
			}
		}
		return false;
	}
	
	public boolean isConsonant(char c){
		switch(c){
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':return false;
		default: return true;
		}
	}
	
	
	
}

