public class TreeNode {

    TreeNode left;
    TreeNode right;

    public static boolean isPerfect(TreeNode root) {
        if(checkHeight(root) == -1) {  
            return false;  
        }  
        else {  
            return true;  
        }  
    }
    
    public static int checkHeight(TreeNode root) {  
        if (null == root) return 0;  
        int leftHeight = checkHeight(root.left);  
        if ( leftHeight == -1 ) {  
            return -1; //unbalanced  
        }  
          
        int rightHeight = checkHeight(root.right);  
        if ( rightHeight == -1 ) {  
            return -1; //unbalanced  
        }  
          
        int heightDiff = leftHeight - rightHeight;  
        if (Math.abs(heightDiff) > 0) {  
            return -1; // unbalanced  
        }  
        else {  
            return Math.max( rightHeight, rightHeight + 1 );  
        }  
    }  
    
    static TreeNode leaf() {
        return new TreeNode();
    }

    static TreeNode join(TreeNode left, TreeNode right) {
        return new TreeNode().withChildren(left, right);
    }

    TreeNode withLeft(TreeNode left) {
        this.left = left;
        return this;
    }

    TreeNode withRight(TreeNode right) {
        this.right = right;
        return this;
    }

    TreeNode withChildren(TreeNode left, TreeNode right) {
        this.left = left;
        this.right = right;
        return this;
    }

    TreeNode withLeftLeaf() {
        return withLeft(leaf());
    }

    TreeNode withRightLeaf() {
        return withRight(leaf());
    }

    TreeNode withLeaves() {
        return withChildren(leaf(), leaf());
    }
}





public class TreeNode {

    TreeNode left;
    TreeNode right;

    public static boolean isPerfect(TreeNode root) {
      if (root == null) { return true; }
      
      if (root.left == null && root.right == null) {
        return true;
      }
      
      if (root.left != null && root.right != null) {
        return isPerfect(root.left) && isPerfect(root.right) && maxDepth(root.left) == maxDepth(root.right);
      }
      
      return false;
    }
    
    static int maxDepth(TreeNode root) {
      if (root == null) { return 0; }
      
      return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
    
    static TreeNode leaf() {
        return new TreeNode();
    }

    static TreeNode join(TreeNode left, TreeNode right) {
        return new TreeNode().withChildren(left, right);
    }

    TreeNode withLeft(TreeNode left) {
        this.left = left;
        return this;
    }

    TreeNode withRight(TreeNode right) {
        this.right = right;
        return this;
    }

    TreeNode withChildren(TreeNode left, TreeNode right) {
        this.left = left;
        this.right = right;
        return this;
    }

    TreeNode withLeftLeaf() {
        return withLeft(leaf());
    }

    TreeNode withRightLeaf() {
        return withRight(leaf());
    }

    TreeNode withLeaves() {
        return withChildren(leaf(), leaf());
    }
}