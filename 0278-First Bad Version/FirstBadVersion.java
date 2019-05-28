/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int i;
        int start = 1;
        int end = n;
        if(n==1) return 1;
        for(i=n/2;i>=1;){
            if(isBadVersion(i)){
                if(i==1) break;
                if(!isBadVersion(i-1)) break; 
                end = i-1;
            }
            else {
                start = i+1;
            }
            i = start + ((end-start)/2);
        }
        return i;
    }
}