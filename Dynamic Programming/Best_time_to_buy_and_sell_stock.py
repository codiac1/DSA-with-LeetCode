class Solution:
    def buy(self ,prices  , index):
        if index == len(prices)-1:
            return 0
        return max(self.sell(prices,index +1) - prices[index] , self.buy(prices,index+1))
        
    def sell(self, prices , index):
        if index == len(prices)-1:
            return prices[index]
        if self.g[index] != -1:
            return self.g[index]
        
        self.g[index] = max(self.sell(prices , index+1) , prices[index])
        return self.g[index]
    def maxProfit(self, prices: List[int]) -> int:
        self.g = [-1]*(len(prices)+1)
        return self.buy(prices , 0)
            
                
