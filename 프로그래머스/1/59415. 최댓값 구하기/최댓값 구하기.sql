-- 코드를 입력하세요
# SELECT DATETIME
# from ANIMAL_INS 
# order by DATETIME desc limit 1;

-- 최근일수록 DATETIME TYPE은 큰 값이다.
SELECT MAX(DATETIME) 시간
FROM ANIMAL_INS;