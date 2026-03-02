n = int(input())
arr = map(int, input().split())
maxi = 0
secMaxi = 0
c=0

for i in arr:
    if i > maxi : 
        maxi = i
        c += 1
    elif maxi > i and c != 0 :
        secMaxi = maxi
        maxi = i
    elif i > secMaxi :
        secMaxi = i

print(secMaxi)


