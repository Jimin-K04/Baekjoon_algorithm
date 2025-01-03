#고유 번호가 M 과 같고 left == right 인 경우 제외외
N = int(input())
M = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

left = 0
right = N - 1
cnt = 0
sum = numbers[left] + numbers[right]

while left < right:
    if sum > M:
        sum -= numbers[right]
        right -= 1
        sum += numbers[right]
    elif sum < M:
        sum -= numbers[left]
        left += 1
        sum += numbers[left]
    else:
        cnt += 1
        left += 1
        sum = numbers[left] + numbers[right]

print(cnt)