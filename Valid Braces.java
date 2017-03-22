import java.util.Stack;

public class BraceChecker {
  
  public boolean isValid(String braces) {
    Stack<Character> s = new Stack<>();
    for (char c : braces.toCharArray()) 
      if (s.size() > 0 && isClosing(s.peek(), c)) s.pop(); 
      else s.push(c);
    return s.size() == 0;
  }
  
  public boolean isClosing(char x, char c) {
    return (x == '{' && c == '}') || (x == '(' && c == ')') || (x == '[' && c == ']');
  }
  
}


public static boolean isValid(String braces) {
		char[] arr = braces.toCharArray();
		System.out.println(arr.length);
		Stack<Character> stack = new Stack<>();
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == '(' || arr[i] == '[' || arr[i] == '{') {
				stack.push(arr[i]);
				System.out.println("++");
				continue;
			}
			if (arr[i] == ')' && !stack.isEmpty() && stack.peek() == '(') {
				System.out.println("--");
				stack.pop();
				continue;
			}
			if (arr[i] == ']' && !stack.isEmpty() && stack.peek() == '[') {
				stack.pop();
				continue;
			}
			if (arr[i] == '}' && !stack.isEmpty() && stack.peek() == '{') {
				stack.pop();
				continue;
			}
			return false;
		}
		return stack.isEmpty();
	}