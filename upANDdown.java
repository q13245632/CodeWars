class Updown {
	public static String arrange(String string) {
		String[] arr = string.split(" ");
		for (int i = 1; i < arr.length; i += 2) {
			if (arr[i].length() < arr[i-1].length()) {
				String temp = arr[i-1];
				arr[i-1] = arr[i];
				arr[i] = temp;
			}
			if (i + 1 < arr.length && arr[i].length() < arr[i+1].length()) {
				String temp2 = arr[i+1];
				arr[i+1] = arr[i];
				arr[i] = temp2;
			}
		}
		String str = "";
		for (int i = 0; i < arr.length; i++) {
			arr[i] = arr[i].toLowerCase();
			if (i != arr.length-1 && i % 2 != 0) {
				str += arr[i].toUpperCase() + " ";
			} else if (i != arr.length-1 && i % 2 == 0) {
				str += arr[i] + " ";
			} else if (i == arr.length - 1 && i % 2 != 0) {
				str += arr[i].toUpperCase();
			} else {
				str += arr[i];
			}
		}
		return str;
	}
}