n = int(input())
answer = ''
for x in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    answer += str(min(a,b)) + ' '

print(answer)