public class Kata {
	public static char findMissingLetter(char[] array) {
		char a = ' ';
		for (int i = 1; i < array.length; i++) {
			if (array[i] - array[i-1] != 1) {
				a = (char) (array[i-1]+1);
			}
		}
		return a;
	}
}


import java.util.stream.IntStream;

public class Kata
{
  public static char findMissingLetter(char[] array)
  {
      int index = IntStream.range(0, array.length-1).filter(i -> array[i] != array[i+1]-1).findFirst().getAsInt();
      return (char)(array[index] + 1);
  }
}