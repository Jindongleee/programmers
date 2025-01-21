import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 1;
        int count = nums.length/2; //이것의 개수가 초과하면 안돼
        
        Arrays.sort(nums); //오름차순
        
        for(int i=0;i<nums.length;i++){
            if(i>=1 && (nums[i-1] != nums[i]))
                answer++;
        }
        
        if(answer>count){
            answer=count;
            return answer;
        }
        
        return answer;
    }
}