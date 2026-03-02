n = int(input())
arr = map(int, input().split())
maxi = -1000
secMaxi = -1000
c=0

for i in arr:
    if  i > maxi :
        secMaxi = maxi
        maxi = i
        print("loop1",maxi, secMaxi)
    elif secMaxi < i and i < maxi :
        secMaxi = i
        print("loop2",maxi, secMaxi)
    elif i == maxi :
        print("loop 3:",maxi, secMaxi)

print(secMaxi)


