import java.util.LinkedList;

public class RemovedNumbers {
  /*
  We desire: ab = 1 + ... + n - a - b
  Take advantage of b = sum - a
                        -------
                         a + 1
  */
  public static LinkedList<long[]> removNb(long n) {
    LinkedList<long[]> numbers = new LinkedList<long[]>();
    long sum = (n * n + n) / 2;
    for (long a = 1; a < n; a++) {
      double b = (sum - a) / (double) (a + 1);
      if (b <= n && b % 1 == 0) {
        numbers.add(new long[] {a, (long) b});
      }
    }
    return numbers;
  }
}



import java.util.*;
public class RemovedNumbers {
    
    public static List<long[]> removNb(long n) {
		long sum = n*(n+1);
		List<long[]> list = new ArrayList<>();
		for (int i = 1; i <= n; i++) {
			System.out.println(i + "+++" + (sum-2*i)%(2*(i+1)));
			if ((sum-2*i)%(2*(i+1)) == 0 && (sum-2*i)/(2*(i+1)) >=1 && (sum-2*i)/(2*(i+1)) <=n) {
				System.out.println(i + "+++" + (sum-2*i)/(2*(i+1)));
				long[] arr = new long[]{i,(sum-2*i)/(2*(i+1))};
				list.add(arr);
			}
		}
		return list;
	}    

}