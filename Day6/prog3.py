class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit=0;buy=0;sell=0
        i=0
        while(i<len(prices)-1):
            if prices[i]<prices[i+1]:
                buy=prices[i]
                sell=prices[i+1]
                profit+=sell-buy

                i+=1
            else:
                i+=1
        
        return profit

        


arr=[7,6,4,3,1]

res=Solution().maxProfit(arr)
print(res)