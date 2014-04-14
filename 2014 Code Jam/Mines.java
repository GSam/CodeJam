import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;


public class Mines {
	public static void main(String [] args){
		Mines l = new Mines();
		l.mine();
	}
	public static int total = 0;
	public void mine(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			
			outer: for(int i = 1; i <= num; i++){
				// for each test case
				boolean [][] mines;
				int maxRows = scan.nextInt();
				int maxCols = scan.nextInt();
				mines = new boolean[maxRows][maxCols];
				
				int numMines = scan.nextInt();
				
				if (maxRows * maxCols < numMines) {
					// impossible
					System.out.println("Case #" + i + ": \nImpossible");
		//			System.out.println(maxRows + " " + maxCols + " " + numMines); printMines(mines); // TODO 
					continue;
				} else if (numMines == 0) {
					System.out.println("Case #" + i + ":");
					printMines(mines);
					if (total != numMines || total != 0) throw new RuntimeException();
					continue outer;
				} else if (numMines == maxRows * maxCols - 1) {
					for (int j = 0; j < maxCols; j++) {
						for (int k = 0; k < maxRows; k++) {
							mines[k][j] = true;
						}
					}
					System.out.println("Case #" + i + ":");
					printMines(mines);
					continue outer;
				}
				
				// one dimension less than 3 
				if (maxRows < 3) {
					// XXXXXXXXXX
					// XXXXXXXXXX
					if (numMines % maxRows != 0) {
						// impossible
						System.out.println("Case #" + i + ": \nImpossible");
	//					System.out.println(maxRows + " " + maxCols + " " + numMines); printMines(mines); // TODO 
						continue;
					}
					int mineCount = 0;
					for (int j = 0; j < maxCols - 2; j++) {
						for (int k = 0; k < maxRows; k++) {
							mines[k][j] = true;
							mineCount++;
							if (mineCount == numMines) {
								// done
								System.out.println("Case #" + i + ":");
								printMines(mines);
								if (total != numMines || total != mineCount) throw new RuntimeException();
								continue outer;
							}
							
						}
					}
					System.out.println("Case #" + i + ": \nImpossible");
	//				System.out.println(maxRows + " " + maxCols + " " + numMines); printMines(mines); // TODO 
					continue;
					
				} else if (maxCols < 3) {
					// XX
					// XX
					// XX
					if (numMines % maxCols != 0) {
						// impossible
						System.out.println("Case #" + i + ": \nImpossible");
	//					System.out.println(maxRows + " " + maxCols + " " + numMines); printMines(mines); // TODO 
						continue;
					}
					int mineCount = 0;
					for (int j = 0; j < maxRows - 2; j++) {
						for (int k = 0; k < maxCols; k++) {
							mines[j][k] = true;
							mineCount++;
							if (mineCount == numMines) {
								// done
								System.out.println("Case #" + i + ":");
								printMines(mines);
								if (total != numMines || total != mineCount) throw new RuntimeException();
								continue outer;
							}
							
						}
					}
					System.out.println("Case #" + i + ": \nImpossible");
	//				System.out.println(maxRows + " " + maxCols + " " + numMines); printMines(mines); // TODO 
					continue;
				}
				
				// otherwise fill it out
				{
					int mineCount = 0;
					for (int j = 0; j < maxCols - 3; j++) {
						for (int k = 0; k < maxRows; k++) {
							if (numMines - mineCount == 1 && k == maxRows - 2) {
								mines[0][j+1] = true;
								System.out.println("Case #" + i + ":");
								printMines(mines);
								mineCount += 1;
								if (total != numMines || total != mineCount) throw new RuntimeException();
								continue outer;
							}
							mines[k][j] = true;
							mineCount++;
							if (mineCount == numMines) {
								System.out.println("Case #" + i + ":");
								printMines(mines);
								if (total != numMines || total != mineCount) throw new RuntimeException();
								continue outer;
							}
							
						}
					}
					
					// now to assign the remainder
					for (int j = 0; j < maxRows - 3; j++) {
						for (int k = maxCols - 3; k < maxCols; k++) {
							if (numMines - mineCount == 1 && k == maxCols - 2) {
								mines[j + 1][maxCols - 3] = true;
								System.out.println("Case #" + i + ":");
								printMines(mines);
								mineCount += 1;
								if (total != numMines || total != mineCount) throw new RuntimeException();
								continue outer;
							}
							mines[j][k] = true;
							mineCount++;
							if (mineCount == numMines) {
								System.out.println("Case #" + i + ":");
								printMines(mines);
								if (total != numMines || total != mineCount) throw new RuntimeException();
								continue outer;
							}
						}
						
					}
					
					// on last 3x3 box
					mines[maxRows - 3][maxCols - 3] = true;
					mineCount++;
					if (numMines == mineCount) {
						System.out.println("Case #" + i + ":");
						printMines(mines);
						if (total != numMines || total != mineCount) throw new RuntimeException();
						continue outer;
					} 
					
					if (numMines - mineCount == 2 || numMines - mineCount == 4) {
						if (numMines - mineCount == 2) {
							mines[maxRows - 3][maxCols - 3 + 1] = true;
							mines[maxRows - 3][maxCols - 3 + 2] = true;
							System.out.println("Case #" + i + ":");
							printMines(mines);
							mineCount += 2;
							if (total != numMines || total != mineCount) throw new RuntimeException();
							continue outer;
						} else {
							mines[maxRows - 3][maxCols - 3 + 1] = true;
							mines[maxRows - 3][maxCols - 3 + 2] = true;
							
							mines[maxRows - 3 + 1][maxCols - 3] = true;
							mines[maxRows - 3 + 2][maxCols - 3] = true;
							System.out.println("Case #" + i + ":");
							printMines(mines);
							mineCount += 4;
							if (total != numMines || total != mineCount) throw new RuntimeException();
							continue outer;
						}
					} else {
						// impossible
						System.out.println("Case #" + i + ": \nImpossible");
	//					System.out.println(maxRows + " " + maxCols + " " + numMines); printMines(mines); // TODO 
						continue;
					}
				}
				
			}
			p.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		

	}

	private void printMines(boolean[][] mines) {
		total = 0;
		for(int i = 0; i < mines.length; i++) {
			for (int j = 0; j < mines[0].length; j++) {
				if (i == mines.length - 1 && j == mines[0].length - 1) {
					System.out.print("c");
				} else {
					System.out.print(mines[i][j] ? '*' : '.');
				}
				if (j == mines[0].length - 1) {
					System.out.println();
				}
				if (mines[i][j]) total++;
			}
		}
		
	}
}
