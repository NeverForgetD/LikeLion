n, x = map(int, input("n과 x 를 입력해주세요(띄어쓰기로 구분)\n").split())

num_list = list(map(int, input(f"n({n})개의 정수를 입력해주세요(띄어쓰기로 구분)\n").split()))
isInputGood = len(num_list) == n

print(".\n.\n.")
if isInputGood:
    for i in range (n):
        if num_list[i] > x:
            print(num_list[i], end=" ")
else:
    print("입력이 올바르지 않습니다.")