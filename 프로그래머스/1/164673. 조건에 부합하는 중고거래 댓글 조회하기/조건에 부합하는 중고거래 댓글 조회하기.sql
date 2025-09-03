-- 코드를 입력하세요
# userd_goods_board -> 중고거래 게신파 정보
# userd_goods_reply -> 테이블과 중고거래 게시판 첨부파일 정보

# SELECT ugb.TITLE,ugb.BOARD_ID,ugr.REPLY_ID,ugr.WRITER_ID,ugr.CONTENTS, date_format(ugb.created_date, '%y-%m-%d') as CREATED_DATE
# from used_goods_board ugb
# inner join used_goods_reply ugr
# on ugb.board_id = ugr.board_id
# where ugb.created_date between '2022-10-01' and '2022-10-31'
# order by ugr.created_date asc;

SELECT 
    ugb.TITLE,
    ugb.BOARD_ID,
    ugr.REPLY_ID,
    ugr.WRITER_ID,
    ugr.CONTENTS,
    DATE_FORMAT(ugr.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD ugb
INNER JOIN USED_GOODS_REPLY ugr
    ON ugb.BOARD_ID = ugr.BOARD_ID
WHERE ugb.CREATED_DATE >= '2022-10-01'
  AND ugb.CREATED_DATE < '2022-11-01'
ORDER BY 
    ugr.CREATED_DATE ASC,
    ugb.TITLE ASC;