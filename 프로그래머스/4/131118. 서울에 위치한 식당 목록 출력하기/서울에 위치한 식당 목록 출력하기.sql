-- 코드를 입력하세요
# inner join, outer join(left join, right join, full outer join), cross join ,self join , natural join

# 서울에 위치해야함
# # 리뷰 평균점수 소수점 세번째 자리에서 반올림 -> 내림차순 -> 즐겨찾기 기준 내림차순 정렬
SELECT ri.rest_id, ri.rest_name, ri.food_type, ri.favorites, ri.address, round(avg(rr.review_score),2) as score
from rest_info ri
inner join rest_review rr on ri.rest_id = rr.rest_id
where ri.address like '서울%'
GROUP BY ri.rest_id, ri.rest_name, ri.food_type, ri.favorites, ri.address
order by score desc, ri.favorites desc;

# 이중 select문은 조건에 들어오는건 단일문이어야함 (컬럼 하나라는 뜻)