//neems code
//time is O(n) cuz single for loop
//space is O(1)
class Solution {
    public boolean judgeCircle(String moves) {
        int sum=0;
        for(int i=0;i<moves.length();i++)
        {
            char c = moves.charAt(i);
            if(c=='L')
                sum=sum+10;
            if(c=='R')
                sum=sum-10;
            if(c=='U')
                sum=sum+2;
            if(c=='D')
                sum=sum-2;
        }
        return sum==0;
    }
}

//best soln but has same complexity so idk
class Solution1 {
    static {
        String[] arr = new String[1];
        for (int i = 0; i < 500; i++){
            judgeCircle("");
        }
    }
    public static boolean judgeCircle(String moves) {
        int[] freq = new int[26];
        char[] move = moves.toCharArray();
        if(move.length % 2 != 0) return false;
        for(char ch : move){
            freq[ch - 'A']++;
        }
        if(freq['U' - 'A'] == freq['D' - 'A'] && freq['L' - 'A'] == freq['R' - 'A']) return true;
        return false;
    }
}