"""
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
"""


def is_palindrome(word):
    list_word = list(word)
    # is_palindrome 메서드에서 word 를 넘겨받아 list(word)로 리스트화 시킨다
    for i in range(0, len(list_word) // 2):
        # for 문으로 word 의 절반까지만 검사
        # /를 사용하면 float 형태가 나오기 때문에 //를 사용
        if list_word[i] == list_word[len(list_word) - 1 - i]:
            # [0]과 [-1]마지막 인덱스만 검사
            # len(list)는 1부터 시작하기 때문에 -1가 마지막 인덱스 임을 뜻한다
            continue    # 조건을 계속해서 검사
        else:
            return False    # 팰린드롬이 아니라면 False 출력
    return True     # 팰린드롬이라면 True 출력


print(is_palindrome("radio"))       # 팰린드롬 검사
print(is_palindrome("토마토"))       # 팰린드롬 검사

