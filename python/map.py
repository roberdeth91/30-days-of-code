n = int(input())
arr = map(int, input().split())
maxi = 0
secMaxi = 0
c=0

for i in arr:
    if i > maxi and c != 0 :
        secMaxi = maxi
        maxi = i
        print("entro 1;",secMaxi,  i)
    elif i > maxi :
        maxi = i
        c += 1
        print("entro 2:",maxi, i )
    elif i > secMaxi:
        secMaxi = i

print(maxi)
print(secMaxi)


