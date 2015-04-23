import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.PriorityQueue;
import java.util.Scanner;


public class Barber {
	public static void main(String[] args){
		Barber t = new Barber();
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
				int barbers = scan.nextInt();
				long placeN = scan.nextLong();
				
				long[] barberTimes = new long[barbers];
				for (int j = 0; j < barbers; j++) {
					barberTimes[j] = scan.nextLong();
				}
				
				PriorityQueue<BarberTime> queue = new PriorityQueue<BarberTime>();
				for (int j = 1; j <= barbers; j++) {
					BarberTime b = new BarberTime();
					b.index = j;
					b.time = 0;
					queue.offer(b);
				}
				
				long currentCustomer = 1;
				while(true) {
					BarberTime newest = queue.poll();
					long currentTime = newest.time;
					
					if (currentCustomer == placeN) {
						p.println("Case #" + i + ": " + newest.index);
						System.out.println("Case #" + i + ": " + newest.index);
						break;
					}
					// Re-offer the barber at the next possible time
					newest.time = currentTime + barberTimes[newest.index-1];
					queue.offer(newest);
					currentCustomer++;
				}
				
			}
			p.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
	}
	
	public static class BarberTime implements Comparable<BarberTime>{
		public long time;
		public int index;
		
		@Override
		public int compareTo(BarberTime b) {
			if (b.time == this.time) {
				return Integer.compare(this.index, b.index);
			} else {
				return Long.compare(this.time, b.time);
			}
		}
	}
}

