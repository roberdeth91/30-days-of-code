n = int(input())
arr = map(int, input().split())
maxi = 0
secMaxi = 0
val = 0
print (arr)
c=0

for i in arr:
    val = i
    if val > maxi and c != 0:
        secMaxi = maxi
        print("entro 1")
    elif val > maxi :
        maxi = val
        c += 1
        print("entro 2")

print(maxi)
print(secMaxi)


