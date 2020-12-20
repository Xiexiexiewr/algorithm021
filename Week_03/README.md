## Week03  
### 一、泛型递归和树的递归  
1.递归——循环：通过函数体来进行的循环（一层层下，再一层层返回，每一层的变量都是拷贝）
    
    def recursion(level, param1, param2, ...):
        #递归终止条件
        if level > MAX_LEVEL:
            prrocess_result
            return
       
        #处理当前层逻辑
        process(level, data...)
        
        #下探到下一层，标记当前是哪一层
        self.recursion(level + 1, p1, ...)
        
        #清理当前层（eg：全局变量） 
  
2.思维要点：a. ！不要人肉递归（可以在纸上先写出来）b.找最近最简重复子问题 c.数学归纳法思维  

### 二、分治、回溯  
1.分治代码模板  
    
    def  divide_conquer(problem, param1, param2, ...):
        #recursion terminator 到达叶子节点，子问题已经解决，没有问题要解决了
        if problem is None:
            print_result
            return
            
        # prepare data 
        data = prerare_data(problem)
        subproblems = split_problem(problem, data)
        
        #conquer subproblems下探到下一层
        subresult1 = self.divide_conquer(subproblems[0], p1, ...)
        subresult2 = self.divide_conquer(subproblems[1], p1, ...)
        subreault3 = self.divide_conquer(subproblems[2], p1, ...)
        ...
        
        #process and generate the final result把子结果合并
        result = process_result(subresult1, subresult2, subresult3, ...)
        
        # revert the current level states  
  
 2.回溯：典型问题：八皇后
