import java.util.ArrayList;

/**
 * Generate the co-primes from (1,1) to (m,n)
 * 
 * [John Bonanno]
 *
 */
public class CoPrimes {
	
	
	public static void main(String[] args) {
		if (args.length != 2) {
			System.err.println("Must be passed two integer values > 0");
			
			System.exit(0);
		}
		
		int m = Integer.parseInt(args[0]);
		int n = Integer.parseInt(args[1]);
		//creates new string array 
		String [][] table = new String [m+1][n+1];		
		
		
		//nested for loop to populate array, 
		for(int x = 15; x>0;x--){

		for(int y =1; y<=15;y++) {
			table[x][y] = x+","+y +" ";
	        if((gcf(x,y)==1)) {
	      	System.out.print(" * ");} //prints asterisk for coprime pairs
	        	
	        	else {System.out.print("   ");//otherwise pritns a space
	       
	        }
	      if(y==15) {System.out.println("");} //after 15 spaces/asterisks moves to new line
		
		       
			}
				
			}

	}//end main
		/**
		 * Provide the necessary logic to generate the co-prime 
		 * pairs from (1,1) to (m,n).
		 * 
		 * This will likely involve additional method(s)
		 */

//finds gcf of two numbers
public static int gcf(int x,int y) {
		   if (y==0) return x;
		   return gcf(y,x%y);  	   
		}//end gcf


//unused method to check if a number (less than 15) is prime

public static boolean isPrime(int x) {	  
	   		if(x == 1 || x==2||x==3) {return true;}
	   		if(x%2==0||x%3==0||x%4==0) {return false;}	
	
   			return true;
	   				
}//end isprime
	   	
	   
	   
	


}//end class
	
	
	


		
		
		
		
		
		
	
	


