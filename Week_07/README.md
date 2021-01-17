## Week07 字典树和并查集
### 一、词频感应  
字典树，即 Trie 树，又称单词查找树或键树，是一种树形结构。典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。  
它的优点是：最大限度地减少无谓的字符串比较，查询效率比哈希表高。  
  
基本性质：  
1. 结点本身不存完整单词；  
2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串；  
3. 每个结点的所有子结点路径代表的字符都不相同。  

结点可以存储额外信息，比如单词频率  
  
核心思想：  
Trie 树的核心思想是空间换时间。  
利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。  
  
Python实现Trie树： 

    class Trie(object):
        def __init__(self):
            self.root = {}
            self.end_of_word = "#"
        def insert(self, word):
            node = self.root
            for char in word:
                node = node.setdefault(char, {})
            node[self.end_of_word] = self.end_of_word
        def search(self, word):
            node = self.root
            for char in word:
                if char not in node:
                    return False
                node = node[char]
            return self.end_of_word in node
        def startsWith(self, prefix):
            node = self.root
            for char in prefix:
                if char not in node:
                    return False
                node = node[char]
            return True
### 二、并查集（Disjoint Set）
基本操作：  
• makeSet(s)：建立一个新的并查集，其中包含 s 个单元素集合。  
• unionSet(x, y)：把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在的集合不相交，如果相交则不合并。  
• find(x)：找到元素 x 所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。  
Java实现：  

    class UnionFind {
        private int count = 0;
        private int[] parent;
        public UnionFind(int n) {
            count = n;
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }
        public int find(int p) {
            while (p != parent[p]) {
                parent[p] = parent[parent[p]];
                p = parent[p];
                }
                return p;
            }
        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ) return;
            parent[rootP] = rootQ;
            count--;
            }
        }
Python实现  

    def init(p):
        # for i = 0 .. n: p[i] = i
        p = [i for i in range(n)]
    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2
    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i: # 路径压缩 ?
            x = i; i = p[i];
            p[x] = root
        return root
### 三、高级搜索
初级搜索：  
1. 朴素搜索（暴力）  
2. 优化方式：不重复（fibonacci）、剪枝（生成括号问题）  
3. 搜索方向：  
        DFS: depth first search 深度优先搜索  
        BFS: breadth first search 广度优先搜索  
        双向搜索、启发式搜索  
  
回溯法：  
回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。  
回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：  
• 找到一个可能存在的正确的答案  
• 在尝试了所有可能的分步方法后宣告该问题没有答案  
在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。  
  
启发式搜索  
A* search    
    
    def AstarSearch(graph, start, end):
        pq = collections.priority_queue() # 优先级 —> 估价函数
        pq.append([start])
        visited.add(start)
        while pq:
            node = pq.pop() # can we add more intelligence here ?
            visited.add(node)
            process(node)
            nodes = generate_related_nodes(node)
            unvisited = [node for node in nodes if node not in visited]
            pq.push(unvisited)
 
