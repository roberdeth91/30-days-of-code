if __name__ == '__main__':
    N = int(input())
    arr = []
for i in range(N):
    partes = input().split()
    if partes[0] == "append":
        arr.append(int(partes [1]))
    elif partes[0] == "print":
        print(arr)
    elif partes[0] == "insert":
        arr.insert(int(partes[1]), int(partes[2]))
    elif partes[0] == "remove":
        arr.remove(int(partes[1]))
    elif partes[0] == "sort":
        arr.sort()
    elif partes[0] == "pop":
        arr.pop()
    elif partes[0] == "reverse":
        arr.reverse()



