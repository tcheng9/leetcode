'''
0. Question notes:
-----------------------------------------------
? notes:
1. Given an array of stock prices
Maximize the day you buy a stock and sell a stock
Return max profit
If you can't return any profit, return 0


'''


'''
I. Conceptual Solution
-----------------------------------------------
Constraints:
1. Time is linear, you only buy on ith day and can only sell on arr[i+1:]


My thoughts:
implmenet 2 pointer solution
Calc max(overall_profit, potential_profit)
return max profit

-> If profit never exceeds 0, it can be handled in the based case

'''



'''
II. Implementation
-----------------------------------------------
left = 0
        right = 0
        res = 0

        for i in range(len(prices)-1):
            
            right = i
            while right < len(prices):
                
                
                
                profit = prices[right] - prices[left]
                
                res = max(profit, res)
                right += 1
              
            left += 1
        
        return res



ISSUE: Not efficient enough
'''



'''
III. Code solutions
-----------------------------------------------
'''


'''
IV. Summary
-----------------------------------------------
'''
