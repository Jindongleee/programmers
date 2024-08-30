import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int i=0;
        int left=0;
        int right=people.length-1;
        int count=0;
        
        
        Arrays.sort(people);
     
        while(left<=right){     
            
            if(limit<people[left]+people[right]){
                right--;
            }
            else{
                left++;
                right--;
            }
            count++;
            
        }
        
        return count;
    }
}