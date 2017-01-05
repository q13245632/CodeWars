import static java.lang.Math.abs;

import java.util.function.BiFunction;

public class Operarray {
    public static long gcdi(long x, long y) {
        return abs(y) == 0 ? abs(x) : gcdi(abs(y), abs(x) % abs(y));
    }
    public static long lcmu(long a, long b) {
        return abs(a) * abs(b) / gcdi(abs(a), abs(b));
    }
    public static long som(long a, long b) {
        return a + b;
    }
    public static long maxi(long a, long b) {
        return a > b ? a : b;
    }
    public static long mini(long a, long b) {
        return a < b ? a : b;
    }
    public static long[] operArray(BiFunction<Long, Long, Long> operator, long[] arr, long init) {
        long[] result = new long[arr.length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = operator.apply(i - 1 < 0 ? init : result[i - 1], arr[i]);
        }
        return result;
    }
}