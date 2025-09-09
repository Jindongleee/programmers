-- 코드를 입력하세요
# # 1. 생일이 3월인 여성
# SELECT member_id, member_name, gender, date_of_birth
# from member_profile
# where gender = 'W' and month(date_of_birth)=3 and tlno is not NULL
# order by member_id asc;

SELECT member_id, member_name, gender, date_format(date_of_birth,'%Y-%m-%d') as DATE_OF_BIRTH
FROM member_profile
WHERE gender = 'W'
  AND MONTH(date_of_birth) = 3
  AND tlno IS NOT NULL
ORDER BY member_id ASC;