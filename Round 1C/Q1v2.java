import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Q1v2 {
	public static void main(String[] args){
		Q1v2 t = new Q1v2();
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
				String name = scan.next();
				int n = scan.nextInt();
				int count = 0;
				Pattern pat = Pattern.compile("[^aeiou][^aeiou][^aeiou]");
				for(int l = 0; l < name.length(); l++){
					for(int r = l+1; r <= name.length(); r++){
						String sub = name.substring(l,r);
						Matcher m = pat.matcher(sub);
						while (m.find()) {
						    count++;
						}
					}
				}
				p.println("Case #" + i + ": " +count);			
			}
			p.close();
			//p.println("Case #" + i + ": " + j/2);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		System.out.println("DONE");
		
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

