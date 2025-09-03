-- 코드를 입력하세요
# 12세 이하의 여자 환자
# 전화번호가 없는 경우 -> NONE,
# 나이를 기준으로 desc, 나이가 같다면 환자이름으로 오름차순

SELECT pt_name, pt_no, gend_cd, age, COALESCE(tlno, 'NONE') AS tlno 
from patient pt
where gend_cd = 'W' and age <= 12 
order by pt.age desc, pt.pt_name asc;