public class Solution {
	public static String[] streetFighterSelection(String[][] fighters, int[] position, String[] moves) {
		int len = moves.length;
		String[] arr = new String[len];
		int x = position[0];
		int y = position[1];
		for (int i = 0; i < len; i++) {
			switch (moves[i]) {
			case "up":
				if (x == 0) {
					arr[i] = fighters[x][y];
				} else {
					x = x - 1;
					arr[i] = fighters[x][y];
				}
				break;
			case "down":
				if (x == 1) {
					arr[i] = fighters[x][y];
				} else {
					x = x + 1;
					arr[i] = fighters[x][y];
				}
				break;
			case "left":
				if (y == 0) {
					y = 5 % 6;
					arr[i] = fighters[x][y];
				} else {
					y = y - 1;
					arr[i] = fighters[x][y];
				}
				break;
			case "right":
				if (y == 5) {
					y = 0;
					arr[i] = fighters[x][y];
				} else {
					y = y + 1;
					arr[i] = fighters[x][y];
				}
				break;
			}
		}
		return arr;
	}
}