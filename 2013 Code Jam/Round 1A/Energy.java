import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.*;


public class Energy {
	public static void main(String[] args){
		Energy t = new Energy();
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
				int maxE = scan.nextInt();
				int regain = scan.nextInt();
				int numAct = scan.nextInt();
				scan.nextLine();
				int [] acts = new int[numAct];
				for(int j = 0; j < numAct; j++){
					acts[j] = scan.nextInt();
				}
				int ans = total(search(new int[numAct], 0, maxE, maxE, regain, acts), acts);
				
			}
			p.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	private int[] search(int[] array, int pos, int energy, int maxE, int regain, int[] factors){
		if(pos >= array.length) return array;
		int[] result = new int[0];
		int largest = 0;
		for(int i = 0; i <= energy; i++){
			int[] newArray = array.clone();
			newArray[pos] = i;
			int[] temp = search(newArray, pos+1, Math.min(maxE,energy-i+regain), maxE, regain,factors);
			if(total(temp,factors) > largest){
				result = temp;
				largest = total(temp,factors);
			}
		}
		return result;
	}
	
	private int total(int[] array,int[] factors){
		int sum = 0;
		for(int i = 0; i < array.length; i++){
			sum += array[i] * factors[i];
		}
		return sum;
	}
}

