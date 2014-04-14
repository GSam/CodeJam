import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;


public class TicTacToe {
	public static void main(String[] args){
		TicTacToe t = new TicTacToe();
		t.readInput();
	}
	
	public void readInput(){
		Scanner scan;
		try {
			scan = new Scanner(new File("input.txt"));
			PrintStream p = new PrintStream("output.txt");
			int num = scan.nextInt();
			int[][] matrix = new int[4][4];
			//while(scan.hasNextLine()){p.println(scan.nextLine());}
			for(int i = 1; i <= num; i++){
				scan.nextLine();
				for(int y = 0; y < 4; y++){
					String line = scan.nextLine();
					for(int x = 0; x < 4; x++){
						matrix[y][x] = line.charAt(x);
					}
				}
				//process array
				//try each row
				Boolean isWon = false;
				Boolean empty = false;
				for(int y = 0; y < 4; y++){
					int sum = 0;
					for(int x = 0; x < 4; x++){
						if(matrix[y][x] == '.'){
							empty = true;
						}
						sum += matrix[y][x];
					}
					if(!isWon && (sum == 'X' + 'X' + 'X' + 'X' || sum == 'X' + 'X' + 'X' + 'T')){
						p.println("Case #" + i + ": X won");
						isWon = true;
					} else if(!isWon && (sum == 'O' + 'O' + 'O' + 'O' || sum == 'T' + 'O' + 'O' + 'O')){
						p.println("Case #" + i + ": O won");
						isWon = true;
					}
				}
				//column
				for(int x = 0; x < 4; x++){
					int sum = 0;
					for(int y = 0; y < 4; y++){
						sum += matrix[y][x];
					}
					if(!isWon && (sum == 'X' + 'X' + 'X' + 'X' || sum == 'X' + 'X' + 'X' + 'T')){
						p.println("Case #" + i + ": X won");
						isWon = true;
					} else if(!isWon && (sum == 'O' + 'O' + 'O' + 'O' || sum == 'T' + 'O' + 'O' + 'O')){
						p.println("Case #" + i + ": O won");
						isWon = true;
					}
				}
				//Diagonal
				int sum = 0;
				for(int x = 0; x < 4; x++){
					sum += matrix[x][x];
					if(!isWon && (sum == 'X' + 'X' + 'X' + 'X' || sum == 'X' + 'X' + 'X' + 'T')){
						p.println("Case #" + i + ": X won");
						isWon = true;
					} else if(!isWon && (sum == 'O' + 'O' + 'O' + 'O' || sum == 'T' + 'O' + 'O' + 'O')){
						p.println("Case #" + i + ": O won");
						isWon = true;
					}
				}
				sum = 0;
				for(int x = 0; x < 4; x++){
					int y = 3 - x;
					sum += matrix[y][x];
					
					if(!isWon && (sum == 'X' + 'X' + 'X' + 'X' || sum == 'X' + 'X' + 'X' + 'T')){
						p.println("Case #" + i + ": X won");
						isWon = true;
					} else if(!isWon && (sum == 'O' + 'O' + 'O' + 'O' || sum == 'T' + 'O' + 'O' + 'O')){
						p.println("Case #" + i + ": O won");
						isWon = true;
					}
				}
				if(!isWon){
					if(empty){
						p.println("Case #" + i + ": Game has not completed");
					}else {
						p.println("Case #" + i + ": Draw");
					}
				}
			}
			p.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}

