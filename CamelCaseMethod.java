//自己的解法
import java.util.*;
class Kata {
    static String camelCase(final String string) {
      String[] arr = string.split(" ");
      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < arr.length; i++) {
      if (arr[i].length() <= 0) {
        continue;
      }
      if (arr[i].length() == 1) {
        sb.append(arr[i]);
        continue;
      }
      sb.append(arr[i].substring(0, 1).toUpperCase()+arr[i].substring(1));
    }
      return sb.toString();
    }
}


//流处理
import static java.util.Arrays.stream;
import static java.util.stream.Collectors.joining;

class Kata {
    static String camelCase(final String string) {
        return stream(string.split(" "))
                .map(s -> s.length() > 1 ? s.substring(0, 1).toUpperCase() + s.substring(1) : s)
                .collect(joining(""));
    }
}