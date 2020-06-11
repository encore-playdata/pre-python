'''
2.
년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하는 함수를 만드세요.
테스트코드
<입력>
print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))
<출력>
연도를 입력하시오 : 2020
월을 입력하시오 : 3
일을 입력하시오 : 13
2020년 3월 13일은 금요일 입니다.
'''

def printDayOfTheWeek():
    year = int(input('연도를 입력하시오 : '))
    month = int(input('월을 입력하시오 : '))
    day = int(input('일을 입력하시오 :'))
    basic_year = 365*(year-1)
    yun_year = (year-1)//4 - (year-1)//100 + (year-1)//400
    total = basic_year + yun_year
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = [31,29,31,30,31,30,31,31,30,31,30,31]
        for i in range(month-1):
            total += days[i]
    else:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(month-1):
            total += days[i]
            
    total += day
    if total % 7 == 0:
        answer = '일'
    if total % 7 == 1:
        answer = '월'
    if total % 7 == 2:
        answer = '화'
    if total % 7 == 3:
        answer = '수'
    if total % 7 == 4:
        answer = '목'
    if total % 7 == 5:
        answer = '금'
    if total % 7 == 6:
        answer = '토'
    print('{}년 {}월 {}일은 {}요일 입니다.'.format(year,month,day,answer))
    
printDayOfTheWeek()