s, p = map(int, input().split())
DNA = input()
target = {'A':0, 'C':0, 'G':0, 'T':0}
ACGT_num = list(map(int, input().split()))
st = 0 
en = p
check = 0 
ans = 0

for i in range(st, en):
    target[DNA[i]] += 1

while True:
    nums = list(target.values())
    check = 0
    
    for i in range(4):
        if ACGT_num[i] > nums[i]:
            check = 1
    if check == 0 :
        ans += 1
    if en >= s : break;
    target[DNA[st]] -= 1
    st+=1
    target[DNA[en]] += 1
    en+=1

print(ans)