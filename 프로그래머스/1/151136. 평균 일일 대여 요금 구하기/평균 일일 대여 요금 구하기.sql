-- 코드를 입력하세요
# 1. 자동차 종류 'SUV'
# 2. 이 자동차들의 평균 일일 대여 요금 출력
# 3. 요금 소수 첫번째 자리에서 반올림
# 4. 컬럼명은 average_fee

SELECT round(avg(daily_fee), 0) as average_fee from car_rental_company_car where car_type = 'SUV'