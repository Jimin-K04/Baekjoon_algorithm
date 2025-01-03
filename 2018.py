#굳이 배열을 만들 필요가 없다 메모리 초과과
N = int(input())

cnt = 1
left = 1
right = 1
sum = 1

while right < N:
    if sum > N:
        sum -= left
        left += 1
    elif sum < N:
        right += 1
        sum += right
    else:
        cnt += 1
        right += 1
        sum += right

print(cnt)