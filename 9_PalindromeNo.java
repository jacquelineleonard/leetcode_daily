//jacks code
import java.lang.Math;
class Solution {
    public boolean isPalindrome(int x) 
    {
        int n=x,f=0;
        while(n!=0)
        {
            int r=n%10;
            n=n/10;
            f=f*10+Math.abs(r);
        }
        if(x==f)
        return true;
        else
        return false;
    }
}
//best code
class Solution1 {
    public boolean isPalindrome(int x) {
        // Negative numbers or numbers ending with 0 (except 0 itself) can't be palindromes
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversedHalf = 0;
        while (x > reversedHalf) {
            int digit = x % 10;
            reversedHalf = reversedHalf * 10 + digit;
            x /= 10;
        }

        // For even or odd number of digits
        return x == reversedHalf || x == reversedHalf / 10;
    }
}