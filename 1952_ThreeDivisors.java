//jacks code
class Solution {
    public boolean isThree(int n) {
        int count=0;
        for(int i=2;i<=n/2;i++)
        {
            if(n%i==0)
            count++;
        }
        if(count==1)
        return true;
        else 
        return false;
        
    }
}
//best code
class Solution1 {
    public boolean isThree(int n) {
        int s=2;
        for(int i=2;i<=n/2;i++){
            if(n%i==0)
            s++;
        }
        return s==3;
    }
}