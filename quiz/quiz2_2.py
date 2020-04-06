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

def print_datetime():
    from datetime import datetime

    year = int(input("연도를 입력하시오 : "))
    month = int(input("월을 입력하시오 : "))
    day = int(input("일을 입력하시오 : "))

    weekday_num = datetime(year, month, day).weekday()
    weekday_list = ['월', '화', '수', '목', '금', '토', '일']

    print('{}년 {}월 {}일은 {}요일 입니다.'.format(year, month, day, weekday_list[weekday_num]))

print_datetime()