//自己的解法
import java.util.ArrayList;
import java.util.List;
public class Kata {
	public static int getLengthOfMissingArray(Object[][] arrayOfArrays) {
		if (arrayOfArrays == null||arrayOfArrays.length == 0) {
			return 0;
		} else {
			List<Integer> list = new ArrayList<>();
			for (int i = 0; i < arrayOfArrays.length; i++) {
				if (arrayOfArrays[i] == null || arrayOfArrays[i].length == 0) {
					return 0;
				} else {
					list.add(arrayOfArrays[i].length);
				}
			}
			list.sort((a, b) -> a.compareTo(b));
			for (int i = 1; i < list.size(); i++) {
				if (list.get(i) - list.get(i - 1) != 1) {
					return list.get(i) - 1;
				}
			}
		}
		return 0;
	}
}

//测试集
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class KataTests {
	@Test
	public void BasicTests() {
		assertEquals(3, Kata.getLengthOfMissingArray(new Object[][] { new Object[] { 1, 2 }, new Object[] { 4, 5, 1, 1 }, new Object[] { 1 }, new Object[] { 5, 6, 7, 8, 9 }} ));
		assertEquals(2, Kata.getLengthOfMissingArray(new Object[][] { new Object[] { 5, 2, 9 }, new Object[] { 4, 5, 1, 1 }, new Object[] { 1 }, new Object[] { 5, 6, 7, 8, 9 }} ));
		assertEquals(2, Kata.getLengthOfMissingArray(new Object[][] { new Object[] { null }, new Object[] { null, null, null } } ));
		assertEquals(5, Kata.getLengthOfMissingArray(new Object[][] { new Object[] { 'a', 'a', 'a' }, new Object[] { 'a', 'a' }, new Object[] { 'a', 'a', 'a', 'a' }, new Object[] { 'a' }, new Object[] { 'a', 'a', 'a', 'a', 'a', 'a' }} ));
		assertEquals(0, Kata.getLengthOfMissingArray(new Object[][] { }));
		new Object[][] {new Object[]{1, 3, 2, 4, 5},new Object[]{2, 1},new Object[]{},new Object[]{0},new Object[]{3,2,2}}
	}
}


import java.util.Arrays;
import java.util.List;
import java.util.OptionalInt;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Kata
{
    public static int getLengthOfMissingArray(Object[][] arrayOfArrays)
    {
        if(arrayOfArrays == null)
            return 0;
        
        List<Integer> lengthsSorted = Arrays.stream(arrayOfArrays)
                .filter(array -> array != null && array.length != 0)
                .mapToInt(array -> array.length)
                .sorted()
                .boxed()
                .collect(Collectors.toList());
        
        if(lengthsSorted.size() != arrayOfArrays.length)
            return 0;
        
        OptionalInt indexOfLastCorrect = 
                IntStream.range(0, lengthsSorted.size()-1)
                        .filter(i -> lengthsSorted.get(i)+1 != lengthsSorted.get(i+1))
                        .findFirst();

        return indexOfLastCorrect.isPresent() 
                ? lengthsSorted.get(indexOfLastCorrect.getAsInt())+1 
                : 0;
    }
}