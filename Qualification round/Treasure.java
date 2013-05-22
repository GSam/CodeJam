import java.util.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;


public class Treasure {
	
	public static void main(String [] args){
		Treasure t = new Treasure();
		t.findOrder();
	}
	
	public void findOrder(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			for(int i = 1; i <= num; i++){
				int numKeys = scan.nextInt();
				int numChest = scan.nextInt();
				List<Set<Chest>> keyToChest = new ArrayList<Set<Chest>>(201);//at most 200 key numbers
				for(int x = 0; x < 201; x++){
					keyToChest.add(new HashSet<Chest>());
				}
				scan.nextLine();
				List<Integer> keys = new ArrayList<Integer>(); //the held keys
				for(int key = 0; key < numKeys; key++){
					keys.add(scan.nextInt());
					
				}
				//chest permutations
				Chest[] chestPermute = new Chest[numChest];
				int[] permutation = new int[numChest];
				for(int c = 0; c < numChest; c++){
					scan.nextLine();
					permutation[c] = c;
					chestPermute[c] = new Chest();
					Set<Chest> kTC = keyToChest.get(scan.nextInt());
					kTC.add(chestPermute[c]);
					int kCount = scan.nextInt();

					for(int k = 0; k < kCount; k++){
						int number = scan.nextInt();
						chestPermute[c].keys.add(number);
					}
				}

				boolean validPermute = false;
				do{
					//String s = "";
					//for(int v = 0; v < permutation.length; v++){
					//	s += " " + (permutation[v] + 1);
					//}
					//System.out.println(s);
					List<Integer> copyBaseKey = new ArrayList<Integer>();
					for(int x = 0; x < keys.size();x++){
						copyBaseKey.add(new Integer(keys.get(x)));
					}
					for(int x = 0; x < permutation.length; x++){
						//check if you have the key
						boolean haveKey = false;
						for(int y = 0; y < copyBaseKey.size(); y++){
							int k = copyBaseKey.get(y);
							if(keyToChest.get(k).contains(chestPermute[permutation[x]])){
								copyBaseKey.addAll(chestPermute[permutation[x]].keys);
								haveKey = true;
								copyBaseKey.remove(y);
								break;
							}
						}
						if(!haveKey){
							break;
						} 
						if(x == permutation.length -1) validPermute = true;
					}
					if(validPermute){
						break;
					}
				}while(permute(permutation));

				if(validPermute){
					String s = "";
					for(int v = 0; v < permutation.length; v++){
						s += " " + (permutation[v] + 1);
					}
					p.println("Case #" + i +":" + s);
				}else p.println("Case #" + i +": IMPOSSIBLE");
			}
			p.close();
			System.out.println("DONE");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	private class Chest{
		public List<Integer> keys = new ArrayList<Integer>();
	}
	
	public boolean permute(int[] permutation){
		for(int k = permutation.length-2; k >= 0; k--){
			if(permutation[k] < permutation[k+1]){
				for(int l = permutation.length-1; l>=0; l--){
					if(permutation[k] < permutation[l]){
						int temp = permutation[k];
						permutation[k] = permutation[l];
						permutation[l] = temp;
						for(int x = k+1; x < (k + 1 + permutation.length)/2; x++){
							int t = permutation[x];
							permutation[x] = permutation[permutation.length-1-(x-(k+1))];
							permutation[permutation.length-1-(x-(k+1))] = t;
						}
						return true;
					}
				}
			}
		}
		return false;
	}

}
