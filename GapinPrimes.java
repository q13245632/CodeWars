import java.util.Arrays;

class GapInPrimes {

	public static long[] gap(int g, long m, long n) {
		System.out.println(g + " " + m + " " + n );
		// your code
		long[] arr = new long[2];
		for (long i = m; i <= n - g; i ++) {
			if (isPeimr(i) && isPeimr(i + g)) {
				boolean isAll = true;
				long j = i + 1;
				while (j < i + g) {
					if (isPeimr(j)) {
						isAll = false;
					}
					j ++;
				}
				if (isAll) {

					arr[0] = i;
					arr[1] = i + g;
					break;
				}
			}
		}
		return arr[0] == 0 ? null : arr;
	}
	private static boolean isPeimr(long n) {
		boolean isPrime = true;
		for (long i = 2; i < (int) Math.sqrt(n) + 1; i++) {
			if (n % i == 0) {
				isPrime = false;
				break;
			}
		}
		return isPrime;
	}
}



import java.math.BigInteger;
import java.util.stream.LongStream;

class GapInPrimes {
  public static long[] gap(long g, long m, long n) {
    return LongStream.iterate(m % 2 == 0 ? m + 1 : m, l -> l + 2).limit((n - m) / 2).filter(l -> BigInteger.valueOf(l).isProbablePrime(5) && BigInteger.valueOf(l + g).isProbablePrime(5)).filter(l -> {
      return LongStream.iterate(l + 2, c -> c + 2).limit((g - 2) / 2).parallel().filter(c -> BigInteger.valueOf(c).isProbablePrime(5)).mapToObj(c -> false).findAny().orElse(true);
    }).mapToObj(l -> new long[]{l, l + g}).findFirst().orElse(null);
  }
}
