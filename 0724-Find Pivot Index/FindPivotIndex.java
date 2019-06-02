class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        int i;
        for(i = 0 ;i<nums.length ;i++)
            sum+=nums[i];
        
        int sum2 = 0;
        for(i=0;i<nums.length;i++){
            if(sum-nums[i] == sum2) return i;
            sum2 += nums[i];
            sum -= nums[i];
        }
        return -1;
    }
}