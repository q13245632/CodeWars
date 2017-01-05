//自己的解法
class StepInPrimes {

	public static long[] step(int g, long m, long n) {
		System.out.println(g + "+"+m+"+"+n);
		if (g + m >= n) {
			return null;
		}
		long[] arr = new long[2];
		for (long i = m; i <= n; i++) {
			if (i+g <= n && isPrime(i) && isPrime(i + g)) {
				arr[0] = i;
				arr[1] = i + g;
				break;
			}
		}
		if (arr[0] == 0 && arr[1] == 0) {
			return null;
		}
		return arr;
	}
	public static boolean isPrime(long a) {
		for (int i = 2; i < ((int)Math.sqrt(a) + 1); i++) {
			if (a % i == 0) {
				return false;
			}
		}

		return true;
	}
}
//测试集
import static org.junit.Assert.*;
import java.util.Arrays;
import org.junit.Test;

public class StepInPrimesTest {

	@Test
	public void test() {
		System.out.println("Fixed Tests");
		assertEquals("[101, 103]", Arrays.toString(StepInPrimes.step(2,100,110)));
		assertEquals("[103, 107]", Arrays.toString(StepInPrimes.step(4,100,110)));
		assertEquals("[101, 107]", Arrays.toString(StepInPrimes.step(6,100,110)));
		assertEquals("[359, 367]", Arrays.toString(StepInPrimes.step(8,300,400)));
		assertEquals("[307, 317]", Arrays.toString(StepInPrimes.step(10,300,400)));
	}

}

//
import java.util.HashSet;
import java.util.OptionalLong;
import java.util.stream.LongStream;

class StepInPrimes {

	private static HashSet<Long> primes = new HashSet<>();

	public static long[] step(int stepLength, long start, long end) {
		OptionalLong smallerPrime = LongStream.rangeClosed(start, end).filter(i -> isPrime(i) && isPrime(i+stepLength)).findFirst();
		return smallerPrime.isPresent()
		       ? new long[] {smallerPrime.getAsLong(), smallerPrime.getAsLong()+stepLength}
		       : null;
	}

	private static boolean isPrime(long primeCandidate) {
		if(primes.contains(primeCandidate))
			return true;

		for(long i=2; i<Math.sqrt(primeCandidate)+1; i++) {
			if(primeCandidate%i == 0)
				return false;
		}

		primes.add(primeCandidate);
		return true;
	}
}