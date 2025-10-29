//jacks code
import java.util.*;
class Solution {
    public int removeElement(int[] nums, int val) {
        int count=0;
        for (int i=0;i<nums.length;i++)
        {
            if(nums[i]==val)
            {
              nums[i]=51;
            }
            else
            count++;
        }
        Arrays.sort(nums);
        return count;
    
    }
}
//best code
class Solution1 {
    public int removeElement(int[] nums, int val) {
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[index++] = nums[i];
            }
        }
        return index; // new length
    }
}
