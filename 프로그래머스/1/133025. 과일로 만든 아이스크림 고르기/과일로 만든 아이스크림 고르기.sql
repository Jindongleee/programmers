-- 코드를 입력하세요
# 1. first_half테이블에서 총주문량이 3000보다 높고 아이스크림 주 성분이 과일
# 2. 총주문량이 큰 순서대로 조회 -> 내림차순 desc
SELECT fh.FLAVOR from first_half fh
inner join icecream_info ii on fh.flavor = ii.flavor 
where fh.total_order > 3000 and ii.ingredient_type = 'fruit_based'
order by fh.total_order desc;