-- 코드를 입력하세요
#### 정답 1 ####
select NAME
from ANIMAL_INS
order by datetime limit 1 

#### 정답 2 ####

# select name
# from ANIMAL_INS
# where DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)