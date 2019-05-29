class Solution {
    public int maxProfit(int[] prices) {
        int i, j;
        int minPrice = 0;
        int profit = 0;
        if(prices.length>0) minPrice = prices[0];
        for(i=1;i<prices.length;i++){
            if(prices[i]<minPrice){
                minPrice = prices[i];
            }
            if(prices[i]-minPrice > profit){
                profit = prices[i]-minPrice;
            }
        }
        return profit;
    }
}