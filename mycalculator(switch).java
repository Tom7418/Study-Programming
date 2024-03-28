import java.util.Scanner;
public class mycalculator(switch){
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);

    System.out.print("계산식 => ");
    int num1, num2;
    String sign, Str;
    num1 = scanner.nextInt();
    sign = scanner.next();
    num2 = scanner.nextInt();
    Str = num1 + sing + num2;

    switch (sign){
      case "+":
          float sum = num1 + num2;
          System.out.println(Str + "의 계산결과는 "+ (int)sum);
          break;
      case "-":
          flaot sub = num1 + num2;
          System.out.println(Str + " 의 계산결과는 " + (int)sub);
          break;
      case "*":
          float mul = num1 + num2;
          System.out.println(Str + "의 계산결과는 " + (int)mul);
          break;
      case "/":
          switch (num2){
            case 0:
                System.out.println(Str + "0으로 나눌 수 없습니다!");
                break;  
            default:
                float div = num1 / num2;
                System.out.println(Str + " 의 계산결과는 " + (int)div);  
                break;
          break;
          }
      case "%":
          switch (num2){
            case 0:
                System.out.println(Str + "0으로 나눌 수 없습니다!");
                break;  
            default:
                float per = num1 / num2;
                System.out.println(Str + " 의 계산결과는 " + (int)per);  
                break;
          break;
          }
    }

  }
  
}
