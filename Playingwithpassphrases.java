//自己的解法
public class PlayPass {
	public static String playPass(String s, int n) {
		String string = s.toUpperCase();
		String str = "";
		for (int i = string.length() - 1; i >= 0; i--) {
			if ('A'<=string.charAt(i)&&string.charAt(i)<='Z') {
				if (string.charAt(i) + n > 'Z') {
					char a = (char) (string.charAt(i) + n - 26);
					if (i % 2 == 0) {
						str += a;
					} else {
						str += (char)(a + 32);
					}
				} else {
					if (i % 2 == 0) {
						str += (char)(string.charAt(i) + n);
					} else {
						str += (char)(string.charAt(i) + n + 32);;
					}
				}
			} else if ('0'<=string.charAt(i)&&string.charAt(i)<='9') {
				str += (char) (105 - string.charAt(i));
			} else {
				str += (char) string.charAt(i);
			}

		}
		return str;
	}
}

//测试集
import static org.junit.Assert.*;

import org.junit.Test;


public class PlayPassTest {

	@Test
	public void test1() {
		assertEquals("!!!vPz fWpM J", PlayPass.playPass("I LOVE YOU!!!", 1));
	}

	@Test
	public void test4() {
		assertEquals("4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO",
		             PlayPass.playPass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2));
	}

}


import java.util.stream.Collectors;

public class PlayPass {
    private static int count = 0;

    public static String playPass(final String s, final int n) {
        count = 0;
        
        return new StringBuilder()
                .append(
                        s.toUpperCase()
                                .chars()
                                .map(i -> Character.isDigit(i) ? 57 - Character.getNumericValue(i) : i)
                                .mapToObj(c -> (char) c)
                                .map(c -> (c <= 90 && c >= 65) ? (char) (c + (n % 26)) : c)
                                .map(c -> c > 90 ? (char) ((c % 91) + 65) : c)
                                .map(i -> i.toString())
                                .map(i -> (count++ % 2) == 0 ? i.toUpperCase() : i.toLowerCase())
                                .collect(Collectors.joining("")))
                .reverse()
                .toString();
    }
}