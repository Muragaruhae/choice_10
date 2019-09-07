n = int(input())
count = 0
for i in range(n):
    t,x,y = map(int,input().split())
    if (x + y <= t and t % 2 == (x + y) % 2):
        continue
    else:
        print("No")
        exit()
print("Yes")