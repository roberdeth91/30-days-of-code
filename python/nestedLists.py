
students = []

for i in range(int(input())):
    name = input()
    score = float(input())
    students.append ([name , score])
    
students.sort(key=lambda x: x[1], reverse=False)
print(students)
