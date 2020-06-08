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

def is_palindrome(word):

  for i in range(len(word) // 2):
     if word[i] == word[-1 - i]:
        return True
     else:
        return False

print(is_palindrome("radio"))
print(is_palindrome("토마토"))


'''1. 함수를 만든다 
   2. 문자열의 처음과 끝이 같으면 트루, 틀리면 폴스
3. 문자열의 처음과 끝이 같은지 확인하는 함수를 찾는다.
4. 적용, 정리'''