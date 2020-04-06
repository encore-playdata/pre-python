"""17. 1988년 ~ 2060년까지 중 월드컵이 개최되는 연도를 출력하시오


예시
<출력>
1988
1992
1996
2000
2004
2008
2012
2016
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
"""

list = [1988, 2060]
i = 1
while True:
    nextYear = 1988 + 4*i
    if 1988 + 4*(i-1) < nextYear < list[-1]:
        list.insert(-1, nextYear)
    else:
        break
    i = i+1

for i in list:
    print(i)