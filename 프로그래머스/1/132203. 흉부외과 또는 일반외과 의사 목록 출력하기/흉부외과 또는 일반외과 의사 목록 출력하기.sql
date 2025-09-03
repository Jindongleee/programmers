-- 코드를 입력하세요
SELECT dc.dr_name, dc.dr_id, dc.mcdp_cd, date_format(dc.hire_ymd,'%Y-%m-%d') as hire_ymd
from doctor as dc 
where dc.mcdp_cd = 'cs' or dc.mcdp_cd = 'gs'
order by dc.hire_ymd desc;