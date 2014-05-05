import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;


public class PowerSwitch {
	public static void main(String[] args){
		PowerSwitch t = new PowerSwitch();
		t.readInput();
	}
	
	public void readInput(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			for(int i = 1; i <= num; i++){
				int outlets = scan.nextInt();
				scan.nextInt();
				long[] initial = new long[outlets];
				long[] expected = new long[outlets];

				// initial
				for (int k = 0; k < outlets; k++) {
					initial[k] = scan.nextLong(2);
				}
				// expected
				for (int k = 0; k < outlets; k++) {
					expected[k] = scan.nextLong(2);
				}
				
				Arrays.sort(initial);
				Arrays.sort(expected);
				long ans = Long.MAX_VALUE;
				for (long outlet : initial) {
					long mask = outlet ^ expected[0];
					long[] temp = new long[outlets];
					for (int x = 0; x < outlets; x++) {
						temp[x] = initial[x] ^ mask;
					}
					Arrays.sort(temp);
					if (Arrays.equals(expected, temp)) {
						ans = Math.min(ans, Long.bitCount(mask));
					}
				}
				if (ans == Long.MAX_VALUE) {
					System.out.println(i + " max value");
					
				} else {
					System.out.println(i + "  " + ans);
				}
			}
			p.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}

