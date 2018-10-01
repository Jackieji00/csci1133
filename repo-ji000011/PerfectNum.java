import java.util.Scanner;
public class PerfectNum{
  public static void main(String[] args){
    int limit;
    int n = 1;

    Scanner in = new Scanner(System.in);

    System.out.print("Enter the upper limit: ");
    limit = in.nextInt();
    while (n <= limit){
      int i = 1;
      int factorsum = 0;
      while(i<n){
        if(n%i == 0){
          factorsum += i;
        }
        i += 1;
      }
      if (factorsum == n){
        System.out.println(n+" is a perfect number!");
      }
      n+=1;
    }
  }
}
