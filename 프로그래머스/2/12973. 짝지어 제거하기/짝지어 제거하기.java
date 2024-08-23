import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int i=1;
        
        char[] c = s.toCharArray();
        
        Stack<Character> stack = new Stack<>();
        
        stack.push(c[0]);
        while(i<c.length){
            
            if(!stack.isEmpty() && stack.peek()==c[i]){
                stack.pop();
            }
            else
                stack.push(c[i]);
            i++;
        }
        
        if(stack.isEmpty())
            return 1;
        
        else
            return 0;
    }
}