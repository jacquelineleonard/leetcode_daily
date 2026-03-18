//jacks code
class Solution {
    public int smallestNumber(int n) {
        
        for(int i=n;;i++)
        {
            int x=i,flag=1;
            while(x>1)
            {
                if(x%2==0)
                {
                    flag=0;
                    break; 
                }
                if(x%2==1)
                    x=x/2;
            }
            if (flag==1)
            return i;
        }
}
}
//best code
class Solution1 {
    public int smallestNumber(int n) {
        int x=n;
        while((x&(x+1))!=0){
            x++;
        }
        return x;
    }
}