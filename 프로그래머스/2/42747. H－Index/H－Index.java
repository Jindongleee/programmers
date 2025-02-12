import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        // 같아야 되는 것은 citations의 h값과 그 이상이 h번인경우
        // ex 6이면 6번 이상 인용이 1번 따라서 값이 다름
        // 전체 길이 - 해당 인덱스 값 > 해당 인덱스 값 -> 그게 최대 값
        Arrays.sort(citations);
        
        for(int i=0; i < citations.length;i++){
            if((citations.length-i)<=citations[i])
                return citations.length-i;
        }
         
        return 0;
    }
}