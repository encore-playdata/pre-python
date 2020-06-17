"""8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오

예시
<입력>
정수를 입력하세요 : 14

<출력>
짝수입니다.
"""
def even_odd(n):
    if n % 2 == 0:
        return '짝수'
    else:
        return '홀수'

def main():
    n = int(input('정수를 입력하세요 : '))
    print(even_odd(n))

main()