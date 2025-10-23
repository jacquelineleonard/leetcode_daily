//Check whether a given number is a perfect number (equal to the sum of its proper divisors).
//my solution -  time complexity is O(num)
class Solution {
    public boolean checkPerfectNumber(int num) {
        int sum=0;
        for(int i=1;i<num;i++)
        {
            if(num%i==0)
                sum=sum+i;
        }
        return(sum==num);
    }
}

//optimal solution
//time is O(root num)
//space is O(1)
class Solution1 {
    public boolean checkPerfectNumber(int num) {
        if (num == 1) return false;
        int sum = 1;  // 1 is always a divisor
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                sum += i;
                if (i != num / i) sum += num / i; // avoid double-counting sqrt
            }
        }
        return sum == num;
    }
}