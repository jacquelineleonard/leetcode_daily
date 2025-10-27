//jacks  Solution
class Solution1 {
    public int[] twoSum(int[] nums, int target) 
    {
        int k=0,l=0;
        for(int i=0;i<nums.length;i++)
        {
            for(int j=i+1;j<nums.length;j++)
            {
                if(i!=j)
                if(nums[i]+nums[j]==target)
                return new int[] {i,j};
            }
        }
        return new int[] {};
    }  
}
//Best Solution
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for(int i = 1;i<n;i++){
            for(int j = i;j<n;j++){
                if(nums[j-i] + nums [j] == target){
                    return new int[]{j-i,j};
                }
            }
        }
        return new int[]{};
    }
}