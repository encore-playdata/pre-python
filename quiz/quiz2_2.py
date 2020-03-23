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

import datetime


def printDayOfTheWeek(year, month, day):
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    return days[datetime.date(year, month, day).weekday()]


print('연도를 입력하시오 : ', end='')
myYear = int(input())
print('월을 입력하시오 : ', end='')
myMonth = int(input())
print('일을 입력하시오 : ', end='')
myDay = int(input())
print('{}년 {}월 {}일은 {} 입니다.'.format(myYear, myMonth,
                                    myDay, printDayOfTheWeek(myYear, myMonth, myDay)))
