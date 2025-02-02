import java.util.*;
import java.util.Stack;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        Stack<Integer> stack = new Stack<>();
        
        for(Integer i : arr) {
            
            if(stack.peek() != i || stack.peek() != null)
                stack.push(i);
        }
        
        System.out.print(stack);
        
        return answer;
    }
}