n = int(input())
student_marks = {}
suma=0

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

#print(student_marks)
for name, scores in student_marks.items() :
    if name == query_name :
        for i in scores:
            suma += i
            print (i/3)


