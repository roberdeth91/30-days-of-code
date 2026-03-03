
students = []

for i in range(int(input())):
    name = input()
    score = float(input())
    students.append ([name , score])
    
students.sort(key=lambda x: x[1], reverse=False)
#print(students[1][0])

second_lowest = students[1][1]

for name,score in students :
    if score == second_lowest :
        print(name)
