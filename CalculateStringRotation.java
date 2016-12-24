//自己的解法
public class CalculateRotation {
  static int shiftedDiff(String first, String second){
        int n = -1;
		int x = first.length();
		for (int i = 0; i < x; i++) {
			String string = first.substring(x - i) + first.substring(0, x - i);
			if (string.equals(second)) {
				n = i;
				break;
			}
		}
	    return n >= 0 ? n :-1 ;
  }
}

//测试集
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;


public class RotationTest {
    @Test
    public void test() {
      assertEquals(-1, CalculateRotation.shiftedDiff("hoop","pooh"));
      assertEquals(2, CalculateRotation.shiftedDiff("coffee","eecoff"));
      assertEquals(4, CalculateRotation.shiftedDiff("eecoff","coffee"));
    }
}

//其他解法
public class CalculateRotation {
  static int shiftedDiff(String first, String second){
    if (first.length() != second.length())
            return -1;
    return (second + second).indexOf(first);
  }
}