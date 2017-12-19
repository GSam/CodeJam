import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class PE79 {
	public static void main(String[] args) {
		PE79.solve();
	}
	
	public static void solve(){
		try {
			Scanner s = new Scanner(new File("keylog.txt"));
			ArrayList<String> attempts = new ArrayList<String>();
			while(s.hasNext()){
				attempts.add(s.next());
			}
			for(int i = 0; i < 100000000; i++){
				String pot = Integer.toString(i);
				boolean fine = true;
				for(int j = 0; j < attempts.size(); j++){
					String temp = attempts.get(j);
					int index1 = pot.indexOf(temp.charAt(0));
					if (index1 == -1) {
						fine = false;
						break;
					}
					int index2 = pot.indexOf(temp.charAt(1), index1+1);
					if(index2 == -1){
						fine = false;
						break;
					}
					int index3 = pot.indexOf(temp.charAt(2), index2+1);
					if(index3 == -1){
						fine = false;
						break;
					}
				}
				if(fine){
					System.out.println(i);
				}
			}
			s.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
