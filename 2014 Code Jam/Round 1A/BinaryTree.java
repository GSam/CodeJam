import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;


public class BinaryTree {
	public static void main(String[] args){
		BinaryTree t = new BinaryTree();
		t.readInput();
	}
	public static ArrayList[] nodes;
	public void readInput(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			for(int i = 1; i <= num; i++){
				int numNodes = scan.nextInt();
				// tree has n-1 edges
				nodes = new ArrayList[numNodes];
				for (int n = 0; n < numNodes; n++) {
					nodes[n] = new ArrayList();
				}
				
				for (int n = 0; n < numNodes - 1; n++) {
					int node1 = scan.nextInt() - 1; // index from 0 to n - 2
					int node2 = scan.nextInt() - 1;
					nodes[node1].add(node2);
					nodes[node2].add(node1);
					// node list is pairs of nodes it is connected to
				}
				
				// perform a depth first search
				// count number of possible nodes in full binary tree
				int[] countArray = new int[numNodes];
				// haven't visited any nodes
				int ans = Integer.MAX_VALUE;
				for (int w = 0; w < numNodes; w++) {
					Arrays.fill(countArray, -1);
					ans = Math.min(ans, numNodes - dfs(w, -1000, numNodes, countArray));
				}
				p.println("Case #" + i+": " + ans);
			}
			p.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	// i = currentNode
	private int dfs(int i, int j, int numNodes, int[] countArray) {
		// if you haven't visited this node before
		if (countArray[i] == -1) {
			// for each edge
			int max1 = -1;
			int max2 = -1;
			
			for (int edge : (ArrayList<Integer>) nodes[i]) {
				if (edge == j) // if parent is node
					continue;
				int v = dfs(edge, i, numNodes, countArray);
				if (v > max1) {
					max2 = max1; 
					max1 = v;
				} else if (v > max2) {
					max2 = v;
				}
			}
			
			if (max2 == -1) {
				countArray[i] = 1;
			} else {
				countArray[i] = 1 + max1 + max2;
			}
			
		}
		return countArray[i];
	}
}

