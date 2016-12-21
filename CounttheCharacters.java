public class CC {
 public static int charCount(String str, char c) {
		 int num = 0;
		 char[] arr = str.toLowerCase().toCharArray();
		 c = Character.toLowerCase(c);
		 for (int i = 0; i < arr.length; i++) {
			if (arr[i] == c) {
				num += 1;
			}
		}
		return num;
	}
}