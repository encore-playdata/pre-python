'''
1.
문자열의 역순이 문자열과 동일하면 팰린드롬이라고 한다.
예를 들어, "토마토"는 팰린드롬이지만, "radio"는 팰린드롬이 아니다.
문자열이 주어지면 python 함수를 작성하여 팰린드롬인지 여부를 확인하시오.

테스트코드
<입력>
print(is_palindrome("radio"))
print(is_palindrome("토마토"))

<출력>
False
True
'''

word = input('단어를 입력하세요: ')

is_palindrome = True  # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):  # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:  # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False  # 회문이 아님
        break

print(is_palindrome)  # 회문 판별값 출력