class Solution {
    public int removeDuplicates(int[] nums) {
        int i;
        int index = 0;
        for(i = 0;i<nums.length;i++){
        	if(nums[index] != nums[i]){
        		index++; 
        		nums[index] = nums[i];
        	}
        }
    	return index+1;
    }
}
public class RemoveDuplicatesfromSortedArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {0,0,1,1,1,2,2,3,3,4};
		Solution solution = new Solution();
	}
}
