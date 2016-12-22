//自己的解法
public static String longest (String s1, String s2) {
	        // your code
		 List<Character> list = new ArrayList<>();
		 String string = s1 + s2;
		 char[] c1 = string.toCharArray();
		 for (int i = 0; i < c1.length; i++) {
			if (list.contains(c1[i])) {
				list.add(c1[i]);
			}
		}
		 list.sort(new Comparator<Character>() {
			 @Override
			public int compare(Character o1, Character o2) {
				// TODO Auto-generated method stub
				 if (o1 - o2 > 0) {
					return 1;
				} else if (o1 - o2 < 0) {
					return -1;
				} else {
					return 0;
				}
			}
		});
		 String str = "";
		 for (int i = 0; i < list.size(); i++) {
			str += list.get(i).toString();
		}
		 return str;
	    }
        
 
/**
import static org.junit.Assert.*;
import org.junit.Test;

public class TwoToOneTest {

    @Test
    public void test() {
        System.out.println("longest Fixed Tests");
        assertEquals("aehrsty", TwoToOne.longest("aretheyhere", "yestheyarehere"));
        assertEquals("abcdefghilnoprstu", TwoToOne.longest("loopingisfunbutdangerous", "lessdangerousthancoding"));
        assertEquals("acefghilmnoprstuy", TwoToOne.longest("inmanylanguages", "theresapairoffunctions"));
    }
}
**/
//程序简化
public class TwoToOne {
    
    public static String longest (String s1, String s2) {
        String s = s1 + s2;
        return s.chars().distinct().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
    }
}


import java.util.stream.*;
import java.util.*;

public class TwoToOne {
    
    public static String longest (String s1, String s2) {
        String[] input = {s1, s2};
        return Stream.of(s1+s2)
                  .map(w -> w.split(""))
                  .flatMap(Arrays::stream)
                  .distinct()
                  .sorted()
                  .collect(Collectors.joining());
    }
}