//jacks code
class Solution {
    public int removeDuplicates(int[] nums) {
        int index=0,i;
        for(i=0;i<nums.length-1;i++)
        {
            if(nums[i]!=nums[i+1])
            nums[index++]=nums[i];
        }
        nums[index++]=nums[nums.length-1];
        return index;
        
    }
}
//best code
class Solution1 {
    public int removeDuplicates(int[] nums) {
        int count=1;
        int index=0;
        nums[index]= nums[0];
       for(int i=1;i<nums.length;i++){
        if(nums[index]!=nums[i]){
nums[index+1]= nums[i];
index++;
count++;
        }
       }
        return count;
    }
}