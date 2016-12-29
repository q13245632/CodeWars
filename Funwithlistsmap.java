//自己的解法
import java.util.function.Function;

class Solution {
	static <T, R> Node<R> map(Node<T> head, Function<T, R> f) {
		if (head == null) {
			return null;
		}
		R x = f.apply(head.data);
		Node<R> pNode = new Node<R>(x);
		Node<R> pHead = pNode;
		while (head.next != null) {
			R aR = f.apply(head.next.data);
			Node<R> node = new Node<R>(aR);
			pNode.next = node;
			head = head.next;
			pNode = pNode.next;
		}
		return pHead;
	}
}

//简化程序
import java.util.function.Function;

class Solution {
	static <T, R> Node<R> map(Node<T> head, Function<T, R> f) {
		return head == null ? null : new Node<R>(f.apply(head.data), map(head.next, f));
	}
}