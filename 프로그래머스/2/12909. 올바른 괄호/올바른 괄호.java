import java.util.Stack;
import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        if(s.length()==0)
            return false;
        
        for(int i=0;i<s.length();i++){
            char a = s.charAt(i);
            
            if(a==')'){
                if(stack.isEmpty())
                    return false;
                stack.pop();
            }
            else 
                stack.push(a);
        }
        
        return stack.isEmpty();
        
    }
}