//neems code
//time and space is O(d)
//where d is no. of dgits
//conv to string is d
//scanning for 6 is d
//conv to array is d
//conv to int is d
//4d = O(d)
class Solution {
    public int maximum69Number(int num) {
        String six = String.valueOf(num);
        int f = six.indexOf('6');   

        if (f != -1) {
            char[] arr = six.toCharArray(); 
            arr[f] = '9';                   
            int res = Integer.parseInt(new String(arr));
            return res;
        }

        return num; 
    }
}

//best code - uses int itself
//time and space is O(1)
class Solution1 {
    public int maximum69Number (int num) {
        int temp = num;
        int pos = -1;
        int i = 0;
        
        while (temp > 0) {
            if (temp % 10 == 6) pos = i;
            temp /= 10;
            i++;
        }
        
        return (pos == -1) ? num : num + 3 * (int)Math.pow(10, pos);
    }
}
