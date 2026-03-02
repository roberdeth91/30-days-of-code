n = int(input())
arr = map(int, input().split())
maxi = 0
secMaxi = 0
val = 0
print (arr)
c=0

for i in arr:
    if i > maxi and c != 0:
        secMaxi = maxi
        print("entro 1;",secMaxi,  i)
    elif i > maxi :
        maxi = val
        c += 1
        print("entro 2:",maxi, i )

print(maxi)
print(secMaxi)


