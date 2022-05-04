class Solution: 
    def buy(self , prices , day):
        if day == len(prices):
            return 0
        if self.buy_state[day] != -1:
            return self.buy_state[day]
        
        self.buy_state[day] = max(self.buy(prices , day+1) , self.sell(prices , day)-prices[day])
        return self.buy_state[day]
    
    def sell(self , prices , day):
        if day == len(prices)-1:
            return prices[day]
        if self.sell_state[day] != -1:
            return self.sell_state[day]
        
        self.sell_state[day] = max(self.sell(prices , day+1) , prices[day]+ self.buy(prices , day+1))
        return self.sell_state[day]
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        self.buy_state = [-1]*(n+1)
        self.sell_state = [-1]*(n+1)
        return self.buy(prices , 0)
