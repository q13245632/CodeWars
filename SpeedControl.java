public static int gps(int s, double[] x) {
	        // your code
		 if (x.length <= 1) {
			return 0;
		}
		 double max = x[1] - x[0];
		 for (int i = 1; i < x.length - 1; i++) {
			double m = x[i+1] - x[i];
			if (m > max) {
				max = m;
			}
		}
		 int speed = (int) (max * 3600 / s);
		 return speed;
	  }

/***
测试例子
import static org.junit.Assert.*;
import org.junit.Test;


public class GpsSpeedTest {
    
    private static void testing(long actual, long expected) {
        assertEquals(expected, actual);
    }
    
    @Test
    public void test1() {
        System.out.println("Fixed Tests: gps"); 
        double[] x = new double[] {0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61};
        testing(GpsSpeed.gps(20, x), 41);
        x = new double[] {0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25};
        testing(GpsSpeed.gps(12, x), 219);
        x = new double[] {0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36, 3.6, 3.84};
        testing(GpsSpeed.gps(20, x), 80);
    }
}
*/

//流处理
import java.util.*;
import java.util.stream.*;

public class GpsSpeed {
    
    public static int gps(int s, double[] x) {
        double maxSpeed = IntStream
          .range(0, x.length - 1)
          .mapToDouble(i -> (x[i+1] - x[i]) * 3600.0 / (double) s )
          .max().orElse(0.0);
        return (int) Math.floor(maxSpeed);
    }
}


import java.util.stream.IntStream;

public class GpsSpeed {
    
    public static int gps(int s, double[] x) {      
      return x.length <= 1 ? 0 : (int) Math.floor(IntStream.range(1, x.length)
                                                           .mapToDouble(i -> x[i] - x[i-1])
                                                           .map(i -> i * 3600.0/s)
                                                           .max()
                                                           .getAsDouble());
    }
}