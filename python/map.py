n = int(input())
arr = map(int, input().split())
maxi = 0
secMaxi = 0
c=0

for i in arr:
    if maxi > i and c != 0 :
        secMaxi = maxi
        maxi = i
        print("loop2",maxi, secMaxi)
    elif i < maxi and i > secMaxi :
        secMaxi = i
        print("loop3",maxi, secMaxi)
    elif i > maxi :
        maxi = input
        c += 1
        print("loop 0:",maxi, secMaxi)

print(secMaxi)


