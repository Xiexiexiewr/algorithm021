## Week09 高级动态规划
动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构）  
拥有共性：找到重复子问题  
差异性：最优子结构、中途可以淘汰次优解  
  
递归 - 函数自己调用自己  

    public void recur(int level, int param) {
        // terminator
        if (level > MAX_LEVEL) {
            // process result
            return;
        }
        // process current logic
        process(level, param);
        // drill down
        recur(level: level + 1, newParam);
        // restore current status
    }

分治代码模板

    def divide_conquer(problem, param1, param2, ...):
        #recursion terminator
        if problem is None:
            print_result
            return
        #prepare data
        data = prepare_data(problem)
        subproblems = split_problem(problem, data)
        #conquer subproblems
        subresult1 = self.divide_conquer(subproblems[0], p1, ...)
        subresult2 = self.divide_conquer(subproblems[1], p1, ...)
        subresult3 = self.divide_conquer(subproblems[2], p1, ...)
        …
        #process and generate the final result
        result = process_result(subresult1, subresult2, subresult3, …)
        #revert the current level states
    
动态规划 Dynamic Programming  
1. “Simplifying a complicated problem by breaking it down into  
    simpler sub-problems”  
    (in a recursive manner)  
2. Divide & Conquer + Optimal substructure  
                            分治 + 最优子结构  
3. 顺推形式： 动态递推  
DP 顺推模板  
   
    function DP():
        dp = [][] # ⼆维情况
        for i = 0 .. M {
            for j = 0 .. N {
                dp[i][j] = _Function(dp[i’][j’]…)
            }
        }
        return dp[M][N];

常见的 DP 题目和状态方程  
1.爬楼梯   递归公式：f(n) = f(n - 1) + f(n - 2) , f(1) = 1, f(0) = 0   
2.不同路径   递归公式：f(x, y) = f(x-1, y) + f(x, y-1)  
3.打家劫舍  
4.最小路径和  
5.股票买卖  


