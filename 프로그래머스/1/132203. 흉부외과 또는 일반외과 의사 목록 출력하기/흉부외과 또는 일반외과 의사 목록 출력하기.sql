-- 코드를 입력하세요
# data_format -> y(00), Y(2000) 서로 다름, m(7), M(July) , d(1), D(1st)
SELECT dc.dr_name, dc.dr_id, dc.mcdp_cd, date_format(dc.hire_ymd,'%Y-%m-%d') as hire_ymd
from doctor as dc 
where dc.mcdp_cd = 'cs' or dc.mcdp_cd = 'gs'
order by dc.hire_ymd desc;