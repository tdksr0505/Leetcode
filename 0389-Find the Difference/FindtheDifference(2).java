class Solution {
    public char findTheDifference(String s, String t) {
        int i, j;
        StringBuilder sb = new StringBuilder(t);
        for(i=0;i<s.length();i++){
            j = sb.indexOf(String.valueOf(s.charAt(i)));
            sb.deleteCharAt(j);
        }
        return sb.charAt(0);        
    }
}