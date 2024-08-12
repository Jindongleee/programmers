import java.util.*;

class Solution {
    public String solution(String s) {
        String[] str = s.split(" ");
        int[] intArray = new int[str.length];
        String answer =" ";
        
        for(int i=0; i<str.length;i++){
            intArray[i]=Integer.parseInt(str[i]);
        }        
        
        int max = intArray[0];
        int min = intArray[0];
        for(int i=0;i<intArray.length;i++){
           	max = Math.max(max, intArray[i]);
			min = Math.min(min, intArray[i]);
        }
        
        return min+answer+max;
    }
}