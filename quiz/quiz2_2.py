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

import calendar

myYear = int(input('연도를 입력하시오 : '))
myMonth = int(input('월를 입력하시오 : '))
myDay = int(input('일를 입력하시오 : '))


def printDayOfTheWeek(a, b, c):
    a = calendar.weekday(a, b, c)
    if a == 0:
        a = "월요일"
        return a
    elif a == 1:
        a = "화요일"
        return a
    elif a == 2:
        a = "수요일"
        return a
    elif a == 3:
        a = "목요일"
        return a
    elif a == 4:
        a = "금요일"
        return a
    elif a == 5:
        a = "토요일"
        return a
    else:
        a = "일요일"
        return a


print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))

