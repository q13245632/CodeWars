//自己的解法
public static long digPow(int n, int p) {
		String string = String.valueOf(n);
		char[] c = string.toCharArray();
		int x = p;
		double sum = 0D;
		for (int i = 0; i < c.length; i++) {
			System.out.println(c[i]);
			sum = sum + Math.pow(Double.valueOf(String.valueOf(c[i])), (double) x);
			System.out.println(sum);
			x ++;
		}
		long d = -1;
		if ((int) sum % n == 0) {
			d = (long) (sum / n);
		}
			// your code
	    return d;
	}


//测试集
// digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
// digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
// digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
// digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

//简化程序
public class DigPow {
  
  public static long digPow(int n, int p) {
    String intString = String.valueOf(n);
    long sum = 0;
    for (int i = 0; i < intString.length(); ++i, ++p)
      sum += Math.pow(Character.getNumericValue(intString.charAt(i)), p);
    return (sum % n == 0) ? sum / n : -1;
  }
  
}
