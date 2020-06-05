"""8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오

예시
<입력>
정수를 입력하세요 : 14

<출력>
짝수입니다.
"""

def checkEven():
    if N % 2 == 0: return '짝수입니다.'
    else: return '홀수입니다.'

N = int(input('정수를 입력하세요 : '))

print(checkEven())