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

def print_day_of_the_week(year, month, day):
    weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    weekday = datetime.date(year, month, day).weekday()
    return weekday_list[weekday]

my_year = int(input('연도를 입력하시오 : '))
my_month = int(input('월을 입력하시오 : '))
my_day = int(input('일을 입력하시오 : '))

print(f'{my_year}년 {my_month}월 {my_day}일은 {print_day_of_the_week(my_year, my_month, my_day)} 입니다.')