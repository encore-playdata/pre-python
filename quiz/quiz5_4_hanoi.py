"""
하노이의 탑
"""


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return

    other_peg = 6 - start_peg - end_peg

    hanoi(num_disks - 1, start_peg, other_peg)
    print(f"{start_peg}번 기둥의 {num_disks}번 원반을 {end_peg}번 기둥에 옮긴다.")
    hanoi(num_disks - 1, other_peg, end_peg)


hanoi(3, 1, 3)
