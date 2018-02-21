public class fizzBuzz{
	public static void main(String[] args){
		for(int i = 1; i <= 100; i++){
			StringBuilder fb = new StringBuilder();
			if(i % 15 == 0){
				fb.append("FizzBuzz");
			}
			else if(i % 3 == 0){ //because elegance is just out of my grasp
				fb.append("Fizz");
			}
			else if(i % 5 == 0){
				fb.append("Buzz");
			}
			else{
				System.out.println(i);
			}
			System.out.println(fb);
			System.out.println("\n");
		}
	}
}
