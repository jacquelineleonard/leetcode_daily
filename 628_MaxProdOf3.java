//jacks code 
import java.lang.Math;
import java.util.*;
class Solution {
    public int maximumProduct(int[] nums){
        int n[]=bubblesort(nums);
        return n[0]*n[1]*n[2];

    }
    public int[] bubblesort(int n[])
    {
        for(int i=0;i<(n.length-1);i++)
        {
            for(int j=0;j<(n.length-i-1);j++)
            {
                if(Math.abs(n[j])<Math.abs(n[j+1]))
                {
                    int temp=n[j];
                    n[j]=n[j+1];
                    n[j+1]=temp;
                }
                
            }
        }
        return n;
        
    }
}