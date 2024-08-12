// import java.util.*;

// class Solution {
//     public int[] solution(String s) {
//         int[] answer = {};
//         int count=0;
//         int changeCount=0;
//         int num;
        
//         while(!s.equals("1")){
//             for(int i=0;i<s.length();i++){
//                 if(s.charAt(i)=='0');
//                     count++;
//             }
            
//             s=s.replace("0","");
            
//             //1의 개수를 2진수로 변환
//             s=Integer.toBinaryString(s.length());
            
//             //2진수 10진수로 변환
//             //num = Integer.parseInt(s,2);
            
//             changeCount++;
//         }
        
//         answer[0]=changeCount;
//         answer[1]=count;
        
//         return answer;
        
        
//     }
// }

import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];  // 배열 크기 지정
        int count = 0;
        int changeCount = 0;
        
        while (!s.equals("1")) {  // 문자열 비교 수정
            int zeroCount = 0;
            
            // 0의 개수를 세고 제거
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0')
                    zeroCount++;
            }
            count += zeroCount;
            s = s.replace("0", "");  // 0을 제거한 후 s에 다시 저장
            
            // 남은 문자열의 길이를 이진수로 변환
            s = Integer.toBinaryString(s.length());
            changeCount++;
        }
        
        answer[0] = changeCount;
        answer[1] = count;
        
        return answer;
    }
}
