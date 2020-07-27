def hanoi(n, start, end):
    if n == 0:
        return

    middle = 6 - start - end

    hanoi(n-1, start, middle)
    print(f"{start}번 기둥의 {n}번 원반을 {end}번 기둥에 옮긴다.")
    hanoi(n-1, middle, end)

hanoi(3, 1, 3)