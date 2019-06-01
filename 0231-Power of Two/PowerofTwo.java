class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n==1) return true;
        for(;n>=2;n/=2){
            if(n%2!=0) return false;
            if(n==2) return true;
        }
        return false;
    }
}