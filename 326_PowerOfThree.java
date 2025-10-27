//jacks code
class Solution {
    public boolean isPowerOfThree(int n) {
        double m=(double)n;
        while(m>1)
        {
            m/=3;
        }
        if(m==1)
        return true;
        else
        return false;
        
    }
}
//best code
class Solution1 {
    public boolean isPowerOfThree(int n) {
        if(n<1)
        return false;
        while(n%3==0){
            n=n/3;
        }
        return n==1;
    }
}
