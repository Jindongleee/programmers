import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder result = new StringBuilder();
        boolean capitalizeNext = true;

        for (char c : s.toCharArray()) {
            if (c == ' ') {
                result.append(c);
                capitalizeNext = true;
            } else {
                if (capitalizeNext) {
                    result.append(Character.toUpperCase(c));
                } else {
                    result.append(Character.toLowerCase(c));
                }
                capitalizeNext = false;
            }
        }

        return result.toString();
    }
}