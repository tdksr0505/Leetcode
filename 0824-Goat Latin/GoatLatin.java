class Solution {
    public String toGoatLatin(String S) {
        String[] strArray = S.split(" ");
        String aStr = "a";
        String str = "";
        int i;
        
        for(i=0;i<strArray.length;i++){
            if(isVowel(strArray[i].charAt(0))){
                strArray[i]+="ma";
            }
            else{
                char prefix = strArray[i].charAt(0);
                strArray[i] = strArray[i].substring(1);
                strArray[i]+=prefix;
                strArray[i]+="ma";
            }
            strArray[i] += aStr;
            aStr += "a";
        }
        for(i=0;i<strArray.length;i++){
            str += strArray[i];
            if((i+1)!=strArray.length)
                str+=" ";
        }
        return str;
    }
    public boolean isVowel(char c){
        if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||
          c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
            return true;
        return false;
    }
}