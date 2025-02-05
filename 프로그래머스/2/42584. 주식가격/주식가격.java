import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        for (int i = 0; i < prices.length; i++) {
            int count = 0;
            
            for (int j = i + 1; j < prices.length; j++) {
                count++; // 초 증가
                
                if (prices[i] > prices[j]) { // 가격이 떨어지면 중단
                    break;
                }
            }
            
            answer[i] = count;
        }

        return answer;
    }
}