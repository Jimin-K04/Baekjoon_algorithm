N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

cnt = 0

for target in range(N):
    left = 0
    right = N-1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum > numbers[target]:
            right -= 1
        elif sum < numbers[target]:
            left += 1
        else:
            if left == target:
                left += 1
            elif right == target:
                right -= 1
            else:
                cnt += 1
                break
print(cnt)