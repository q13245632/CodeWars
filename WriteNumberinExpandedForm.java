//自己的解法
import java.util.ArrayList;
import java.util.List;
public class Kata {
	public static String expandedForm(int num) {
		char[] char_arr = String.valueOf(num).toCharArray();
		List<String> list = new ArrayList<>();
		String string = "";
		for (int i = 0; i < char_arr.length; i++) {
			String char_str = String.valueOf(char_arr[i]);
			int char_num = Integer.parseInt(char_str);
			if (char_num == 0) {
				continue;
			} else {
				list.add("" + (int)(char_num * Math.pow(10, char_arr.length - 1 - i)));
			}
		}
		for (int j = 0; j < list.size(); j++) {
			if (j != list.size() - 1) {
				string += list.get(j) + " + ";
			} else {
				string += list.get(j);
			}
		}
		return string;
	}
}

//思路不同
public class Kata
{
    public static String expandedForm(int num)
    {
      String st = "", zeros = "";
      
      while (num > 0){
        if (num % 10 != 0){
          st = " + " + num % 10 + zeros + st;        
        }
  
        zeros += "0";
        num = num / 10; 
      }
    
      return st.substring(3);
    }
}