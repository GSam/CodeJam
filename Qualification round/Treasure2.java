import java.util.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;


public class Treasure2 {
	public static void main(String [] args){
		Treasure2 t = new Treasure2();
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
				 //at most 200 key numbers
				List<Set<Chest>> keyToChest = new ArrayList<Set<Chest>>(201);
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
					chestPermute[c].index = c;
					Set<Chest> kTC = keyToChest.get(scan.nextInt());
					kTC.add(chestPermute[c]);
					int kCount = scan.nextInt();

					for(int k = 0; k < kCount; k++){
						int number = scan.nextInt();
						chestPermute[c].keys.add(number);
					}
				}

				List<Integer> copyBaseKey = new ArrayList<Integer>();
				for(int x = 0; x < keys.size();x++){
					copyBaseKey.add(new Integer(keys.get(x)));
				}
				List<Integer> steps = find(new ArrayList<Integer>(), chestPermute, keyToChest, copyBaseKey);

				if(steps != null){
					String s = "";
					for(int v : steps){
						s += " " + (v + 1);
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
	
	private List<Integer> find(List<Integer> steps, Chest[] chestPermute, List<Set<Chest>> keyToChest, List<Integer> copyBaseKey) {
		//if you've visited all chests, return something
		if(steps.size() == chestPermute.length){
			return steps;
		}
		//for all the possible chests, choose one in order
		Set<Chest> posChests = new HashSet<Chest>();
		for(int k : copyBaseKey){
			posChests.addAll(keyToChest.get(k));
		}
		List<Chest> posChestSort = new ArrayList<Chest>(posChests);
		Collections.sort(posChestSort);
		String s = "";
		for(int v : steps){
			s += " " + (v + 1);
		}
		System.out.println(s);
		for(Chest c : posChestSort){
			if(steps.contains(c.index)) continue;
			List<Integer> newStep = new ArrayList<Integer>(steps);
			newStep.add(c.index);
			List<Integer> newKey = new ArrayList<Integer>(copyBaseKey);
			for(int x = 0; x < copyBaseKey.size(); x++){
				int k = copyBaseKey.get(x);
				if(keyToChest.get(k).contains(c)){
					newKey.remove(x);
					break;
				}
			}
			newKey.addAll(c.keys);
			List<Integer> ans = find(newStep, chestPermute, keyToChest, newKey);
			if(ans != null) return ans;
		}
		return null;
	}

	private class Chest implements Comparable<Chest>{
		public List<Integer> keys = new ArrayList<Integer>();
		public int index;
		public int compareTo(Chest c){
			return index - c.index;
		}
	}
	


}
