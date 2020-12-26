## Week04 BFS、DFS、贪心、二分  
### 一、深度优先搜索和广度优先搜索  
1.深度优先（DFS）：相邻节点（栈）  
基础模板：

    def dfs(node):
    if node in visited:
        # already visited
        return
        
       visited.add(node)
       
       # process current node
       # ... # logic here
       dfs(node.left)
       dfs(node.right)
非递归：  
    
    def DFS(self, tree):
    if tree.root is None:
        return []
        
    visited, stack = [], [tree.root]
    
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
        #other processing work  
        ...
 递归：
 
    visited = set()
    def dfs(node, visited):
    if node in visited:   #terminator
    #already visited
    return
    
    visited.add(node)
    
    #process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
 
 2.广度优先（BFS）：一层一层向下（队列---python数组）
    
    def BFS(graph, start, end):
        queue = []
        queue.append([start])
        visited.add(start)
    
        while queue:
            node = queue.pop()
            visited.add(node)
        
            process(node)
            nodes = generate_ralated_nodes(node)
            queue.push(nodes)
        # other processing work
        ...
### 二、贪心算法  
  贪心算法是在每一种在每一步选择中都采取当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。）  
  贪心和动态规划的区别：  
  贪心：当下做局部最优判断，不能回退  
  动规：保存之前的运算结果，最有判断+回退  
  贪心例子：求图中最小生成树、求哈夫曼编码
  
### 三、二分查找  
  1.目标函数单调性（单调递增或者递减）  
  2.存在上下界（bounded）  
  3.能通过索引访问（index accessible）  
    
    left, right = 0, len(array) - 1
    while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # find the target!!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
