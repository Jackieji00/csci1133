import java.util.Scanner;
import java.util.ArrayList;
public class ConvertRoman{
  public static int convertDigit(char letter){
    String digits = new String("IVXLCDM");
    int[] values = {1,5,10,50,100,500,1000};
    int i = 0;
    while(i< digits.length()&& letter != digits.charAt(i)){
      i += 1;
      if(i< digits.length()){
        return values[i];
      }
    }
    return 0;
  }
  public static int convertRoman(String istr){
    int lastvalue = 0;
    int decimalval = 0;
    char[] ch = istr.toCharArray();
    for(char l:ch){
      int currentvalue = convertDigit(l);
      if(lastvalue< currentvalue){
        decimalval -= lastvalue;
      }else{
        decimalval += lastvalue;
      }
      lastvalue = currentvalue;
    }
    return decimalval + lastvalue;
  }
  public static void main(String[] args){
    boolean done = false;
    while(!done){
      Scanner in = new Scanner(System.in);
      System.out.print("Enter a Roman Numeral as a string: ");
      String romannumeral = in.nextLine();
      if (romannumeral.length()== 0){
        done = true;
      }else{
        System.out.println("Decimal value: "+Integer.toString(convertRoman(romannumeral)));
      }
    }
  }
}
