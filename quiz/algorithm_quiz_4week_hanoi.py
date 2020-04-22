'''
    하노이의 탑
'''
def hanoi(num, _from, _by, _to):
    #탈출 조건
    if num == 1:
        print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮긴다.".format(_from, num, _to))
        return

    hanoi(num-1, _from, _to, _by)
    print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮긴다.".format(_from, num, _to))
    hanoi(num-1, _by, _from, _to)

print(hanoi(3,1,2,3))
