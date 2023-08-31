list =[]
mark = []
grade = []
for i in range(int(input())):
    name = input()
    score = float(input())
    cgpa = float(input())
    list.append([name, score, cgpa])
    mark.append(score)
    grade.append(cgpa)
# print(list)
mark.sort()
second_min = 0
minim = mark[0]
list.sort()
for i in mark:
    if i != minim:
        second_min = i
        break
for i in list:
    if i[1] == second_min:
        print(i[0])
        
grade.sort()
second = 0
minim = grade[0]
for i in grade:
    if i != minim:
        second = i
        break
for i in list:
    if i[2] == second:
        print(i[0], i[1], i[2])