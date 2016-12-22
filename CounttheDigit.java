//自己的解法
public static int nbDig(int n, int d) {
	        // your code
		 int num = 0;
		 for (int i = 0; i <= n; i++) {
			 int x = i * i;
			 String c = String.valueOf(d); 
			 String string = String.valueOf(x);
			 for (int j = 0; j < string.length(); j++) {
				if (string.substring(j, j+1).equals(c)) {
					num += 1;
				}
			}
		}
		 return num;
	}
 
//流处理
import java.util.stream.IntStream;

public class CountDig {

    public static int nbDig(int n, int d) {

         return (int) IntStream
               .rangeClosed(0, n)
               .map(i -> i * i)
               .flatMap(i -> String.valueOf(i).chars())
               .mapToObj(i -> (char)i)
               .mapToInt(Character::getNumericValue)
               .filter(i -> i == d)
               .count();
    }
}


/**
import static org.junit.Assert.*;

import org.junit.Test;


public class CountDigTest {
    private static void testing(int actual, int expected) {
        assertEquals(expected, actual);
    }
    @Test
    public void test() {
        System.out.println("Fixed Tests nbDig");
        testing(CountDig.nbDig(5750, 0), 4700);
        testing(CountDig.nbDig(11011, 2), 9481);
        testing(CountDig.nbDig(12224, 8), 7733);
        testing(CountDig.nbDig(11549, 1), 11905);       
    }
}
**/