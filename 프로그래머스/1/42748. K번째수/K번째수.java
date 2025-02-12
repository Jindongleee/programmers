import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] array, int[][] commands) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < commands.length; i++) {
            int start = commands[i][0] - 1;  // 시작 인덱스 (0 기반)
            int end = commands[i][1];        // 끝 인덱스 (subArray는 끝 인덱스를 포함하지 않으므로 그대로 사용)
            int k = commands[i][2] - 1;      // k번째 인덱스 (0 기반으로 변환)
            
            // 부분 배열 추출 및 정렬
            int[] subArray = Arrays.copyOfRange(array, start, end);
            Arrays.sort(subArray);
            
            // k번째 요소 추가
            list.add(subArray[k]);
        }
        
        return list;
    }
}