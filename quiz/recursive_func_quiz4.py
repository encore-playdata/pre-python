"""
4. 재귀 호출을 이용한 <하노이 탑> 문제

입력 예시)
hanoi(3, 1, 3)

출력 결과)
1번 기둥의 1번 원반을 3번 기둥에 옮긴다.
1번 기둥의 2번 원반을 2번 기둥에 옮긴다.
3번 기둥의 1번 원반을 2번 기둥에 옮긴다.
1번 기둥의 3번 원반을 3번 기둥에 옮긴다.
2번 기둥의 1번 원반을 1번 기둥에 옮긴다.
2번 기둥의 2번 원반을 3번 기둥에 옮긴다.
1번 기둥의 1번 원반을 3번 기둥에 옮긴다.
"""

def hanoi(n_disk, start_peg, end_peg):
    # 옮길 원판이 없으면 부분 문제를 나누지 않고 함수를 끝냄
    if n_disk == 0: return
    else:
        other_peg = 6 - start_peg - end_peg
        # 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
        hanoi(n_disk - 1, start_peg, other_peg)
        # 가장 큰 원판을 start_peg에서 end_peg로 이동
        print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮긴다.".format(start_peg, n_disk, end_peg))
        # 나머지 원판들을 other_peg에서 end_peg로 이동
        hanoi(n_disk - 1, other_peg, end_peg)

hanoi(3, 1, 3)