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
answer = 'no'
while answer == 'no':
    year = int(input('몇 년:'))
    month = int(input('몇 월:'))
    day = int(input('몇 일:'))
    print('입력하신 날짜가 {}년 {}월 {}일이 맞습니까? \n 맞으면 yes 아니면 no라고 말씀해주세요.'.format(year, month, day))
    answer = input()
    while not ((answer == 'no') or (answer == 'yes')):
        answer = input('답변은 yes나 no로만 해주세요.')

luna = -1
for i in range(0, year, 4):
    if (i % 100 == 0) & (i % 400 != 0):
        continue
    luna += 1

year_modulo = year + luna  # 1년이 정확히 지나면 같은 월 같은 일에는 요일이 +1이 된다. e.g) 작년 오늘: 월, 올해 오늘: 화

day_per_month = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]  # n월이 지날때마다 같은 일자에는 요일이 +day_per_month[n-1]이 된다.
month_day = 0
for i in range(month - 1):
    month_day += day_per_month[i]

total = year_day + month_day + day
if (year % 4 == 0) & (month > 2):
    if (i % 100 == 0) & (i % 400 != 0):
        pass
    total += 1

modulo = total % 7
num_day = {
    1: '월',
    2: '화',
    3: '수',
    4: '목',
    5: '금',
    6: '토',
    0: '일'
}
print('{}년 {}월 {}일은 {}요일 입니다.'.format(year, month, day, num_day[modulo]))