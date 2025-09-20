-- 코드를 입력하세요
# 경기도에 위치
# 냉동 시설 여부가 NULL -> N으로 출력
# 창고 ID기준으로 ASC
SELECT warehouse_id, warehouse_name, address, coalesce(freezer_yn,'N') as freezer_yn
from food_warehouse 
where address like '%경기%'