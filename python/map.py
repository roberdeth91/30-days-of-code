n = int(input())
arr = map(int, input().split())
maxi = 0
secMaxi = 0
val = 0
print (arr)

for i in arr:
    val = arr[i]
    if val > maxi:
        maxi = val

print(maxi)

