// WIP
public class Problem549 {
	public static void main(String[] args) {
		int[] sieve = new int[(int)(Math.pow(10, 8)) + 1];
		int[] sieve2 = new int[(int)(Math.pow(10, 8)) + 1];
		for (int i = 0; i < sieve.length; i++) sieve[i] = i;
		long total = 0;
		double pow = Math.pow(10, 2) + 1;
		for (int x = 2; x < pow; x++) {
			if (x % 1000000 == 0) System.out.println(x);
			if (sieve[x] == 1) {
				// Nothing
			} else {
				total += x;
				System.out.println(x);
			}

			//if (x < Math.sqrt(pow)) {
				for (int y = x * 2; y < pow; y += x) {
					System.out.println("index: " + y + " sieve " + sieve[y]);
					if (sieve[y] % sieve[x] == 0) {
						sieve[y] /= sieve[x];
						if (sieve[y] == 1) {
							total += x;
							System.out.println("Add " + x + " Index " + y);
						}
					}
				}
			//}
		}
		System.out.println(total);

	}
}
