/*
    SELF JOIN 여러 번 해서 3세대까지 구하기
    
    | A.ID | A.PARENT_ID | B.PARENT_ID | C.PARENT_ID |
    | ---- | ----------- | ----------- | ----------- |
    |   1  |     NULL    |     NULL    |     NULL    |
    |   2  |     NULL    |     NULL    |     NULL    |
    |   3  |       1     |     NULL    |     NULL    |
    |   4  |       2     |     NULL    |     NULL    |
    |   5  |       2     |     NULL    |     NULL    |
    |   6  |       4     |       2     |     NULL    | <- 3세대
    |   7  |       3     |       1     |     NULL    | <- 3세대
    |   8  |       6     |       4     |       2     |
 */
SELECT A.ID
FROM ECOLI_DATA AS A
JOIN ECOLI_DATA AS B ON A.PARENT_ID = B.ID
JOIN ECOLI_DATA AS C ON B.PARENT_ID = C.ID
WHERE C.PARENT_ID IS NULL
ORDER BY A.ID ASC;