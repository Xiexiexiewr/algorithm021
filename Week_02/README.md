### 一、哈希表、映射、集合  
** 哈希表（key-value：**增删查改O(1)、最坏是O(n)  
```set_x ={‘jack’, selina ’, ‘Andy'} ```  
```set_y = set([‘jack’, selina ’, ‘jack'])```  
** Map：**key-value对，key不重复  
** Set：**单个value，不重复元素的集合

### 二、堆和二叉树、二叉搜索树  
** 二叉树的遍历：**前序（根左右）、中序（左根右）、后序（左右根）O(logn)  

    def preorder(self, root):
        if root:  
            self.traverse_path.append(root.val)  
            self.preorder(root.left)  
            self.preorder(root.right) 
    
    def inorder(self, root):  
        if root:  
            self.inorder(root.left)  
            self.traverse_path.append(root.val)  
            self.preorder(root.right)  
    
    def postorder(self, root):  
        if root:  
            self.postorder(root.left)  
            self.postorder(root.right)  
            self.traverse_path.append(root.val)
  
** 二叉搜素树：**左子树上所有结点的值均小于它的根结点的值；右子树上所有结点的值均大于它的根结点的值；
 
### 三、堆和二叉堆
1.堆：分为大顶堆（大根堆）——根节点最大的堆，小顶堆（小根堆）——根节点最小的堆。  O(logn)  
2.二叉堆：通过完全二叉树来实现。1.一颗完全树；2.树中任意节点的值总是>=其子节点的值  
3.二叉堆的实现细节：    
    1.二叉堆一般都是通过“数组”来实现；    
    2.假设第一个元素索引为0，则父节点和子节点的位置关系如下：  
        * 索引为i的左孩子的索引(2i+1)；  
        * 索引为i的右孩子的索引(2i+2)；  
        * 索引为i的父结点的索引floor((i-1)/2)；  
4.插入操作（新元素插入到堆尾，依次向上调整 HeapifyUp）  
5.删除操作（堆尾替换堆顶，依次从根向下调整整个堆HeapifyDown）
