class Solution {
    public char findTheDifference(String s, String t) {
        int i, j;
        for(i=0;i<s.length();i++){
            if(t.indexOf(s.charAt(i))!=-1){
                j = t.indexOf(s.charAt(i));
                t = t.substring(0, j) + t.substring(j+1);
            }
        }
        return t.charAt(0);        
    }
}