import java.util.ArrayList;
import java.util.Arrays;

public class KPrimes {
  public static long[] countKprimes(int k, long start, long end) {
    ArrayList<Long> longList = new ArrayList<>();

    if (start == 0){
      start += 1;
    }

    for (long n = start ; n <= end; n++) {
      ArrayList<Integer> intList = new ArrayList<>();
      long i = n;
      while (i % 2 == 0) {
        intList.add(2);
        if (intList.size() > k){
          break;
        }
        i /= 2;
      }

      for (int y = 3; y <= Math.sqrt(i); y += 2) {
        while (i % y == 0) {
          intList.add(y);
          if (intList.size() > k){
            break;
          }
          i /= y;
        }
      }

      if (i > 2) {
        intList.add((int)i);
      }

      if (intList.size() == k){
        longList.add(n);
      }
    }

    long[] longlist = new long[longList.size()];
    int count = 0;

    for (Long num : longList){
      longlist[count] = num;
      count += 1;
    }


    return longlist;
  }

  public static int puzzle(int s) {
    long[] aList = countKprimes(1, 0, s);
    long[] bList = countKprimes(3, 8, s);
    long[] cList = countKprimes(7, 128, s);

    if (s < 138) {
      return 0;
    } else if (s == 138){
      return 1;
    }
    
    int count = 0;
    
    for (long a : aList){
      for (long b : bList) {
        for (long c : cList) {
          if (a + b + c == s){
            count += 1;
          }
        }
      }
    }
    
    return count;
  }
}



import java.util.stream.LongStream;

public class KPrimes {
    
    public static long[] countKprimes(int k, long start, long end) {
        return LongStream.rangeClosed(start, end)
            .filter(n -> findK(n) == k)
            .toArray();
    }
    
    public static int puzzle(long s) {
      int count = 0;

      for (long c : countKprimes(1, 1, s)) {
        for (long b : countKprimes(3, 1, s)) {
          for (long a : countKprimes(7, 1, s)) {
            if (a + b + c > s) {
              break;
            }
            if (a + b + c == s) {
              count++;
            }
          }
        }
      }
      
      return count;
    }
    
    private static long findK(long n) {
      int myK = 0;
      
      // Deal with zero
      if (n == 0) {
        return 0;
      }

    // Factor out all twos
    if (n % 2 == 0) {
      myK++;
      n = n / 2;
      while (n % 2 == 0) {
        myK++;
        n = n / 2;
      }
    }

    // Factor out other primes
    long factor = 3;
    while (Math.abs(n) > 1 && factor <= Math.sqrt(n)) {
      if (n % factor == 0) {
        myK++;
        n = n / factor;
        while (n % factor == 0) {
          myK++;
          n = n / factor;
        }
      }
      factor += 2;
    }

    // number is prime
    if (n != 1) {
      myK++;
    }
      
      return myK;
    }

}