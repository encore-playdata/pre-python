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

re = []
re = []
def is_palindrome(re):
    if re[0] == re[-1]:
        a = "TRUE"
        return a
    else:
        a = "FALSE"
        return a

print(is_palindrome("radio"))
print(is_palindrome("토마토"))
